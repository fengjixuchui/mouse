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

***

# About mouse (MPL)

![mouse](https://user-images.githubusercontent.com/54115104/66684988-f82bc600-ec83-11e9-8f59-f16a729dc693.png)

    INFO: Mouse Payload Loader (MPL) is a post exploitation surveillance tool written 
    in Python, C and Objective-C. It gives you a command line session with extra functionality 
    between you and a target machine with simple MPL payload. MPL gives you the power and convenience 
    of uploading/downloading files, tab completion, taking pictures, location tracking, shell command 
    execution, persistence, escalating privileges, password retrieval, and much more.
  
***
    
# Getting started

## mouse (MPL) installation

> cd mouse

> chmod +x install.sh

> ./install.sh

## mouse (MPL) uninstallation

> cd mouse

> chmod +x uninstall.sh

> ./uninstall.sh

***

# Building payloads (macOS/iOS)

![payloads](https://user-images.githubusercontent.com/54115104/66684991-f8c45c80-ec83-11e9-9788-265573a79d90.png)

    INFO: MPL payloads are executed on the target machine. The payload first sends over 
    instructions for getting and sending back device details to our server and then chooses 
    the appropriate executable to establish a secure remote control session.

## Bourne-Again Shell payload

    INFO: Selecting bash from the payload menu will give us a 1 liner that 
    establishes a remote MPL session upon execution on the target machine.
    
## Entynet PI payload (USB injection)

    INFO: Entynet PI is a development board that can be programmed 
    with the Arduino IDE. It emulates USB keyboard strokes extremely 
    fast and can inject the MPL payload just in a few seconds.

## Rubber Duck payload (USB injection)

    INFO: USB Rubber Duck is a development USB board that can inject 
    uploaded to duck SD card inject.bin payload in a few seconds!
    
## MacOS Application payload

    INFO: This is a standart Mouse (MPL) Payload 
    that converted to the MacOS Application.
    
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

    INFO: Mouse Substrate (MPL Substrate) is a package that will 
    be installed on the victim's iOS device after receiving remote 
    control. Mouse Substrate allows you to run substrate commands 
    and services on the victim’s remote iOS device.
    
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
    location       : Toggle location services.
    mute           : Update and view mute status.
    setvol         : Set output volume.
    sysinfo        : View system information.
    
## Substrate commands

### iOS

    dhome          : Simulate a double home button press.
    home           : Simulate a home button press.

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
    keyboard       : Control target's keyboard.
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

![screenshot](https://user-images.githubusercontent.com/54115104/66684999-f9f58980-ec83-11e9-8a69-3ea9d17553f6.png)

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

![su](https://user-images.githubusercontent.com/54115104/66684995-f95cf300-ec83-11e9-8170-8bb1dfed471f.png)

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

# Terms of use

    This tool is only for educational purposes only.
    Use this tool wisely and never without permission.
    I am not responsible for anything you do with this tool.

***

# Mouse (MPL) license
 
        --------------------------------------------------
                       Mouse Payload Loader          
        --------------------------------------------------
      Copyright (C) <2015>  <Entynetproject (Ivan Nikolsky)>

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
