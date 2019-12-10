import os
from os.path import expanduser
import modules.helper as h

class command:
    def __init__(self):
        self.name = "exec"
        self.description = "Execute local shell commands."
    
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print "Usage: exec <command>"
            return
        else:
            print(h.CYAN+"[*]"+h.WHITE+" exec: "+cmd_data['args'])
            print("")
            split_args = cmd_data['args'].split()
            os.system(cmd_data['args'])

