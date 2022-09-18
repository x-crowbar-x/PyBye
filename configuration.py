import os
import configparser

home = os.path.expanduser('~')
path_to_config = home + "/.config/PyBye/pybye.conf"
config = configparser.ConfigParser()

# Configuration to write to the configfile
config.add_section("Commands") 
config.set("Commands", "button_one_command", "shutdown now")
config.set("Commands", "button_two_command", "reboot")
config.set("Commands", \
           "button_three_command", 
           "systemctl suspend && light-locker-command -l")
config.set("Commands", \
           "button_four_command", \
           "light-locker-command -l")
config.set("Commands", \
           "button_five_command", \
           "loginctl terminate-session ${XDG_SESSION_ID-}")

config.add_section("Icons")
config.set("Icons", "button_one_icon", "system-shutdown-symbolic")
config.set("Icons", "button_two_icon", "system-reboot-symbolic")
config.set("Icons", "button_three_icon", "system-suspend-symbolic")
config.set("Icons", "button_four_icon", "system-lock-screen-symbolic")
config.set("Icons", "button_five_icon", "system-log-out-symbolic")
config.set("Icons", "cancel_icon", "stock_calc-cancel")

config.add_section("Size")
config.set("Size", "Width", "1920")
config.set("Size", "Height", "1080")
config.set("Size", "border_width", "500")
config.set("Size", "icon_size", "6")

config.add_section("Options")
config.set("Options", "ask_for_confirmation", "True")
config.set("Options", "enable_shortcuts", "True")
config.set("Options", "enable_cancel", "False")
config.set("Options", "space_between_buttons_and_text", "15")
config.set("Options", "space_between_buttons", "80")
config.set("Options", "fullscreen_mode", "True")

config.add_section("Text")
config.set("Text", "button_one", "Shutdown")
config.set("Text", "button_two", "Reboot")
config.set("Text", "button_three", "Suspend")
config.set("Text", "button_four", "Lock screen")
config.set("Text", "button_five", "Log-Out")

config.add_section("Colors")
config.set("Colors", "background_color", "rgba(40,40,40, 0.6)")
config.set("Colors", "button_background", "rgba(40,40,40, 0.1)")
config.set("Colors", "button_hover", "rgba(235, 219, 178, 0.461)")
config.set("Colors", "button_shadow", "antiquewhite")
config.set("Colors", "button_activate", "antiquewhite")
config.set("Colors", "text_color", "#ebdbb2")
config.set("Colors", "text_shadow", "#3c3836")

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
icon_size = int(config["Size"]["icon_size"])

# Variables for options
confirmation = config["Options"]["ask_for_confirmation"].capitalize()
enable_shortcuts = config["Options"]["enable_shortcuts"].capitalize()
enable_cancel = config["Options"]["enable_cancel"].capitalize()
row_spacing = int(config["Options"]["space_between_buttons_and_text"])
column_spacing = int(config["Options"]["space_between_buttons"])
fullscreen_mode = config["Options"]["fullscreen_mode"].capitalize()

# Variables for text
button_one = config["Text"]["button_one"]
button_two = config["Text"]["button_two"]
button_three = config["Text"]["button_three"]
button_four = config["Text"]["button_four"]
button_five = config["Text"]["button_five"]

# Variables for colors
background_color = config["Colors"]["background_color"]
button_background = config["Colors"]["button_background"]
button_hover = config["Colors"]["button_hover"]
button_shadow = config["Colors"]["button_shadow"]
button_activate = config["Colors"]["button_activate"]
text_color = config["Colors"]["text_color"]
text_shadow = config["Colors"]["text_shadow"]

lines_list = [
    '@define-color bg-color ',
    '@define-color button-bg-color ',
    '@define-color bg-hover ',
    '@define-color box-shadow ',
    '@define-color button-active-bg-color ',
    '@define-color text-color ',
    '@define-color text-shadow ',
]

vars_list = [
    background_color,
    button_background,
    button_hover,
    button_shadow,
    button_activate,
    text_color,
    text_shadow,
]

path_to_css = os.path.dirname(os.path.abspath(__file__)) + "/gtk_style.css"
with open(path_to_css, 'r') as css_file:
    for i in range(0, 7):
        css_file.seek(0)
        lines = css_file.readlines()
        lines[i] = lines_list[i] + vars_list[i] + ';\n'
        with open(path_to_css, 'w') as file:
            file.writelines(lines)
