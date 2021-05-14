#https://python-gtk-3-tutorial.readthedocs.io/en/latest/
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__(title="Grammar Sheets Print Out")
        self.set_border_width(20)
        #self.set_default_size(300, 500)

        main_container = Gtk.Box(spacing=10)
        self.add(main_container)
        main_container.show()

        self.main_page = MainPage(self)
        main_container.add(self.main_page)

        self.print_page = PrintingPage(self)
        main_container.add(self.print_page)
        
        self.main_page.show_all()

class MainPage(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window

        self.set_orientation(Gtk.Orientation.VERTICAL)

        button1Text = "My First Grammar 1"
        button2Text = "My First Grammar 2"
        button3Text = "My First Grammar 3"
        button4Text = "My Next Grammar 1"
        button5Text = "My Next Grammar 2"

        self.button1 = Gtk.Button(label=button1Text)
        self.button2 = Gtk.Button(label=button2Text)
        self.button3 = Gtk.Button(label=button3Text)
        self.button4 = Gtk.Button(label=button4Text)

        self.button1.connect("clicked", self.on_class_button_clicked, button1Text)
        self.button2.connect("clicked", self.on_class_button_clicked, button2Text)
        self.button3.connect("clicked", self.on_class_button_clicked, button3Text)
        self.button4.connect("clicked", self.on_class_button_clicked, button4Text)
        self.label1 = Gtk.Label()
        self.entry2 = Gtk.Entry()
        self.entry3 = Gtk.Entry()
        self.entry4 = Gtk.Entry()

        self.buttonQuit = Gtk.Button(label="Quit")
        self.buttonQuit.connect("clicked", self.on_buttonQuit_clicked)

        self.pack_start(self.button1, True, True, 0)
        self.pack_start(self.button2, True, True, 0)
        self.pack_start(self.button3, True, True, 0)
        self.pack_start(self.button4, True, True, 0)
        self.pack_start(self.buttonQuit, True, True, 0)

    def show_print_page(self, *args):
        self.__parent_window.print_page.show_all()
        self.hide()

    def on_class_button_clicked(self, widget, *data):
        #print("General Button Test")
        #print(data[0])
        self.__parent_window.print_page.setTitle(data[0])
        self.show_print_page()

    def on_buttonQuit_clicked(self, widget):
        print("Try to exit...")
        self.__parent_window.destroy()

class PrintingPage(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)
        self.__parent_window = parent_window
        self.set_orientation(Gtk.Orientation.HORIZONTAL)
        #self.add(self.box)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)
        self.pack_start(vbox_left, True, True, 0)
        self.pack_start(vbox_right, True, True, 0)

        self.label1 = Gtk.Label()
        self.title = Gtk.Label()
        label_text = "Test"
        self.title.set_label(label_text)
        self.label2 = Gtk.Label()
        self.label2.set_label("Lessons")
        self.entry1 = Gtk.Entry()
        vbox_left.pack_start(self.title, True, True, 0)
        vbox_right.pack_start(self.label2, True, True, 0)

        self.buttonQuit = Gtk.Button(label="Quit")
        self.buttonQuit.connect("clicked", self.on_buttonQuit_clicked)

        self.pack_start(self.buttonQuit, True, True, 0)

    def show_main_page(self, *args):
        self.__parent_window.main_page.show_all()
        self.hide()

    def setTitle(self, text):
        self.title.set_label(text)

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
