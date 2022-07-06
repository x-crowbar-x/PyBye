#!/usr/bin/python
from configuration import *
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

status = ""


class ConfirmAction(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Confirm", transient_for=parent, modal=True)
        self.set_default_size(150, 100)

        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, status, Gtk.ResponseType.YES
        )

        label = Gtk.Label(label="\nAre you sure?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyBye", window_position=Gtk.WindowPosition.CENTER)
        Gtk.Window.set_default_size(self, width, height)
        self.set_border_width(border_width)
        self.set_decorated(False)

        self.connect('key-press-event', self.on_key_pressed)
        self.box = Gtk.Box(spacing=5)
        self.add(self.box)
    # Shutdown button
        shutdown = Gtk.Button.new_from_icon_name(icon_name=shutdown_icon, size=icon_size)
        Gtk.Widget.set_tooltip_text(shutdown, "Shutdown")
        shutdown.connect("clicked", self.on_shutdown_clicked)
        self.box.pack_start(shutdown, True, True, 0)
    # Reboot button
        reboot = Gtk.Button.new_from_icon_name(icon_name=reboot_icon, size=icon_size)
        Gtk.Widget.set_tooltip_text(reboot, "Reboot")
        reboot.connect("clicked", self.on_reboot_clicked)
        self.box.pack_start(reboot, True, True, 0)
    # Suspend button
        suspend = Gtk.Button.new_from_icon_name(icon_name=suspend_icon, size=icon_size)
        Gtk.Widget.set_tooltip_text(suspend, "Suspend")
        suspend.connect("clicked", self.on_suspend_clicked)
        self.box.pack_start(suspend, True, True, 0)
    # Lock screen button
        lock_screen = Gtk.Button.new_from_icon_name(icon_name=lockscreen_icon, size=icon_size)
        Gtk.Widget.set_tooltip_text(lock_screen, "Lock Screen")
        lock_screen.connect("clicked", self.on_lock_screen_clicked)
        self.box.pack_start(lock_screen, True, True, 0)
    # Log out button
        log_out = Gtk.Button.new_from_icon_name(icon_name=logout_icon, size=icon_size)
        Gtk.Widget.set_tooltip_text(log_out, "Log out")
        log_out.connect("clicked", self.on_log_out_clicked)
        self.box.pack_start(log_out, True, True, 0)

    # Button functions

    def on_shutdown_clicked(self, widget):
        if confirmation == "True":
            global status
            status = "  Shutdown"

            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                shut = os.system(shutdown_command)
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            shut = os.system(shutdown_command)

    def on_reboot_clicked(self, reboot):
        if confirmation == "True":
            global status
            status = "累 Reboot"

            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                restart = os.system(reboot_command)
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            restart = os.system(reboot_command)

    def on_lock_screen_clicked(self, lock_screen):
        if confirmation == "True":
            global status
            status = "  Lock screen"
            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                lock = os.system(lockscreen_command)
                Gtk.main_quit()
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            lock = os.system(lockscreen_command)
            Gtk.main_quit()

    def on_suspend_clicked(self, suspend):
        if confirmation == "True":
            global status
            status = " Suspend"
            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                sus = os.system(suspend_command)
                Gtk.main_quit()
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            sus = os.system(suspend_command)
            Gtk.main_quit()
    
    def on_log_out_clicked(self, widget):
        if confirmation == "True":
            global status
            status = " Log-out"
            dialog = ConfirmAction(self)
            response = dialog.run()
            
            if response == Gtk.ResponseType.YES:
                lout = os.system(logout_command)
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            lout = os.system(logout_command)
            
    # Key press function
    def on_key_pressed(self, widget, event):
        pressed_key = Gdk.keyval_name(event.keyval)
        alt = (event.state & Gdk.ModifierType.MOD1_MASK)

        if pressed_key == "Escape":
            Gtk.main_quit()
        elif alt and pressed_key == "1":
            shut = os.system(shutdown_command)
        elif alt and pressed_key == "2":
            restart = os.system(reboot_command)
        elif alt and pressed_key == "3":
            sus = os.system(suspend_command)
        elif alt and pressed_key == "4":
            lock = os.system(lockscreen_command)
        elif alt and pressed_key == "5":
            lout = os.system(logout_command)


if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
