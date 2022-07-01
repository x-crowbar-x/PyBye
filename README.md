# PyBye
Logout program for Linux desktop.

## What you need to know
 
PyBye is written with Python and GTK3. It is basically just one script, that has some basic functionality. 

### The program has:
- Configuration file. You can change the commands, size of the window, icons.
- Keyboard shortcuts. They are there in case you want to quickly log-out without confirmation.

The config file is located in `~/.config/PyBye/pybye.conf`. 

Standart keyboard shortcuts are:
- Alt + 1: Shutdown
- Alt + 2: Reboot
- Alt + 3: Suspend
- Alt + 4: Lock screen
- Alt + 5: Log-out

## Miscellaneous
* The shutdown, reboot, suspend, log-out commands are standart SystemD commands, but to lock screen I use `slock`. You can easily change it in the config file.
* The icons are theme-dependent. In order to change the default ones, you need to specify exact the name (without file extention) of the icon of your currently installed GTK3 theme. 
* Haven't tested it on Wayland yet. Ran it only on my Qtile with X11.

## Installation

### Prerequisites
- Python 3.10
- GTK 3.0
