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

import time
import getpass
import core.helper as h

class command:
    def __init__(self):
        self.name = "su"
        self.description = "Login as root."
        self.type = "eggsu"

    def run(self,session,cmd_data):
        password = getpass.getpass("Password: ")
        cmd_data['args'] = password
        password = password.replace("\\","\\\\").replace("'","\\'")
        cmd_data['cmd'] = "eggsu"
        result = session.send_command(cmd_data)
        if "root" in result:
            h.info_general("Root Granted!")
            time.sleep(0.2)
            h.info_general("Escalating Privileges...")
            if session.server.is_multi == False:
                session.server.update_session(session)
            else:
                session.needs_refresh = True
        else:
            h.info_error("Failed getting root!")
