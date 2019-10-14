import modules.helper as h

class command:
    def __init__(self):
        self.name = "home"
        self.description = "Simulate a home button press."
    
    def run(self,session,cmd_data):
        error = session.send_command(cmd_data)
        if error:
        	print(h.RED+"[-]"+h.WHITE+" MPL Substrate is not installed!")
