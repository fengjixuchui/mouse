# Mouse Framework

                                      _     __,..---""-._                 ';-,
                               ,    _/_),-"`             '-.                `\\
                              \|.-"`    -_)                 '.                ||
                              /`   a   ,                      \              .'/
                              '.___,__/                 .-'    \_        _.-'.'
                                 |\  \      \         /`        _`------`_.-'
                                    _/;--._, >        |   --.__/ `------`
                                  (((-'  __//`'-......-;\      )
                                       (((-'       __//  '--. /  
                                                 (((-'    __//
                                                        (((-'

<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a> 
  <a href="https://github.com/entynetproject/mouse/releases">
    <img src="https://img.shields.io/github/release/entynetproject/mouse.svg">
  </a>
  <a href="https://wikipedia.org/wiki/Python_(programming_language)">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/mouse">
    <img src="https://img.shields.io/badge/payloads-macOS/iOS-red.svg">
 </a>
  <a href="https://github.com/entynetproject/mouse/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/mouse.svg">
  </a>
  <a href="https://github.com/entynetproject/mouse/wiki">
      <img src="https://img.shields.io/badge/wiki%20-mouse-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

![mouse](https://user-images.githubusercontent.com/54115104/71723678-d890dd80-2e2d-11ea-8262-818480c40e87.png)

***

# About Mouse Framework

    Mouse Framework is an iOS and macOS post exploitation surveillance framework 
    that gives you a command line session with extra functionality between you and a 
    target machine with simple Mouse payload. Mouse gives you the power and convenience of 
    uploading and downloading files, tab completion, taking pictures, location tracking,
    shell command execution, escalating privileges, password retrieval, and much more.
  
***
    
# Getting started

## Mouse installation

> cd mouse

> chmod +x install.sh

> ./install.sh

## Mouse uninstallation

> cd mouse

> chmod +x uninstall.sh

> ./uninstall.sh

***

# Mouse Framework execution

    To execute Mouse Framework you 
    should execute the following command.

> mouse

***

# Mouse Payloads (macOS/iOS)

![payloads](https://user-images.githubusercontent.com/54115104/71848194-2415e680-30cf-11ea-9dbe-9c0d2d028dd4.png)

    Mouse Payloads are executed on the target machine. The payload first sends over 
    instructions for getting and sending back device details to our server and then chooses 
    the appropriate executable to establish a secure remote control session.

## Bourne-Again Shell payload

    Selecting Bourne-Again Shell payload from the payload 
    menu will give us a 1 liner that establishes a remote 
    Mouse session upon execution on the target machine.

    Platform: iOS/macOS

## Teensy macOS payload (USB injection)

    Teensy is a development USB board that can be programmed 
    with the Arduino IDE. It emulates usb keyboard strokes extremely 
    fast and can inject the Mouse payload just in a few seconds!

    Platform: macOS
    
## Rubber Duck payload (USB injection)

    USB Rubber Duck is a development USB board that can inject 
    uploaded to duck SD card inject.bin payload in a few seconds!

    Platform: macOS
    
## Application macOS payload

    Selecting Application macOS from the payload menu will give you
    standart Mouse payload that converted to the macOS application.
    
    Platform: macOS
    
***

# MultiHandler CLI

![multihandler](https://user-images.githubusercontent.com/54115104/71770527-d4e48000-2f2d-11ea-98ff-f4e6a9b8ce62.png)

    The Multihandler option lets us handler multiple sessions. 
    You can choose to interact with different devices while 
    listening for new connections in the background.
    
## MultiHandler commands

    close          : Close active session.
    exit           : Close all sessions and exit.
    help           : Show all available commands.
    interact       : Interact with a session. 
    sessions       : List active sessions.
    
***

# Mouse Substrate

    Mouse Substrate is a package that can be installed 
    on the target iOS device after receiving remote control 
    to run substrate commands and services.
    
## Substrate commands

    dhome          : Simulate a double home button press.
    home           : Simulate a home button press.
    locat          : Toggle location services.
    mute           : Update and view mute status.
    
***

# Mouse CLI

![help](https://user-images.githubusercontent.com/54115104/71770526-d4e48000-2f2d-11ea-9240-1a1f749c8460.png)

    After a session is established, we can execute commands on that device through 
    the Mouse CLI. We can show all available commands by typing "help". Mouse CLI 
    allows you to control a remote device. Remote device can be controlled by Mouse
    CLI commands. You can explore list of available Mouse CLI commands bellow.

## Local commands

![exec](https://user-images.githubusercontent.com/54115104/71770525-d4e48000-2f2d-11ea-9c63-bdea00f781b7.png)

    clear          : Clear terminal input/output.
    help           : Show all available commands.
    exec           : Execute local shell commands.
    exit           : Close current session and exit.
    
## Settings commands

![setvol](https://user-images.githubusercontent.com/54115104/71770530-d57d1680-2f2d-11ea-9e4b-3d4f5b3007ab.png)

### macOS

    getpaste       : Get pasteboard contents.
    getvol         : Get speaker output volume.
    idletime       : Get the amount of user activity time.
    setbright      : Set screen brightness.
    setvol         : Set output volume.

### iOS

    battery        : Get battery level.
    getvol         : Get volume level.
    msub           : Mouse Substrate.
    setvol         : Set output volume.
    sysinfo        : Show system information.

## Trolling commands

![alert](https://user-images.githubusercontent.com/54115104/71848193-237d5000-30cf-11ea-9f43-ae65ff288a78.png)

### macOS

    alert          : Make alert show up on device.
    chwall         : Change desktop wallpaper.
    close          : Close application.
    imessage       : Send message through the messages app.
    itunes         : Control iTunes player.
    keyboard       : Control keyboard.
    open           : Open application.
    say            : Convert text to speach.
    
### iOS

    alert          : Make alert show up on device.
    dial           : Dial a phone number.
    ipod           : Control music player.
    kill           : Terminate or signal a process.
    killall        : Kill process by name.
    lastapp        : Open last opened application.
    open           : Open application.
    openurl        : Open URL on device.
    say            : Convert text to speach.
    vibrate        : Vibrate device.

## Stealing commands

![screenshot](https://user-images.githubusercontent.com/54115104/71770529-d57d1680-2f2d-11ea-901b-ab9703c0bd0c.png)

### macOS

    download       : Download remote file.
    getfacebook    : Retrieve facebook session cookies.
    mic            : Record mic sound.
    picture        : Take picture through iSight.
    prompt         : Prompt user to type password.
    screenshot     : Take screenshot.
    
### iOS

    download       : Download remote file.
    getcontacts    : Download addressbook.
    getnotes       : Download notes.
    getpasscode    : Retreive the device passcode.
    getsms         : Download SMS data.
    locate         : Get device location coordinates.
    mic            : Record mic sound.
    picture        : Take picture through the camera.
    
## Boot commands

### macOS

    reboot         : Reboot device.
    sleep          : Put device into sleep mode.
    suspend        : Suspend current session.
    
### iOS

    reboot         : Reboot device.
    respring       : Restart SpringBoard.
    safemode       : Put device into SafeMode.

## Other commands

![shell](https://user-images.githubusercontent.com/54115104/71770673-a9fb2b80-2f2f-11ea-974f-99017752960c.png)

### macOS

    icons          : List system alert icons.
    pid            : Get Mouse process ID.
    shell          : Open target device shell.
    su             : Login as root.
    upload         : Upload local file.

### iOS

    bundleids      : List bundle identifiers.
    islocked       : Check if the device is locked.
    pid            : Get Mouse process ID.
    shell          : Open target device shell.
    upload         : Upload local file.

***

# Mouse Framework disclaimer

    Usage of the Mouse Framework for attacking targets without prior mutual consent is illegal. 
    It is the end user's responsibility to obey all applicable local, state, federal, and international laws. 
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.

***

# Mouse Framework license
 
        --------------------------------------------------
                       Mouse Framework          
        --------------------------------------------------
              Copyright (C) <2019>  <Entynetproject>      

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.                
