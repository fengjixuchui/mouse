#!/bin/bash

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

#blue start 
	BS="\033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[1;31m"
#green start
	GNS="\033[1;32m"
#white start
        WHS="\033[0m"
        
if [[ -d /data/data/com.termux ]]
then
if [[ -f /data/data/com.termux/files/usr/bin/mouse ]]
then
UPD="true"
else
UPD="false"
fi
else
if [[ -f /usr/local/bin/mouse ]]
then
UPD="true"
else
UPD="false"
fi
fi
{
ASESR="$( curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//' )"
} &> /dev/null
if [[ "$ASESR" = "" ]]
then 
sleep 1
echo -e ""$RS"[-] "$WHS"Download failed!"$CE""
sleep 1
exit
fi
if [[ $EUID -ne 0 ]]
then
sleep 1
echo -e ""$RS"[-] "$WHS"Permission denied!"$CE""
sleep 1
exit
fi
sleep 1
echo -e ""$BS"[*] "$WHS"Installing update..."$CE""
{
rm -rf ~/mouse
rm /bin/mouse
rm /usr/local/bin/mouse
rm /data/data/com.termux/files/usr/bin/mouse
cd ~
git clone https://github.com/entynetproject/mouse.git
if [[ "$UPD" != "true" ]]
then
sleep 0
else
cd ~/mouse
chmod +x install.sh
./install.sh
fi
} &> /dev/null
echo -e ""$GNS"[+] "$WHS"Successfully updated!"$CE""
cd .
touch .updated
sleep 1
exit
