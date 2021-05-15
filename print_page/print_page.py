import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Print_Page(Gtk.Box):
    def __init__(self, parent_window):
        super().__init__(spacing=10)

        self.__parent_window = parent_window
        self.set_orientation(Gtk.Orientation.HORIZONTAL)

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

        self.buttonBack = Gtk.Button(label="Back")
        self.buttonBack.connect("clicked", self.on_buttonBack_clicked)

        self.buttonQuit = Gtk.Button(label="Quit")
        self.buttonQuit.connect("clicked", self.on_buttonQuit_clicked)

        self.pack_start(self.buttonBack, True, True, 0)
        self.pack_start(self.buttonQuit, True, True, 0)

    def show_main_page(self, *args):
        self.__parent_window.main_page.show_all()
        self.hide()

    def setTitle(self, text):
        self.title.set_label(text)

    def on_buttonQuit_clicked(self, widget):
        print("Try to exit...")
        self.__parent_window.destroy()

    def on_buttonBack_clicked(self, widget):
        print("Back to Home")
        self.__parent_window.main_page.show_all()
        self.hide()
