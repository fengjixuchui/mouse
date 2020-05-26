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
import time
import base64
import json
try:
    # Win32
    from msvcrt import getch
except ImportError:
    # UNIX
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

class command:
    def __init__(self):
        self.name = "keyboard"
        self.description = "Control device keyboard."
        self.type = "applescript"
        self.id = 115

    def run(self,session,cmd_data):
        #do something with conn if you want
        h.info_general("Press Ctrl-C to stop.")
        h.info_general("Device keyboard:")
        while 1:
            key = getch()
            if key == chr(3):
                return ""
            payload = """tell application "System Events"
            keystroke \""""+key+"""\"
            end tell"""
            session.send_command({"cmd":"applescript","args":payload})
        return ""

