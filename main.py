import os
import configparser
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

home = os.path.expanduser('~')
path_to_config = home + "/.config/PyBye/pybye.conf"
config = configparser.ConfigParser()

# Configuration to write to the configfile
config.add_section("Commands") 
config.set("Commands", "shutdown_command", "shutdown now")
config.set("Commands", "reboot_command", "reboot")
config.set("Commands", "lockscreen_command", "slock")
config.set("Commands", "suspend_command", "suspend")
config.set("Commands", "logout_command", "logout")

config.add_section("Icons")
config.set("Icons", "shutdown_icon", "system-shutdown-symbolic")
config.set("Icons", "reboot_icon", "system-reboot-symbolic")
config.set("Icons", "lockscreen_icon", "system-lock-screen-symbolic")
config.set("Icons", "suspend_icon", "media-playback-pause-symbolic")
config.set("Icons", "logout_icon", "system-log-out-symbolic")
config.set("Icons", "menu_icon", "menu-symbolic")

config.add_section("Size")
config.set("Size", "Height", "150")
config.set("Size", "Width", "800")
config.set("Size", "Border_width", "10")

# Create folder for config file if it does not exist yet
if not os.path.exists(home + "/.config/PyBye/"):
    os.mkdir(home + "/.config/PyBye/")

# Write configuration to the file if the file does not exist yet
# if not os.path.exists(path_to_config):
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
lockscreen_command = config["Commands"]["lockscreen_command"]
suspend_command = config["Commands"]["suspend_command"]
logout_command = config["Commands"]["logout_command"]

# Variables for size
width = int(config["Size"]["Width"])
height = int(config["Size"]["Height"])
border_width = int(config["Size"]["Border_width"])


class ConfirmAction(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Confirm", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_NO, Gtk.ResponseType.NO, Gtk.STOCK_YES, Gtk.ResponseType.YES
        )

        self.set_default_size(150, 100)

        label = Gtk.Label(label="\nAre you sure?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyBye")
        Gtk.Window.set_default_size(self, width, height)
        self.set_border_width(border_width)

        self.box = Gtk.Box(spacing=5)
        self.add(self.box)

        
        self.popover = Gtk.Popover()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        settings = Gtk.ModelButton(label="Settings")
        settings.connect("clicked", self.on_settings_clicked)
        vbox.pack_start(settings, False, True, 10)
        about = Gtk.ModelButton(label="About")
        about.connect("clicked", self.on_about_clicked)
        vbox.pack_start(about, False, True, 10)
        vbox.show_all()

        self.popover.add(vbox)
        self.popover.set_position(Gtk.PositionType.BOTTOM)

        menu = Gtk.MenuButton(label="", popover=self.popover)
        self.box.pack_end(menu, False, False, 0)

        shutdown = Gtk.Button.new_from_icon_name(icon_name=shutdown_icon, size=6)
        shutdown.connect("clicked", self.on_shutdown_clicked)
        self.box.pack_start(shutdown, True, True, 0)

        reboot = Gtk.Button.new_from_icon_name(icon_name=reboot_icon, size=6)
        reboot.connect("clicked", self.on_reboot_clicked)
        self.box.pack_start(reboot, True, True, 0)

        suspend = Gtk.Button.new_from_icon_name(icon_name=suspend_icon, size=6)
        suspend.connect("clicked", self.on_suspend_clicked)
        self.box.pack_start(suspend, True, True, 0)

        lock_screen = Gtk.Button.new_from_icon_name(icon_name=lockscreen_icon, size=6)
        lock_screen.connect("clicked", self.on_lock_screen_clicked)
        self.box.pack_start(lock_screen, True, True, 0)

        log_out = Gtk.Button.new_from_icon_name(icon_name=logout_icon, size=6)
        log_out.connect("clicked", self.on_log_out_clicked)
        self.box.pack_start(log_out, True, True, 0)
        

    def on_about_clicked(self, about):
        dialog = Gtk.AboutDialog()
        dialog.set_program_name("PyBye")
        dialog.set_comments("Shutdown menu for desktop Linux.")
        dialog.set_version("1.0")
        icon_file = Gtk.IconTheme.get_default().load_icon("python", 100, 0)
        dialog.set_logo(icon_file)
        dialog.set_website("https://github.com/x-crowbar-x/PyBye")
        dialog.set_authors(["Pavel Allahverdov <pennyvoidtea@gmail.com>"])
        dialog.set_transient_for(self)
        text = ("Distributed under the GNU GPL(v3) license.\n")
        text += 'https://github.com/x-crowbar-x/PyBye/main/LICENSE\n'
        dialog.set_license(text)
        dialog.run()
        dialog.destroy()

    def on_settings_clicked(self, settings):
        pass

    def on_shutdown_clicked(self, shutdown):
        dialog = ConfirmAction(self)
        response = dialog.run()

        if response == Gtk.ResponseType.YES:
            shut = os.system(shutdown_command)
        elif response == Gtk.ResponseType.NO:
            dialog.destroy()
        
    def on_reboot_clicked(self, reboot):
        dialog = ConfirmAction(self)
        response = dialog.run()

        if response == Gtk.ResponseType.YES:
            restart = os.system(reboot_command)
        elif response == Gtk.ResponseType.NO:
            dialog.destroy()
    
    def on_lock_screen_clicked(self, lock_screen):
        dialog = ConfirmAction(self)
        response = dialog.run()

        if response == Gtk.ResponseType.YES:
            lock = os.system(lockscreen_command)
            Gtk.main_quit()
        elif response == Gtk.ResponseType.NO:
            dialog.destroy()

    def on_suspend_clicked(self, suspend):
        dialog = ConfirmAction(self)
        response = dialog.run()

        if response == Gtk.ResponseType.YES:
            sus = os.system(suspend_command)
            Gtk.main_quit()
        elif response == Gtk.ResponseType.NO:
            dialog.destroy()

    def on_log_out_clicked(self, log_out):
        dialog = ConfirmAction(self)
        response = dialog.run()

        if response == Gtk.ResponseType.YES:
            lout = os.system(logout_command)
        elif response == Gtk.ResponseType.NO:
            dialog.destroy()


if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
