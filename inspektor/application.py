#!/usr/bin/env python3

'''
   Copyright 2018 Adi Hezral (hezral@gmail.com)

   This file is part of inspektor.

    inspektor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    inspektor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with inspektor.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GLib
#from constants import inspektorAttributes
from mainwindow import inspektorWindow
from services.manager import inspektorManager


class inspektor(Gtk.Application):
    def __init__(self):
        super().__init__()

        self.props.application_id = "com.github.hezral.inspektor" #inspektorAttributes.application_id
        self.props.flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE
        self.add_main_option("test", ord("t"), GLib.OptionFlags.NONE, GLib.OptionArg.NONE, "Command line test", None)

        self.instance = None
        self.window = None
        
    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        # We only allow a single window and raise any existing ones
        if not self.window:
            # Windows are associated with the application 
            # when the last one is closed the application shuts down
            self.window = inspektorWindow(application=self)
        self.window.present()
        self.add_window(self.window)
        #self.window.connect('key-press-event', self.window.check)
        manager = inspektorManager(debugflag=False)
        manager.clipboard.connect('owner-change', manager.clipboard_changed)

    def do_command_line(self, command_line):
        options = command_line.get_options_dict()
        # convert GVariantDict -> GVariant -> dict
        options = options.end().unpack()

        if "test" in options:
            # This is printed on the main instance
            print("Test argument recieved: %s" % options["test"])

        self.activate()
        return 0

    def close_window(self):
        pass

    def get_default(self):
        if not self.instance:
            self.instance = inspektor()
            return self.instance

if __name__ == "__main__":
    app = inspektor()
    app.run(sys.argv)