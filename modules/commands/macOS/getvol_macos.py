import json
class command:
    def __init__(self):
        self.name = "getvol"
        self.description = "Get speaker output volume."
    	self.type = "applescript"

    def run(self,session,cmd_data):
        payload = "output volume of (get volume settings)"
        cmd_data.update({"cmd":"applescript","args":payload})
        print("Current Volume: "+session.send_command(cmd_data))
