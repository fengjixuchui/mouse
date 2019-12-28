# Mouse Payload Loader (MPL)

                                      _     __,..---""-._                 ';-,
                               ,    _/_),-"`             '-.                `\\
                              \|.-"`    -_)                 '.                ||
                              /`   a   ,                      \              .'/
                              '.___,__/                 .-'    \_        _.-'.'
                                 |\  \      \         /`        _`------`_.-'
                                    _/;--._, >        |   --.__/ `------`
                                  (((-'  __//`'-......-;\      )
                                       (((-'       __//  '--. /   mouse/MPL
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

![mouse](https://user-images.githubusercontent.com/54115104/70463102-4109ca80-1acd-11ea-9dc4-e5e6ff8123eb.png)

***

# About Mouse (MPL)

    INFO: Mouse Payload Loader (MPL) is an iOS and macOS post exploitation surveillance 
    tool that gives you a command line session with extra functionality between you and 
    a target machine with simple MPL payload. MPL gives you the power and convenience of 
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

# Building payloads (macOS/iOS)

![payloads](https://user-images.githubusercontent.com/54115104/68298895-8f314580-00ab-11ea-8943-a3f237291427.png)

    INFO: MPL payloads are executed on the target machine. The payload first sends over 
    instructions for getting and sending back device details to our server and then chooses 
    the appropriate executable to establish a secure remote control session.

## Bourne-Again Shell payload

    INFO: Selecting Bourne-Again Shell payload from the payload 
    menu will give us a 1 liner that establishes a remote MPL 
    session upon execution on the target machine.

    Platform: iOS/macOS

## Teensy macOS payload (USB injection)

    INFO: Teensy is a development USB board that can be programmed 
    with the Arduino IDE. It emulates usb keyboard strokes extremely 
    fast and can inject the MPL payload just in a few seconds!

    Platform: macOS
    
## Rubber Duck payload (USB injection)

    INFO: USB Rubber Duck is a development USB board that can inject 
    uploaded to duck SD card inject.bin payload in a few seconds!

    Platform: macOS
    
## Application macOS payload

    INFO: Selecting Application macOS from the payload menu will give 
    us standart MPL payload that converted to the macOS application.
    
    Platform: macOS

***

# Mouse CLI

![mcli](https://user-images.githubusercontent.com/54115104/66684993-f95cf300-ec83-11e9-8b65-f51568fa8e82.png)

    INFO: After a session is established, we can execute commands on that device 
    through the Mouse (MPL) CLI. We can show all available commands by typing "help".
    
## Taking pictures

    INFO: Both iOS and macOS payloads have picture taking capability. 
    The picture command lets you take a picture from the iSight on 
    macOS as well as the front or back camera on iOS.
    
## Tab completion

    INFO: Similar to most command line interfaces, MPL supports 
    tab completion. When you start typing the path to a directory or 
    filename, we can complete the rest of the path using the tab key.

***

# MultiHandler CLI

![multihandler](https://user-images.githubusercontent.com/54115104/66684989-f82bc600-ec83-11e9-922b-dc784c6af241.png)

    INFO: The Multihandler option lets us handler multiple 
    sessions. We can choose to interact with different devices 
    while listening for new connections in the background.
    
***

# Mouse Substrate (MPL Substrate)

    INFO: Mouse Substrate (MPL Substrate) is a package that 
    can be installed on the target iOS device after receiving 
    remote control to run substrate commands and services.
    
## Substrate commands

    dhome          : Simulate a double home button press.
    home           : Simulate a home button press.
    locat          : Toggle location services.
    mute           : Update and view mute status.
    
***

# MPL commands

![help](https://user-images.githubusercontent.com/54115104/66684997-f9f58980-ec83-11e9-8557-2a710c15b805.png)

    INFO: MPL commands are commands that allow you to control a remote device via 
    Mouse CLI or via MultiHandler CLI. Each operating system of the remote device has 
    its own set of MPL commands. You can explore supported operating systems bellow.
    
## Local commands

![exec](https://user-images.githubusercontent.com/54115104/66684992-f8c45c80-ec83-11e9-8dcd-8063112bd4c9.png)

    clear          : Clear terminal input/output.
    help           : Show all available commands.
    exec           : Execute local shell commands.
    exit           : Close current session and exit.

## System commands

![mount](https://user-images.githubusercontent.com/54115104/66684994-f95cf300-ec83-11e9-87c6-12cbeb5d01e0.png)

### macOS

    cat            : Concatenate and print files.
    cd             : Change current directory.
    chflags        : Change flags on file.
    chgrp          : Change files groups.
    chmod          : Change permissions.
    cp             : Copy files or directories.
    date           : Display current date.
    du             : Display disk usage statistics.
    echo           : Write arguments to standard output.
    hash           : Display last executed commands.
    head           : Display first new lines of file.
    kill           : Terminate or signal a process.
    killall        : Kill process by name.
    ln             : Create softlink on oldname.  
    ls             : List contents of a directory.
    mkdir          : Create directories.
    more           : Read contents of a file.
    mount          : Mount file systems.
    mv             : Move files or directories.
    netstat        : Show network status.
    ps             : Show process status.
    pwd            : Show current directory.
    read           : Read user input.
    rm             : Remove files or directories.
    rmdir          : Remove directories.
    sudo           : Execute command as root.
    ssh            : OpenSSH SSH client.
    syscmds        : Display all system commands.
    time           : Display current time.
    touch          : Create files.
    trap           : Configure signals.
    w              : List terminal sessions.
    
### iOS

    cat            : Concatenate and print files.
    cd             : Change current directory.
    chflags        : Change flags on file.
    chgrp          : Change files groups.
    chmod          : Change permissions.
    cp             : Copy files or directories.
    date           : Display current date.
    du             : Display disk usage statistics.
    echo           : Write arguments to standard output.
    hash           : Display last executed commands.
    head           : Display first new lines of file.
    kill           : Terminate or signal a process.
    killall        : Kill process by name.
    ln             : Create softlink on oldname.  
    ls             : List contents of a directory.
    mkdir          : Create directories.
    more           : Read contents of a file.
    mount          : Mount file systems.
    mv             : Move files or directories.
    netstat        : Show network status.
    ps             : Show process status.
    pwd            : Show current directory.
    read           : Read user input.
    rm             : Remove files or directories.
    rmdir          : Remove directories.
    sudo           : Execute command as root.
    ssh            : OpenSSH SSH client.
    syscmds        : Display all system commands.
    time           : Display current time.
    touch          : Create files.
    trap           : Configure signals.
    w              : List terminal sessions.
    
## Settings commands

![getvol](https://user-images.githubusercontent.com/54115104/66684990-f8c45c80-ec83-11e9-9df8-b3120b57db8a.png)

### macOS

    getpaste       : Get pasteboard contents.
    getvol         : Get speaker output volume.
    idletime       : Get the amount of user activity time.
    setbright      : Set screen brightness.
    setvol         : Set output volume.

### iOS

    battery        : Get battery level.
    getvol         : Get volume level.
    msub           : Install or uninstall MPL Substrate.
    setvol         : Set output volume.
    sysinfo        : Show system information.
    
## Substrate commands

### iOS

    dhome          : Simulate a double home button press.
    home           : Simulate a home button press.
    locat          : Toggle location services.
    mute           : Update and show mute status.

## Development commands

![python](https://user-images.githubusercontent.com/54115104/66685000-f9f58980-ec83-11e9-8a33-38757905e952.png)

### macOS

    clang          : The Clang compiler.
    make           : GNU make utility.
    osascript      : Execute OSA scripts.
    python         : The Python compiler.
    
### iOS

    clang          : The Clang compiler.
    make           : GNU make utility.
    python         : The Python compiler.

## Trolling commands

![alert](https://user-images.githubusercontent.com/54115104/66685678-dd5a5100-ec85-11e9-9729-f6810bcaf27f.png)

### macOS

    alert          : Make alert show up on device.
    chwall         : Change desktop wallpaper.
    close          : Close application.
    imessage       : Send message through the messages app.
    itunes         : Control iTunes player.
    keyboard       : Control keyboard.
    kill           : Terminate or signal a process.
    killall        : Kill process by name.
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

![screenshot](https://user-images.githubusercontent.com/54115104/66701587-58fbe280-ed06-11e9-9c2f-6714023dcaba.png)

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
    shutdown       : Shutdown device.
    sleep          : Put device into sleep mode.
    suspend        : Suspend current session.
    
### iOS

    reboot         : Reboot device.
    respring       : Restart SpringBoard.
    safemode       : Put device into SafeMode.
    shutdown       : Shutdown device.

## Other commands

![su](https://user-images.githubusercontent.com/54115104/66701093-fb18cc00-ed00-11e9-8603-7eb62a3638f4.png)

### macOS

    icons          : List system alert icons.
    pid            : Get MPL process ID.
    su             : Login as root.
    upload         : Upload local file.

### iOS

    bundleids      : List bundle identifiers.
    islocked       : Check if the device is locked.
    pid            : Get MPL process ID.
    upload         : Upload local file.

***

# Mouse (MPL) disclaimer

    INFO: Usage of the Mouse Payload Loader for attacking targets without prior mutual consent is illegal. 
    It is the end user's responsibility to obey all applicable local, state, federal, and international laws. 
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.

***

# Mouse (MPL) license
 
        --------------------------------------------------
                       Mouse Payload Loader          
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

***

# Thats all!
