#!/bin/python3
from subprocess import check_output, CalledProcessError
from os import path, mkdir
from configparser import ConfigParser
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

PATH_TO_CONFIG = path.expanduser("~") + "/.config/PyBye/"
PATH_TO_CSS = path.dirname(path.abspath(__file__)) + "/gtk_style.css"
config = ConfigParser()

# Configuration to write to the configfile.
config.add_section("Commands")
config.set("Commands", "button_one_command", "shutdown now")
config.set("Commands", "button_two_command", "reboot")
config.set("Commands", "button_three_command", "systemctl suspend")
config.set("Commands", "button_four_command", "dm-tool lock")
config.set("Commands", "button_five_command", "gnome-session-quit --force")
config.set("Commands", "button_six_command", "systemctl hibernate")

config.add_section("Icons")
config.set("Icons", "button_one_icon", "system-shutdown-symbolic")
config.set("Icons", "button_two_icon", "system-reboot-symbolic")
config.set("Icons", "button_three_icon", "system-suspend-symbolic")
config.set("Icons", "button_four_icon", "system-lock-screen-symbolic")
config.set("Icons", "button_five_icon", "system-log-out-symbolic")
config.set("Icons", "button_six_icon", "system-hibernate-symbolic")

config.add_section("Size")
config.set("Size", "Width", "1920")
config.set("Size", "Height", "1080")
config.set("Size", "border_width", "480")
config.set("Size", "icon_size", "6")
config.set("Size", "dialog_height", "120")
config.set("Size", "dialog_width", "150")

config.add_section("Options")
config.set("Options", "ask_for_confirmation", "True")
config.set("Options", "space_between_buttons_and_text", "20")
config.set("Options", "space_between_buttons", "20")
config.set("Options", "fullscreen_mode", "True")

config.add_section("Text")
config.set("Text", "button_one", "Shutdown")
config.set("Text", "button_two", "Reboot")
config.set("Text", "button_three", "Suspend")
config.set("Text", "button_four", "Lock screen")
config.set("Text", "button_five", "Log-Out")
config.set("Text", "button_six", "Hibernate")

config.add_section("Colors")
config.set("Colors", "background_color", "rgba(40,40,40, 0.6)")
config.set("Colors", "button_background", "rgba(40,40,40, 0.1)")
config.set("Colors", "button_hover", "rgba(235, 219, 178, 0.461)")
config.set("Colors", "button_shadow", "antiquewhite")
config.set("Colors", "button_activate", "antiquewhite")
config.set("Colors", "text_color", "#ebdbb2")
config.set("Colors", "text_shadow", "#3c3836")

# Writes configuration to the file if the file does not exist yet.
# Also creates a folder if it doesn't exist yet.
if not path.exists(PATH_TO_CONFIG + "pybye.conf"):
    if not path.exists(PATH_TO_CONFIG):
        mkdir(PATH_TO_CONFIG)
    with open(PATH_TO_CONFIG + "pybye.conf", "w") as conf:
        config.write(conf)

config.read(PATH_TO_CONFIG + "pybye.conf")

# Variables for icons.
button_one_icon = config["Icons"]["button_one_icon"]
button_two_icon = config["Icons"]["button_two_icon"]
button_three_icon = config["Icons"]["button_three_icon"]
button_four_icon = config["Icons"]["button_four_icon"]
button_five_icon = config["Icons"]["button_five_icon"]
button_six_icon = config["Icons"]["button_six_icon"]

# Variables for commands.
button_one_command = config["Commands"]["button_one_command"]
button_two_command = config["Commands"]["button_two_command"]
button_three_command = config["Commands"]["button_three_command"]
button_four_command = config["Commands"]["button_four_command"]
button_five_command = config["Commands"]["button_five_command"]
button_six_command = config["Commands"]["button_six_command"]

# Variables for size.
width = int(config["Size"]["Width"])
height = int(config["Size"]["Height"])
border_width = int(config["Size"]["Border_width"])
icon_size = int(config["Size"]["icon_size"])
dialog_width = int(config["Size"]["dialog_width"])
dialog_height = int(config["Size"]["dialog_height"])

# Variables for options.
confirmation = config["Options"]["ask_for_confirmation"].capitalize()
row_spacing = int(config["Options"]["space_between_buttons_and_text"])
column_spacing = int(config["Options"]["space_between_buttons"])
fullscreen_mode = config["Options"]["fullscreen_mode"].capitalize()

# Variables for text.
button_one = config["Text"]["button_one"]
button_two = config["Text"]["button_two"]
button_three = config["Text"]["button_three"]
button_four = config["Text"]["button_four"]
button_five = config["Text"]["button_five"]
button_six = config["Text"]["button_six"]

# Variables for colors.
background_color = config["Colors"]["background_color"]
button_background = config["Colors"]["button_background"]
button_hover = config["Colors"]["button_hover"]
button_shadow = config["Colors"]["button_shadow"]
button_activate = config["Colors"]["button_activate"]
text_color = config["Colors"]["text_color"]
text_shadow = config["Colors"]["text_shadow"]

