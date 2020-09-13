import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class PopoverWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Popover Demo")
        self.set_border_width(10)

        outerbox = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        self.add(outerbox)

        button = Gtk.Button(label="Export", image=Gtk.Image.new_from_icon_name("document-export", Gtk.IconSize.LARGE_TOOLBAR))
        button.set_always_show_image(True)
        button.connect("clicked", self.on_click_me_clicked)
        outerbox.pack_start(button, False, True, 0)

        export_json_button = Gtk.Button(label="Export to JSON", image=Gtk.Image.new_from_icon_name("text-css", Gtk.IconSize.LARGE_TOOLBAR))
        export_json_button.set_always_show_image(True)
        # export_json_button.props.halign = Gtk.Align.START
        export_json_button.connect("clicked",self.on_open_clicked)

        export_csv_button = Gtk.Button(label="Export to CSV", image=Gtk.Image.new_from_icon_name("application-vnd.ms-excel", Gtk.IconSize.LARGE_TOOLBAR))
        export_csv_button.set_always_show_image(True)
        # export_csv_button.props.halign = Gtk.Align.START
        export_csv_button.connect("clicked",self.on_open_clicked)

        self.popover = Gtk.Popover()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.props.margin_left = 10
        vbox.props.margin_right = 10
        vbox.props.margin_top = 8
        vbox.props.margin_bottom = 6
        vbox.pack_start(export_json_button,True,True,4)
        vbox.pack_start(export_csv_button,True,True,4)
        self.popover.add(vbox)
        self.popover.set_position(Gtk.PositionType.RIGHT)
        self.popover.set_modal(True)

    def on_click_me_clicked(self, button):
        self.popover.set_relative_to(button)
        self.popover.show_all()
        self.popover.popup()

    def on_open_clicked(self, button):
        print('"Open" button was clicked')


win = PopoverWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()