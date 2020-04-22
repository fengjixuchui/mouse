#!/usr/bin/env python

#            ---------------------------------------------------
#                              Mouse Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from os.path import expanduser
import core.helper as h

class command:
    def __init__(self):
        self.name = "exec"
        self.description = "Execute local shell command."
    
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
