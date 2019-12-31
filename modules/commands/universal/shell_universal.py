import modules.helper as h
import json
import os

class command:
    def __init__(self):
        self.name = "shell"
        self.description = "Open target device shell."
    
    def run(self,session,cmd_data):
	while 1:
	    uid = session.send_command({"cmd":"echo","args":"$UID"})
	    whoami = ""
	    if whoami == "":
		if uid[:-1] == "0":
	            whoami = "# "
	        else:
		    whoami = "$ "
	    shell = raw_input(h.WHITE+session.hostname+":"+session.current_directory+" "+session.username+whoami)
	    if not shell or shell.replace(" ","") == "":
	        continue
	    shelld = shell.split()[0]
	    shelld_data = {"cmd": shelld, "args":shell[len(shelld) + 1:]}
	    if shelld == "cd":
		result = json.loads(session.send_command(shelld_data))
                if 'error' in result:
        	    h.info_error(result['error'])
                elif 'current_directory' in result:
        	    session.current_directory = result['current_directory'].encode('utf-8')
                else:
        	     h.info_error('Unable to get current directory!')
	    if shelld == "ls":
                if not shelld_data['args']:
                    shelld_data['args'] = '.'
                data = session.send_command(shelld_data)
                try:
                    contents = json.loads(data)
                except:
                    print data
                    return
                keys = contents.keys()
                keys.sort()
                for k in keys:
                    if contents[k] == 4 or contents[k] == 10:
                        print h.COLOR_INFO + k + h.ENDC
                    else:
                        print k
	    if shelld == "exit":
                return
	    else:
		try:
		    result = session.send_command(shelld_data)
		    if result:
		        if shelld == "ls" or shelld == "cd":
			    pass
			else:
			    print result.rstrip()
		except KeyboardInterrupt:
	            session.send_command({"cmd":"killtask"})
