class command:
    def __init__(self):
        self.name = "pid"
        self.description = "Get MPL process ID."
        self.type = "native"

    def run(self,session,cmd_data):
        print("PID: "+session.send_command(cmd_data))
