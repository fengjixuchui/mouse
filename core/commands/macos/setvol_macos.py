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

class command:
    def __init__(self):
        self.name = "setvol"
        self.description = "Set output volume."
     
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print("Usage: setvol <level: 0-100>")
            return -1
        payload = "set volume output volume "+cmd_data['args']
        cmd_data.update({"cmd":"applescript","args":payload})
        error = session.send_command(cmd_data)
        if error:
            h.info_error("Failed to set output volume!")
