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

YS="\033[1;33m"
CE="\033[0m"

#blue start 
	BS="\033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[1;31m"
#green start
	GNS="-e \033[1;32m"
#white start
   WHS="\033[0m"
   
printf '\033]2;install.sh\a'

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$RS"[-]"$WHS" This script must be run as root!"$CE"" 1>&2
   sleep 1
   exit
fi

if [[ -d ~/mouse ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/mouse.git
} &> /dev/null
fi

sleep 0.5
clear
sleep 0.5
echo
cd ~/mouse
cat banner/banner.txt
echo

sleep 1
echo -e ""$BS"[*]"$WHS" Installing dependencies..."$CE""
sleep 1

{
pkg update
pkg -y install git
pkg -y install python
pkg -y install openssl
apt-get update
apt-get -y install git
apt-get -y install python
apt-get -y install openssl
apk update
apk add git
apk add python
apk add openssl
pacman -Sy
pacman -S --noconfirm git
pacman -S --noconfirm python
pacman -S --noconfirm openssl
zypper refresh
zypper install -y git
zypper install -y python
zypper install -y openssl
yum -y install git
yum -y install python
yum -y install openssl
dnf -y install git
dnf -y install python
dnf -y install openssl
eopkg update-repo
eopkg -y install git
eopkg -y install python
eopkg -y install openssl
xbps-install -S
xbps-install -y git
xbps-install -y python
xbps-install -y openssl
} &> /dev/null

{
cd ~/mouse/bin
cp mouse /usr/local/bin
chmod +x /usr/local/bin/mouse
cp mouse /bin
chmod +x /bin/mouse
cp mouse /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/mouse
} &> /dev/null

sleep 1
echo -e ""$GNS"[+]"$WHS" Successfully installed!"$CE""
sleep 1