lines_list = [
    "@define-color bg-color ",
    "@define-color button-bg-color ",
    "@define-color bg-hover ",
    "@define-color box-shadow ",
    "@define-color button-active-bg-color ",
    "@define-color text-color ",
    "@define-color text-shadow ",
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


def save_colors(n):
    """"Rewrites the variables inside gtk_style.css 
        to change colors if the values are different."""
    with open(PATH_TO_CSS, "r") as css_file:
        if n == 7:
            return
        css_file.seek(0)
        lines = css_file.readlines()
        if lines[n] == lines_list[n] + vars_list[n] + ";\n":
            save_colors(n+1)
        else:
            lines[n] = lines_list[n] + vars_list[n] + ";\n"
            with open(PATH_TO_CSS, "w") as file:
                file.writelines(lines)
            save_colors(n+1)


save_colors(0)


def switch_to_watch_cursor():
    """Changes cursor to 'loading' state."""
    watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
    win.get_window().set_cursor(watch_cursor)


def switch_to_arrow_cursor():
    """Changes cursor back to normal."""
    arrow_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
    win.get_window().set_cursor(arrow_cursor)


def run_command(shell_command):
    """Runs a command and displays an error if there is one."""
    try:
        check_output((shell_command), shell=True)
    except CalledProcessError as error:
        dialog = Gtk.MessageDialog(
            transient_for=MainWindow(),
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CLOSE,
            text="There's been an error while running the command.",
        )
        dialog.format_secondary_text(
            str(error)
        )
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.CLOSE:
            switch_to_arrow_cursor()
    else:
        switch_to_arrow_cursor()
        Gtk.main_quit()


def run_dialog(button_name, button_command):
    """Shows the dialog window for the clicked button.
    Takes two args: button_name and button command."""
    global status
    status = button_name
    dialog = ConfirmAction(MainWindow())
    response = dialog.run()
    if response == Gtk.ResponseType.YES:
        run_command(button_command)
        switch_to_arrow_cursor()
        dialog.hide()


class ConfirmAction(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title=status,
                         transient_for=parent,
                         modal=True,
                         name="dialog"
                         )
        self.set_default_size(dialog_width, dialog_height)
        self.set_resizable(False)
        self.connect("key-press-event", self.on_escape_pressed)
        self.add_button(Gtk.STOCK_NO, Gtk.ResponseType.CANCEL)
        self.add_button(Gtk.STOCK_YES, Gtk.ResponseType.YES)
        label = Gtk.Label(label=f"\n\nDo you want to {status.lower()}?")
        box = self.get_content_area()
        box.add(label)
        self.show_all()

    def on_escape_pressed(self, widget, event):
        pressed_key = Gdk.keyval_name(event.keyval)
        if pressed_key == "Escape":
            switch_to_arrow_cursor()
            self.hide()


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,
                            title="PyBye",
                            name="main_window"
                            )
        Gtk.Window.set_default_size(self, width, height)
        self.set_border_width(border_width)
        self.set_decorated(False)
        self.connect("key-press-event", self.on_key_pressed)

        # Get CSS style for GTK+3 from a file.
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(PATH_TO_CSS)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        buttons = {
            1: [button_one, button_one_icon, self.on_button1_clicked],
            2: [button_two, button_two_icon, self.on_button2_clicked],
            3: [button_three, button_three_icon, self.on_button3_clicked],
            4: [button_four, button_four_icon, self.on_button4_clicked],
            5: [button_five, button_five_icon, self.on_button5_clicked],
            6: [button_six, button_six_icon, self.on_button6_clicked],
        }
        grid = Gtk.Grid()

        def buttons_and_labels(n):
            """Creates 5 buttons and 5 labels under them 
                with specified text, icons, 
                icon size and corresponding commands."""
            label = Gtk.Label(label=buttons[n][0])
            label.set_selectable(False)
            button = Gtk.Button.new_from_icon_name(icon_name=buttons[n][1],
                                                   size=icon_size
                                                   )
            button.connect("clicked", buttons[n][2])
            grid.add(button)
            grid.attach_next_to(label, button,
                                Gtk.PositionType.BOTTOM,
                                1, 1)
            if n == 6:
                return
            buttons_and_labels(n+1)

        buttons_and_labels(1)

        grid.set_row_spacing(row_spacing)
        grid.set_row_homogeneous(False)
        grid.set_column_homogeneous(True)
        grid.set_column_spacing(column_spacing)
        self.add(grid)

    # Button functions.
    def on_button1_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            run_dialog(button_one, button_one_command)
        elif confirmation == "False":
            run_command(button_one_command)

    def on_button2_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            run_dialog(button_two, button_two_command)
        elif confirmation == "False":
            run_command(button_two_command)

    def on_button3_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            run_dialog(button_three, button_three_command)
        elif confirmation == "False":
            run_command(button_three_command)

    def on_button4_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            run_dialog(button_four, button_four_command)
        elif confirmation == "False":
            run_command(button_four_command)

    def on_button5_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            run_dialog(button_five, button_five_command)
        elif confirmation == "False":
            run_command(button_five_command)

    def on_button6_clicked(self, widget):
        switch_to_watch_cursor()
        if confirmation == "True":
            run_dialog(button_six, button_six_command)
        elif confirmation == "False":
            run_command(button_six_command)

    # Key press function.
    def on_key_pressed(self, widget, event):
        pressed_key = Gdk.keyval_name(event.keyval)
        if pressed_key == "Escape":
            Gtk.main_quit()


if __name__ == "__main__":
    win = MainWindow()
    screen = win.get_screen()
    visual = screen.get_rgba_visual()
    win.set_visual(visual)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    if fullscreen_mode == "True":
        win.fullscreen()
    Gtk.main()
