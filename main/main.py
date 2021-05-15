#https://python-gtk-3-tutorial.readthedocs.io/en/latest/
import gi
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from print_page.print_page import Print_Page

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Grammar Sheets Print Out")

        main_container = Gtk.Box()
        self.set_border_width(20)
        self.add(main_container)

        self.main_page = MainPage(self)
        main_container.add(self.main_page)
        main_container.show()

        self.print_page = Print_Page(self)
        main_container.add(self.print_page)

        self.main_page.show_all()


class MainPage(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window
        self.set_border_width(10)

        self.set_orientation(Gtk.Orientation.VERTICAL)

        container = Gtk.Grid()
        container.set_row_spacing(5)
        self.add(container)

        explainerText = "Please select a level"
        button1Text = "My First Grammar 1"
        button2Text = "My First Grammar 2"
        button3Text = "My First Grammar 3"
        button4Text = "My Next Grammar 1"
        button5Text = "My Next Grammar 2"

        self.explainerLabel = Gtk.Label()
        self.explainerLabel.set_text(explainerText)
        self.explainerLabel.set_justify(Gtk.Justification.LEFT)
        self.button1 = Gtk.Button(label=button1Text)
        self.button2 = Gtk.Button(label=button2Text)
        self.button3 = Gtk.Button(label=button3Text)
        self.button4 = Gtk.Button(label=button4Text)
        self.button5 = Gtk.Button(label=button5Text)

        self.button1.connect("clicked", self.on_class_button_clicked, button1Text)
        self.button2.connect("clicked", self.on_class_button_clicked, button2Text)
        self.button3.connect("clicked", self.on_class_button_clicked, button3Text)
        self.button4.connect("clicked", self.on_class_button_clicked, button4Text)
        self.button5.connect("clicked", self.on_class_button_clicked, button5Text)
        self.label1 = Gtk.Label()
        self.entry2 = Gtk.Entry()
        self.entry3 = Gtk.Entry()
        self.entry4 = Gtk.Entry()

        self.buttonQuit = Gtk.Button(label="Quit")
        self.buttonQuit.connect("clicked", self.on_buttonQuit_clicked)

        #self.pack_start(self.button1, True, True, 0)
        #self.pack_start(self.button2, True, True, 0)
        #self.pack_start(self.button3, True, True, 0)
        #self.pack_start(self.button4, True, True, 0)
        #self.pack_start(self.buttonQuit, True, True, 0)
        container.add(self.explainerLabel)
        container.attach_next_to(self.button1, self.explainerLabel, Gtk.PositionType.BOTTOM, 1, 2)
        container.attach_next_to(self.button2, self.button1, Gtk.PositionType.BOTTOM, 1, 2)
        container.attach_next_to(self.button3, self.button2, Gtk.PositionType.BOTTOM, 1, 2)
        container.attach_next_to(self.button4, self.button3, Gtk.PositionType.BOTTOM, 1, 2)
        container.attach_next_to(self.button5, self.button4, Gtk.PositionType.BOTTOM, 1, 2)

        footerSeparator = Gtk.HSeparator()
        footer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        footer.pack_start(footerSeparator, True, True, 0)
        footer.pack_end(self.buttonQuit, True, True, 0)
        self.set_spacing(20)
        self.pack_end(footer, True, True, 0)

    def show_print_page(self, *args):
        self.__parent_window.print_page.show_all()
        self.hide()

    def on_class_button_clicked(self, widget, *data):
        self.__parent_window.print_page.setTitle(data[0])
        self.show_print_page()

    def on_buttonQuit_clicked(self, widget):
        print("Try to exit...")
        self.__parent_window.destroy()

class PageData:
  def __init__(self, title, lesson):
    self.title = title
    self.lessons = lessons

if __name__ == '__main__':
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.connect("destroy", Gtk.main_quit)
    window.show()
    Gtk.main()
