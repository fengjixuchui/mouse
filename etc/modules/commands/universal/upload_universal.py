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

import core.helper as h
import re, os

class command:
    def __init__(self):
        self.name = "upload"
        self.description = "Upload local file."
        self.usage = "Usage: upload <local_file> <remote_dir>"
    
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print self.usage
            return
        else:
            paths = re.split(r'(?<!\\) ', cmd_data['args'].rstrip())
            if len(paths) > 2:
                print "Usage: upload <local_file> <remote_dir>"
                return
            
            local_dir = os.path.split(paths[0])[0]
            local_file = os.path.split(paths[0])[1]
            
            if len(paths) == 1:
                remote_dir = "."
                remote_file = local_file
            else:
                remote_dir = os.path.split(paths[1])[0]
                if not remote_dir:
                    remote_dir = "."
                remote_file = os.path.split(paths[1])[1]
                if not remote_file:
                    remote_file = local_file

            w = os.environ['OLDPWD']
            os.chdir(w)

            session.upload_file(paths[0],remote_dir,remote_file)

            g = os.environ['HOME']
            os.chdir(g + "/mouse")

            h.info_general("File successfully uploaded!")
