import os
import configparser

home = os.path.expanduser('~')
path_to_config = home + "/.config/PyBye/pybye.conf"
config = configparser.ConfigParser()

# Configuration to write to the configfile
config.add_section("Commands") 
config.set("Commands", "shutdown_command", "shutdown now")
config.set("Commands", "reboot_command", "reboot")
config.set("Commands", "locks_creen_command", "slock")
config.set("Commands", "suspend_command", "systemctl suspend && slock")
config.set("Commands", "logout_command", "pkill -u $USER")

config.add_section("Icons")
config.set("Icons", "shutdown_icon", "system-shutdown-symbolic")
config.set("Icons", "reboot_icon", "system-reboot-symbolic")
config.set("Icons", "lockscreen_icon", "system-lock-screen-symbolic")
config.set("Icons", "suspend_icon", "sleep-symbolic")
config.set("Icons", "logout_icon", "system-log-out-symbolic")
config.set("Icons", "menu_icon", "menu-symbolic")

config.add_section("Size")
config.set("Size", "Height", "150")
config.set("Size", "Width", "800")
config.set("Size", "border_width", "10")
config.set("Size", "icon_size", "6")

config.add_section("Options")
config.set("Options", "ask_for_confirmation", "True")

# Create folder for config file if it does not exist yet
if not os.path.exists(home + "/.config/PyBye/"):
    os.mkdir(home + "/.config/PyBye/")

# Write configuration to the file if the file does not exist yet
if not os.path.exists(path_to_config):
    with open(path_to_config, 'w') as conf:
        config.write(conf)

config.read(path_to_config)

# Variables for icons
shutdown_icon = config["Icons"]["shutdown_icon"]
reboot_icon = config["Icons"]["reboot_icon"]
lockscreen_icon = config["Icons"]["lockscreen_icon"]
suspend_icon = config["Icons"]["suspend_icon"]
logout_icon = config["Icons"]["logout_icon"]
menu_icon = config["Icons"]["menu_icon"]

# Variables for commands
shutdown_command = config["Commands"]["shutdown_command"]
reboot_command = config["Commands"]["reboot_command"]
lockscreen_command = config["Commands"]["locks_creen_command"]
suspend_command = config["Commands"]["suspend_command"]
logout_command = config["Commands"]["logout_command"]

# Variables for size
width = int(config["Size"]["Width"])
height = int(config["Size"]["Height"])
border_width = int(config["Size"]["Border_width"])
icon_size = int(config["Size"]["icon_size"])

# Variables for options
confirmation = config["Options"]["ask_for_confirmation"].lower()
