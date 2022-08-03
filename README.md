# PyBye
Log-out program for Linux desktop.
****
![Screenshot](/Screenshot/PyBye-window.png "Main window")

****
## What you need to know

PyBye is a simple little log-out program with the help of which, it is more aesthetically pleasing (for me anyway) to end the current session, lock screen or suspend. And of course this program is mostly for those who use window managers, for obvious reasons. Also, I've customized it for my system and idk how to put appearance settings inside the config... So, for now users can only change the values inside the `style.css` file.

### Features

The program has a configuration file to change it to your liking. 
<b>IMPORTANT!</b> To use new options in the config (if you had an older version and then downloaded a new one), delete or change the name of the config and run the script again to regenerate it.

<b><p>You can:</p></b>

- Change commands and icons.
- Set any text for the buttons, which makes it possible to change the position of any button. For example, to put suspend on the first place you need to switch the commands of the first and the third buttons, icons and their texts.
- Specify the border width.
- Change the size of the main window. <b>BUT, after the latest update it is always fullscreen, no matter what values for the resolution you set in the config, unless you also change the values of `border_width` and `fullscreen_mode`.</b>
- Disable confirmation dialog.
- Enable shortcuts (don't even know if anyone would need them at all, but they are `Alt`+(from `1` to `5`)). 
- Enable the cancel button. (Also don't know if anyone would need it, because I set Escape button to close the dialog and the main window.)
- Specify how much space between buttons and text you would like to have.
- And also specify the spacing between the buttons.
- Disable fullscreen mode.

<b>The config file is located in `~/.config/PyBye/pybye.conf`.</b>

****

## Additional Info
* The shutdown, reboot, suspend and log-out commands are standart Systemd commands, but the command to lock screen you'll need to check what is used in your desktop environment or window manager (sometimes there is none and you will have to manually install something like `light-locker` or `slock`).
* The icons are <b>theme-dependent</b>. In order to change the default ones, you need to specify the exact name (without the file extention) of the icon of the currently installed GTK3 theme. The maximum size of default icons is 6. After changing the icons and their size, that is larger than 6, run the script in the command line to see if there are any errors related to the icons.
* The transparency effect is achieved through the use of a compositor. I use the `picom` compositor. Install `picom` and then make this command `picom --experimental-backends &` (with or without `--experimental-backends`) to run after logging in.
* If the confirmation dialog window appears under the main one for some reason, set the option `Fullscreen` inside the config to `False` and try again.

****

## Installation

### Prerequisites
- Python 3
- GTK 3.0 (install `python3-gobject` package)

It is basically a script, so it is possible to just run it as it is. Just put the files in a separate directory somewhere in the `$PATH`.
<p>I've never dealt with python installation scripts, so I don't know how to do it. I will see what I can do.</p>

*****

I took the inspiration from [DistroTube](https://www.youtube.com/c/DistroTube "Derek Taylor's chanel"), who built a similar [project](https://gitlab.com/dwt1/byebye "ByeBye on GitLab"), which is called ByeBye (hence the name "PyBye") but in Haskell. I've also found another repository on GitHub with the same name as this one. I made it up myself and did not steal it! It's just a coinsidence. :)

*****