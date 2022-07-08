# PyBye
Log-out program for Linux desktop.
****
![Screenshot](/Screenshot/PyBye-window.png "App. window")
****
## What you need to know

PyBye is a simple little log-out program with the help of which, it is more aesthetically pleasing (for me anyway) to end the current session, lock screen or suspend.

### Features

The program has a configuration file to change it to your liking.

<b><p>You can:</p></b>

- Change commands and icons.
- Disable icons.
- Change the size of the dialog and the main window.
- Specify the border width and spacing (space between buttons).
- Disable the dialog window.
- Change orientation of the window (horizontal or vertical).
- Disable shortcuts (don't even know if anyone would need them at all).
- Set the position of the window to either `center` or `mouse`.
- Disable the cancel button.

<b>The config file is located in `~/.config/PyBye/pybye.conf`.</b>

****

## Additional Info
* The shutdown, reboot, suspend commands are standart SystemD commands, but to lock screen I use `slock`. You can easily change it in the config file.
* The icons are theme-dependent. In order to change the default ones, you need to specify the exact name (without the file extention) of the icon of the currently installed GTK3 theme. The maximum size of default icons is 6. After changing the icons and their size, that is bigger than 6, run the script in the command line to see if there are any errors related to the icons.
* The position of the buttons is hard-coded. You can change it in the main file by moving the blocks of code for the buttons up or down.
* Escape button closes the main window. If the dialog is open, then, obviously, it will be closed, but not the main window.
* It is better to use a Nerd font, so that the icons on the dialog window are shown correctly (I have no idea how to make it use the default icons on dialog buttons).
* To use new options in the config (if you had older version and then downloaded a new one), delete or change the name of the config and run the script again to regenerate it (It is like that only for now).

****

## Installation

### Prerequisites
- Python
- GTK 3.0

It is basically a script, so it is possible to just run it as it is. Just put it somewhere in the `$PATH`. 
<p>I've never dealt with Makefile files, so I don't know how to write an installation script. I will see what I can do with it.</p>

*****

I took the inspiration from [DistroTube](https://www.youtube.com/c/DistroTube "Derek Taylor's chanel"), who built a similar [project](https://gitlab.com/dwt1/byebye "ByeBye on GitLab"), which is called ByeBye (hence the name "PyBye") but in Haskell. I've also found another repository on GitHub with the same name as this one. I made it up myself and did not steal it! It's just a coinsidence. :)

<p>If you have any suggestions or questions, send me an E-mail to pennyvoidtea@gmail.com </p>

*****