import os
import configparser

home = os.path.expanduser('~')
path_to_config = home + "/.config/PyBye/pybye.conf"
config = configparser.ConfigParser()

# Configuration to write to the configfile
config.add_section("Commands") 
config.set("Commands", "button_one_command", "shutdown now")
config.set("Commands", "button_two_command", "reboot")
config.set("Commands", "button_three_command", "systemctl suspend && slock")
config.set("Commands", "button_four_command", "slock")
config.set("Commands", "button_five_command", "pkill -u $USER")

config.add_section("Icons")
config.set("Icons", "button_one_icon", "system-shutdown-symbolic")
config.set("Icons", "button_two_icon", "system-reboot-symbolic")
config.set("Icons", "button_three_icon", "sleep-symbolic")
config.set("Icons", "button_four_icon", "system-lock-screen-symbolic")
config.set("Icons", "button_five_icon", "system-log-out-symbolic")
config.set("Icons", "cancel_icon", "cancel")

config.add_section("Size")
config.set("Size", "Height", "150")
config.set("Size", "Width", "800")
config.set("Size", "border_width", "10")
config.set("Size", "icon_size", "6")
config.set("Size", "dialog_height", "100")
config.set("Size", "dialog_width", "100")
config.set("Size", "Spacing", "5")

config.add_section("Options")
config.set("Options", "ask_for_confirmation", "True")
config.set("Options", "enable_icons", "True")
config.set("Options", "Orientation", "horizontal")
config.set("Options", "enable_shortcuts", "True")
config.set("Options", "window_position", "center")
config.set("Options", "enable_cancel", "True")

config.add_section("Text")
config.set("Text", "button_one", "Shutdown")
config.set("Text", "button_two", "Reboot")
config.set("Text", "button_three", "Suspend")
config.set("Text", "button_four", "Lock Screen")
config.set("Text", "button_five", "Log Out")

# Create folder for config file if it does not exist yet
if not os.path.exists(home + "/.config/PyBye/"):
    os.mkdir(home + "/.config/PyBye/")

# Write configuration to the file if the file does not exist yet
if not os.path.exists(path_to_config):
    with open(path_to_config, 'w') as conf:
        config.write(conf)

config.read(path_to_config)

# Variables for icons
button_one_icon = config["Icons"]["button_one_icon"]
button_two_icon = config["Icons"]["button_two_icon"]
button_three_icon = config["Icons"]["button_three_icon"]
button_four_icon = config["Icons"]["button_four_icon"]
button_five_icon = config["Icons"]["button_five_icon"]
cancel_icon = config["Icons"]["cancel_icon"]

# Variables for commands
button_one_command = config["Commands"]["button_one_command"]
button_two_command = config["Commands"]["button_two_command"]
button_three_command = config["Commands"]["button_three_command"]
button_four_command = config["Commands"]["button_four_command"]
button_five_command = config["Commands"]["button_five_command"]

# Variables for size
width = int(config["Size"]["Width"])
height = int(config["Size"]["Height"])
border_width = int(config["Size"]["Border_width"])
dialog_height = int(config["Size"]["dialog_height"])
dialog_width = int(config["Size"]["dialog_width"])
icon_size = int(config["Size"]["icon_size"])
space = int(config["Size"]["Spacing"])

# Variables for options
confirmation = config["Options"]["ask_for_confirmation"].capitalize()
enable_icons = config["Options"]["enable_icons"].capitalize()
orientation = config["Options"]["Orientation"].lower()
enable_shortcuts = config["Options"]["enable_shortcuts"].capitalize()
window_position = config["Options"]["window_position"].lower()
enable_cancel = config["Options"]["enable_cancel"].lower()

# Variables for tooltip  
button_one = config["Text"]["button_one"]
button_two = config["Text"]["button_two"]
button_three = config["Text"]["button_three"]
button_four = config["Text"]["button_four"]
button_five = config["Text"]["button_five"]
