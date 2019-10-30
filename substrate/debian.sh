#! /bin/bash

# 
#            --------------------------------------------------
#                           Mouse Payload Loader                
#            --------------------------------------------------
#          Copyright (C) <2015>  <Entynetproject (Ivan Nikolsky)>
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
#
#
#    About Author :   
#    Founder   : Entynetproject (Ivan Nikolsky)
#    Site      : http://entynetproject.simplesite.com/
#    Instagram : @entynetproject 
#    Twitter   : @entynetproject
#    Email     : entynetproject@gmail.com
#

if [[ "$1" = "-b" || "$1" = "--build" ]]
then


        rm -rf .cydia-package
	# directory stucture
        mkdir .cydia-package
	mkdir .cydia-package/DEBIAN
	mkdir .cydia-package/Library
        mkdir .cydia-package/Library/MobileSubstrate
	mkdir .cydia-package/Library/MobileSubstrate/DynamicLibraries
	# copy files
        cp mpl.dylib .cydia-package/Library/MobileSubstrate/DynamicLibraries
        cp mpl.plist .cydia-package/Library/MobileSubstrate/DynamicLibraries
	mv .cydia-package/Library/MobileSubstrate/DynamicLibraries/mpl.dylib .cydia-package/Library/MobileSubstrate/DynamicLibraries/.mpl.dylib
	mv .cydia-package/Library/MobileSubstrate/DynamicLibraries/mpl.plist .cydia-package/Library/MobileSubstrate/DynamicLibraries/.mpl.plist
	# control file
        echo "Name: Mouse Substrate" >> .cydia-package/DEBIAN/control
        echo "Package: com.entynetproject.mouse" >> .cydia-package/DEBIAN/control
        echo "Version: 0.0.1" >> .cydia-package/DEBIAN/control
        echo "Description: Mouse Substrate (MPL Substrate)" >> .cydia-package/DEBIAN/control
        echo "Architecture: iphoneos-arm" >> .cydia-package/DEBIAN/control
        echo "Author: Entynetproject" >> .cydia-package/DEBIAN/control
        echo "Maintainer: Entynetproject" >> .cydia-package/DEBIAN/control
        echo "Depends: mobilesubstrate" >> .cydia-package/DEBIAN/control
        #postinst
        echo "#!/bin/bash" >> .cydia-package/DEBIAN/postinst
        echo "ldid -S /usr/bin/python" >> .cydia-package/DEBIAN/postinst
        chmod +x .cydia-package/DEBIAN/postinst
        dpkg -b .cydia-package mouse-substrate.deb
	fi
