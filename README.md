# PyBye
Log-out program for Linux desktop.
****
![Screenshot](/Screenshot/PyBye-window.png "Main window")
****
## What you need to know

PyBye is a simple little log-out program with the help of which, it is more aesthetically pleasing (for me anyway) to end the current session, lock screen or suspend.

### Features

The program has a configuration file to change it to your liking. 
<b>IMPORTANT!</b> To use new options in the config (if you had an older version and then downloaded a new one), delete or change the name of the config and run the script again to regenerate it.

<b><p>You can:</p></b>

- Set any tooltip/dialog button text, which allows you to change the position of any button. For example, to put suspend on the first place you need to switch the commands of the first and the third buttons, icons and their texts.
- Change commands and icons.
- Disable icons (only the text will be shown).
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
* The icons are <b>theme-dependent</b>. In order to change the default ones, you need to specify the exact name (without the file extention) of the icon of the currently installed GTK3 theme. The maximum size of default icons is 6. After changing the icons and their size, that is bigger than 6, run the script in the command line to see if there are any errors related to the icons.
* Escape button closes the main window. If the dialog is open, then, obviously, it will be closed, but not the main window.

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