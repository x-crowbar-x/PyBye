# PyBye
Logout program for Linux desktop.
****
![Screenshot](/Screenshot/PyBye-window.png "App. window")
****
## What you need to know

PyBye is a simple little log-out program with the help of which, it is more aesthetically pleasing (for me anyway) to end current session, lock screen or suspend.

### The program has:

- Configuration file. You can change the commands, size of the window and the icons, as well as icons themselves.
- Keyboard shortcuts. They are there in case you want to quickly log out without confirmation. Or simply set `ask_for_confirmation` to `false` (case-insensitive) in the config file.

The config file is located in `~/.config/PyBye/pybye.conf`. 

Standart keyboard shortcuts are:
- Alt + 1 to 5

****

## Additional Info
* The shutdown, reboot, suspend commands are standart SystemD commands, but to lock screen I use `slock`. You can easily change it in the config file.
* The icons are theme-dependent. In order to change the default ones, you need to specify exact the name (without file extention) of the icon of your currently installed GTK3 theme. The maximum size of default icons is 6. After changing the icons and their size, that is bigger than 6, run the script in the command line to see if there are any errors related to the icons.
* Haven't tested it on Wayland yet. Ran it only on my Qtile with X11.
* The position of the buttons is hard-coded for now. Maybe I'll work on it later.
* Escape button closes the main window and dialogs.

****

## Installation

### Prerequisites
- Python
- GTK 3.0

It is basically a script, so it is possible to just run it as it is. Just put it somewhere in the `$PATH`. 
<p>I've never dealt with Makefile files, so I have no idea how to write an installation script. I will see what I can do with it.</p>

*****

I took the inspiration from [DistroTube](https://www.youtube.com/c/DistroTube "Derek Taylor's chanel"), who built a similar [project](https://gitlab.com/dwt1/byebye "ByeBye on GitLab"), which is called ByeBye (hence the name "PyBye") but in Haskell.

<p>If you have any suggestions or questions, send me an E-mail to pennyvoidtea@gmail.com </p>

*****