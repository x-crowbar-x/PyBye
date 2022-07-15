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

- Set any text for the buttons, which makes it possible to change the position of any button. For example, to put suspend on the first place you need to switch the commands of the first and the third buttons, icons and their texts.
- Change commands and icons.
- Specify the border width.
- Change the size of the main window. <b>BUT, after the latest update it is now 1920x1080, no matter what values below that you put inside the config, unless you also change the value of `border_width`. The same same applies to greater resolutions.</b>
- Disable confirmation.
- Enable shortcuts (don't even know if anyone would need them at all, but they are `Alt`+(from `1` to `5`)). 
- Enable the cancel button. (Also don't know if anyone would need it, because I set Escape button to close the window.)
- Specify how much space between buttons and text you would like to have.
- And also specify the spacing between the buttons.

<b>The config file is located in `~/.config/PyBye/pybye.conf`.</b>

****

## Additional Info
* The shutdown, reboot, suspend commands are standart SystemD commands, but to lock screen I use `light-locker` (locker for `lightdm`). You can easily change it in the config file.
* The icons are <b>theme-dependent</b>. In order to change the default ones, you need to specify the exact name (without the file extention) of the icon of the currently installed GTK3 theme. The maximum size of default icons is 6. After changing the icons and their size, that is bigger than 6, run the script in the command line to see if there are any errors related to the icons.
* The transparency effect is achieved through the use of a compositor. I use the `picom` compositor. If you have no idea how to configure `picom`, here is my [picom config](https://github.com/x-crowbar-x/Dotfiles/tree/main/picom). Install `picom` and put this file inside `~/.config/picom/` directory. Then make this command `picom --experimental-backends &` (with or without `--experimental-backends`) to run after logging in.
* If the resolution of the screen is correct in the config and for some reason the window is not fullscreen, try to uncomment `win.fullscreen()` (remove the `#`) on line 208 and comment out the next line `win.move(-1, -5)` and run PyBye again.

****

## Installation

### Prerequisites
- Python
- GTK 3.0

It is basically a script, so it is possible to just run it as it is. Just put it somewhere in the `$PATH`. 
<p>I've never dealt with Makefile files, so I don't know how to write an installation script. I will see what I can do with it.</p>

*****

I took the inspiration from [DistroTube](https://www.youtube.com/c/DistroTube "Derek Taylor's chanel"), who built a similar [project](https://gitlab.com/dwt1/byebye "ByeBye on GitLab"), which is called ByeBye (hence the name "PyBye") but in Haskell. I've also found another repository on GitHub with the same name as this one. I made it up myself and did not steal it! It's just a coinsidence. :)

*****