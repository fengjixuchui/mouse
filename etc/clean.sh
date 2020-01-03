#!/bin/bash

#            --------------------------------------------------
#                              Mouse Framework                                 
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

#blue start 
	BS="\033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[1;31m"
#green start
	GNS="-e \033[1;32m"
#white start
        WHS="\033[0;97m"

if [[ "$1" = "-h" || "$1" = "--help" ]]
then
echo -e "Usage: clean.sh [OPTION...]"
echo -e "Copyright (C) 2019, Entynetproject. All Rights Reserved."
echo -e
echo -e "   -d  --downloads  Clean up downloads."
echo -e "   -p  --payloads   Clean up payloads."
echo -e "   -h  --help       Give this help list."
exit

elif [[ "$1" = "-d" || "$1" = "--downloads" ]]
then
{
cd ~/mouse
rm -rf downloads
mkdir downloads
} &> /dev/null
sleep 1
echo -e ""$BS"[*]"$WHS" Cleaning up..."$CE""
sleep 10
exit

elif [[ "$1" = "-p" || "$1" = "--payloads" ]]
then
{
cd ~/mouse
rm -rf payloads
mkdir payloads
} &> /dev/null
sleep 1
echo -e ""$BS"[*]"$WHS" Cleaning up..."$CE""
sleep 10
exit
fi

echo -e "Usage: clean.sh [OPTION...]"
echo -e "Copyright (C) 2019, Entynetproject. All Rights Reserved."
echo -e
echo -e "   -d  --downloads  Clean up downloads."
echo -e "   -p  --payloads   Clean up payloads."
echo -e "   -h  --help       Give this help list."
exit
