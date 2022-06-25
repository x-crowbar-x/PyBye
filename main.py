import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


icons = ["system-shutdown-symbolic", "system-reboot-symbolic", "system-lock-screen-symbolic", "media-playback-pause-symbolic", "system-log-out-symbolic"]

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Shutdown Menu")
        Gtk.Window.set_default_size(self, 800, 150)
        self.set_border_width(10)
        self.connect("key-press-event", self.do_key_press_event)
        self.box = Gtk.Box(spacing=5)
        self.add(self.box)

        shutdown = Gtk.Button.new_from_icon_name(icon_name=icons[0], size=6)
        shutdown.connect("clicked", self.on_shutdown_clicked)
        self.box.pack_start(shutdown, True, True, 0)

        reboot = Gtk.Button.new_from_icon_name(icon_name=icons[1], size=6)
        reboot.connect("clicked", self.on_reboot_clicked)
        self.box.pack_start(reboot, True, True, 0)

        suspend = Gtk.Button.new_from_icon_name(icon_name=icons[3], size=6)
        suspend.connect("clicked", self.on_suspend_clicked)
        self.box.pack_start(suspend, True, True, 0)

        lock_screen = Gtk.Button.new_from_icon_name(icon_name=icons[2], size=6)
        lock_screen.connect("clicked", self.on_lock_screen_clicked)
        self.box.pack_start(lock_screen, True, True, 0)

        log_out = Gtk.Button.new_from_icon_name(icon_name=icons[4], size=6)
        log_out.connect("clicked", self.on_log_out_clicked)
        self.box.pack_start(log_out, True, True, 0)
        

    def on_shutdown_clicked(self, shutdown):
        shut = os.system("shutdown")
        
    def on_reboot_clicked(self, reboot):
        restart = os.system("reboot")
    
    def on_lock_screen_clicked(self, lock_screen):
        lock = os.system("slock")

    def on_suspend_clicked(self, suspend):
        sus = os.system("suspend")

    def on_log_out_clicked(self, log_out):
        lout = os.system("logout")

    def do_key_press_event(self, event):
        escape = Gtk.main_quit()

if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
