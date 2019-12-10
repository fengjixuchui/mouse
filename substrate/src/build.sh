#!/bin/bash

#            --------------------------------------------------
#                              Mouse Substrate               
#            --------------------------------------------------
#                  Copyright (C) <2019>  <Entynetproject>
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

         rm -rf .cydia-package
 	 # directory stucture
         mkdir .cydia-package
 	 mkdir .cydia-package/DEBIAN
 	 mkdir .cydia-package/Library
         mkdir .cydia-package/Library/MobileSubstrate
 	 mkdir .cydia-package/Library/MobileSubstrate/DynamicLibraries
 	 # copy files
         cp ../msub.dylib .cydia-package/Library/MobileSubstrate/DynamicLibraries
         cp ../msub.plist .cydia-package/Library/MobileSubstrate/DynamicLibraries
 	 mv .cydia-package/Library/MobileSubstrate/DynamicLibraries/msub.dylib .cydia-package/Library/MobileSubstrate/DynamicLibraries/.msub.dylib
 	 mv .cydia-package/Library/MobileSubstrate/DynamicLibraries/msub.plist .cydia-package/Library/MobileSubstrate/DynamicLibraries/.msub.plist
 	 # control file
         cat control >> .cydia-package/DEBIAN/control
         # building
         dpkg -b .cydia-package msub.deb
