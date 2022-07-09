#!/usr/bin/python
from configuration import *
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class ConfirmAction(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Confirm", transient_for=parent, modal=True)
        self.set_default_size(dialog_width, dialog_height)

        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, status, Gtk.ResponseType.YES
        )

        label = Gtk.Label(label="\nAre you sure?")

        box = self.get_content_area()
        box.add(label)
        self.show_all()


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyBye")
        Gtk.Window.set_default_size(self, width, height)
        self.set_border_width(border_width)
        self.set_decorated(False)
        self.set_resizable(False)

        if window_position == "center":
            self.set_position(Gtk.WindowPosition.CENTER)
        elif window_position == "mouse":
            self.set_position(Gtk.WindowPosition.MOUSE)

        self.connect('key-press-event', self.on_key_pressed)

        if orientation == "horizontal":
            self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=space)
        else:
            self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=space)
        self.add(self.box)

        if enable_icons == "True":
            button1 = Gtk.Button.new_from_icon_name(icon_name=button_one_icon, size=icon_size)
            Gtk.Widget.set_tooltip_text(button1, button_one)

            button2 = Gtk.Button.new_from_icon_name(icon_name=button_two_icon, size=icon_size)
            Gtk.Widget.set_tooltip_text(button2, button_two)

            button3 = Gtk.Button.new_from_icon_name(icon_name=button_three_icon, size=icon_size)
            Gtk.Widget.set_tooltip_text(button3, button_three)

            button4 = Gtk.Button.new_from_icon_name(icon_name=button_four_icon, size=icon_size)
            Gtk.Widget.set_tooltip_text(button4, button_four)

            button5 = Gtk.Button.new_from_icon_name(icon_name=button_five_icon, size=icon_size)
            Gtk.Widget.set_tooltip_text(button5, button_five)
        else:
            button1 = Gtk.Button.new_with_label(button_one)
            button2 = Gtk.Button.new_with_label(button_two)
            button3 = Gtk.Button.new_with_label(button_three)
            button4 = Gtk.Button.new_with_label(button_four)
            button5 = Gtk.Button.new_with_label(button_five)

    # First button    
        button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(button1, True, True, 0)
    # Second button
        button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(button2, True, True, 0)
    # Third button
        button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(button3, True, True, 0)
    # Fourth button
        button4.connect("clicked", self.on_button4_clicked)
        self.box.pack_start(button4, True, True, 0)
    # Fifth button
        button5.connect("clicked", self.on_button5_clicked)
        self.box.pack_start(button5, True, True, 0)
    # Cancel button
        if enable_cancel == "true":
            cancel = Gtk.Button.new_from_icon_name(icon_name=cancel_icon, size=icon_size)
            Gtk.Widget.set_tooltip_text(cancel, "Cancel")
            cancel.connect("clicked", self.on_cancel_pressed)
            self.box.pack_start(cancel, False, True, 0)
        
    # Button functions
    def on_button1_clicked(self, widget):
        if confirmation == "True":
            global status
            status = button_one

            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                click = os.system(button_one_command)
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            click = os.system(button_one_command)

    def on_button2_clicked(self, widget):
        if confirmation == "True":
            global status
            status = button_two

            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                click = os.system(button_two_command)
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            click = os.system(button_two_command)

    def on_button3_clicked(self, widget):
        if confirmation == "True":
            global status
            status = button_three
            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                click = os.system(button_three_command)
                Gtk.main_quit()
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            click = os.system(button_three_command)
            Gtk.main_quit()

    def on_button4_clicked(self, widget):
        if confirmation == "True":
            global status
            status = button_four
            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                click = os.system(button_four_command)
                Gtk.main_quit()
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            click = os.system(button_four_command)
            Gtk.main_quit()
    
    def on_button5_clicked(self, widget):
        if confirmation == "True":
            global status
            status = button_five
            dialog = ConfirmAction(self)
            response = dialog.run()
            
            if response == Gtk.ResponseType.YES:
                click = os.system(button_five_command)
            elif response == Gtk.ResponseType.CANCEL:
                dialog.destroy()
        elif confirmation == "False":
            click = os.system(button_five_command)
            
    # Key press function
    def on_key_pressed(self, widget, event):
        pressed_key = Gdk.keyval_name(event.keyval)
        alt = (event.state & Gdk.ModifierType.MOD1_MASK)

        if pressed_key == "Escape":
            Gtk.main_quit()
            
        if enable_shortcuts == "True":
            if alt and pressed_key == "1":
                but1 = os.system(button_one_command)
            elif alt and pressed_key == "2":
                but2 = os.system(button_two_command)
            elif alt and pressed_key == "3":
                but3 = os.system(button_three_command)
            elif alt and pressed_key == "4":
                but4 = os.system(button_four_command)
            elif alt and pressed_key == "5":
                but5 = os.system(button_five_command)

    def on_cancel_pressed(self, cancel):
        Gtk.main_quit()
    
if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
