import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "chwall"
        self.description = "Change desktop wallpaper."
        self.type = "applescript"

        

    def run(self,session,cmd_data):
        picture = raw_input(h.WW+"[>]"+h.WHITE+" Wallpaper Picture: "+h.ENDC)
        one = '"'
        payload = """
        tell application "Finder" to set desktop picture to POSIX file "/usr/local/share/picture.jpg"
        """
        session.send_command({"cmd":"rm","args":"/usr/local/share/picture.jpg"})
        session.upload_file(picture,"/usr/local/share","picture.jpg")
        cmd_data.update({"cmd":"applescript","args":payload})
        picture = session.send_command(cmd_data).strip()
        return ""
