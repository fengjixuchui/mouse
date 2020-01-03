class command:
	def __init__(self):
		self.name = "reboot"
		self.description = "Reboot device."

	def run(self,session,cmd_data):
		session.send_command({"cmd":"reboot","args":""})
