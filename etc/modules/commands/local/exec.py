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
            w = os.environ['OLDPWD']
            os.chdir(w)
            
            split_args = cmd_data['args'].split()
            os.system(cmd_data['args'])
            
            g = os.environ['HOME']
            os.chdir(g + "/mouse")      
