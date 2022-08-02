#!/usr/bin/python
from configuration import *
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class ConfirmAction(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Confirm", transient_for=parent, modal=True, name="dialog")
        self.set_default_size(100, 120)
        self.set_resizable(False)
        self.connect('key-press-event', self.on_escape_pressed)

        cancel = self.add_button(Gtk.STOCK_NO, Gtk.ResponseType.CANCEL)
        yes = self.add_button(status.capitalize(), Gtk.ResponseType.YES)

        label = Gtk.Label(label=f"\n Are you sure?")
        box = self.get_content_area()
        box.add(label)
        self.show_all()

    def on_escape_pressed(self, widget, event):
        pressed_key = Gdk.keyval_name(event.keyval)
        alt = (event.state & Gdk.ModifierType.MOD1_MASK)

        if pressed_key == "Escape":
            watch_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
            win.get_window().set_cursor(watch_cursor)
            self.hide()

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyBye", name="main_window")
        Gtk.Window.set_default_size(self, width, height)
        self.set_border_width(border_width)
        self.set_decorated(False)
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.connect('key-press-event', self.on_key_pressed)

        # Get CSS style
        path_to_css = os.path.dirname(os.path.abspath(__file__)) + "/style.css"
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path(path_to_css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    # First button
        label1 = Gtk.Label(label=button_one)
        label1.set_selectable(False)
        button1 = Gtk.Button.new_from_icon_name(icon_name=button_one_icon, size=icon_size)
        button1.connect("clicked", self.on_button1_clicked)
    # Second button
        label2 = Gtk.Label(label=button_two)
        label2.set_selectable(False)
        button2 = Gtk.Button.new_from_icon_name(icon_name=button_two_icon, size=icon_size)
        button2.connect("clicked", self.on_button2_clicked)
    # Third button
        label3 = Gtk.Label(label=button_three)
        label3.set_selectable(False)
        button3 = Gtk.Button.new_from_icon_name(icon_name=button_three_icon, size=icon_size)
        button3.connect("clicked", self.on_button3_clicked)
    # Fourth button
        label4 = Gtk.Label(label=button_four)
        label4.set_selectable(False)
        button4 = Gtk.Button.new_from_icon_name(icon_name=button_four_icon, size=icon_size)
        button4.connect("clicked", self.on_button4_clicked)
    # Fifth button
        label5 = Gtk.Label(label=button_five)
        label5.set_selectable(False)
        button5 = Gtk.Button.new_from_icon_name(icon_name=button_five_icon, size=icon_size)
        button5.connect("clicked", self.on_button5_clicked)

    # Add buttons and labels to the grid
        grid = Gtk.Grid()
        if enable_cancel == "true":
            label_cancel = Gtk.Label(label="Cancel")
            cancel = Gtk.Button.new_from_icon_name(icon_name=cancel_icon, size=icon_size)
            cancel.connect("clicked", self.on_cancel_pressed)
            grid.add(cancel)
            grid.attach_next_to(label_cancel, cancel, Gtk.PositionType.BOTTOM, 1, 1)
        
        grid.add(button1)
        grid.attach_next_to(label1, button1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.add(button2)
        grid.attach_next_to(label2, button2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.add(button3)
        grid.attach_next_to(label3, button3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.add(button4)
        grid.attach_next_to(label4, button4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.add(button5)
        grid.attach_next_to(label5, button5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.set_row_spacing(row_spacing)
        grid.set_row_homogeneous(False)
        grid.set_column_homogeneous(True)
        grid.set_column_spacing(column_spacing)
        self.add(grid)

    # Button functions
    def on_button1_clicked(self, widget):
        watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
        win.get_window().set_cursor(watch_cursor)
        if confirmation == "True":
            global status
            status = button_one

            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                click = os.system(button_one_command)
            elif response == Gtk.ResponseType.CANCEL:
                watch_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
                win.get_window().set_cursor(watch_cursor)
                dialog.hide()
        elif confirmation == "False":
            click = os.system(button_one_command)

    def on_button2_clicked(self, widget):
        watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
        win.get_window().set_cursor(watch_cursor)

        if confirmation == "True":
            global status
            status = button_two

            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                click = os.system(button_two_command)
            elif response == Gtk.ResponseType.CANCEL:
                watch_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
                win.get_window().set_cursor(watch_cursor)
                dialog.hide()
        elif confirmation == "False":
            click = os.system(button_two_command)

    def on_button3_clicked(self, widget):
        watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
        win.get_window().set_cursor(watch_cursor)

        if confirmation == "True":
            global status
            status = button_three
            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                click = os.system(button_three_command)
                Gtk.main_quit()
            elif response == Gtk.ResponseType.CANCEL:
                watch_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
                win.get_window().set_cursor(watch_cursor)
                dialog.hide()
        elif confirmation == "False":
            click = os.system(button_three_command)
            Gtk.main_quit()

    def on_button4_clicked(self, widget):
        watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
        win.get_window().set_cursor(watch_cursor)

        if confirmation == "True":
            global status
            status = button_four
            dialog = ConfirmAction(self)
            response = dialog.run()

            if response == Gtk.ResponseType.YES:
                click = os.system(button_four_command)
                Gtk.main_quit()
            elif response == Gtk.ResponseType.CANCEL:
                watch_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
                win.get_window().set_cursor(watch_cursor)
                dialog.hide()
        elif confirmation == "False":
            click = os.system(button_four_command)
            Gtk.main_quit()
    
    def on_button5_clicked(self, widget):
        watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
        win.get_window().set_cursor(watch_cursor)

        if confirmation == "True":
            global status
            status = button_five
            dialog = ConfirmAction(self)
            response = dialog.run()
            
            if response == Gtk.ResponseType.YES:
                click = os.system(button_five_command)
            elif response == Gtk.ResponseType.CANCEL:
                watch_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
                win.get_window().set_cursor(watch_cursor)
                dialog.hide()
        elif confirmation == "False":
            click = os.system(button_five_command)
            
    # Key press function
    def on_key_pressed(self, widget, event):
        pressed_key = Gdk.keyval_name(event.keyval)
        alt = (event.state & Gdk.ModifierType.MOD1_MASK)

        if pressed_key == "Escape":
            watch_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
            win.get_window().set_cursor(watch_cursor)
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
    screen = win.get_screen()
    visual = screen.get_rgba_visual()
    win.set_visual(visual)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

    if fullscreen_mode == "True":
        win.fullscreen()
    else:
        win.move(-1, -5)

    watch_cursor = Gdk.Cursor(Gdk.CursorType.ARROW)
    win.get_window().set_cursor(watch_cursor)
    Gtk.main()
