import modules.helper as h
import re, os, time

class command:
    def __init__(self):
        self.name = "msub"
        self.description = "Install or uninstall MPL Substrate."
        self.usage = "Usage: msub [install|uninstall]"
    
    def run(self,session,cmd_data):
        if not cmd_data['args'] or not cmd_data['args'] in ['install','uninstall']:
       		print self.usage
       		return
       	if cmd_data['args'] == "install":
    	    h.info_general("Uploading mpl.dylib (1/2)...")
            session.upload_file("substrate/mpl.dylib","/Library/MobileSubstrate/DynamicLibraries",".mpl.dylib")
            time.sleep(0.5)
    	    h.info_general("Uploading mpl.plist (2/2)...")
            session.upload_file("substrate/mpl.plist","/Library/MobileSubstrate/DynamicLibraries",".mpl.plist")
            time.sleep(0.5)
            h.info_general("Restarting SpringBoard...")
            time.sleep(1)
            session.send_command({"cmd":"killall","args":"SpringBoard"})
        if cmd_data['args'] == "uninstall":
            h.info_general("Removing mpl.dylib (1/2)...")
            session.send_command({"cmd":"rm","args":"/Library/MobileSubstrate/DynamicLibraries/.mpl.plist"})
            time.sleep(0.3)
    	    h.info_general("Removing mpl.plist (2/2)...")
            session.send_command({"cmd":"rm","args":"/Library/MobileSubstrate/DynamicLibraries/.mpl.plist"})
            time.sleep(0.3)
            h.info_general("Restarting SpringBoard...")
            time.sleep(1)
            session.send_command({"cmd":"killall","args":"SpringBoard"})
