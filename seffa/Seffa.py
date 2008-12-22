#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import sys

import gtk
import gtk.gdk
import gtk.glade

from seffa.constants import *
from seffa.animation import MovieAnimation, MovieFrame, Image

class SeffaApplication(gtk.glade.XML):
    """ Seffa main application GUI. """

    filename = os.path.join(DATADIR,"glade","main.glade")

    # Python Object code

    def __init__(self):
        gtk.glade.XML.__init__(self, self.filename)
        
        self.mainWindow = self.get_widget("mainWindow")
        self.mainWindow.show_all()

        self.signal_autoconnect(self)

    def __getattr__(self, name):
        widget = self.get_widget(name)
        if widget is not None:
            return widget
        else:
            raise AttributeError, widget

    # Gtk Callbacks

    def on_mainWindow_delete_event(self, *args, **kargs):
        self.quit()

    def on_frameEditor_expose_event(self, frameEditor, event):
        x,y, w,h = frameEditor.get_allocation()
        
        filepath = os.path.join(DATADIR, "images","prolinux.png")
        pixbuf = gtk.gdk.pixbuf_new_from_file(filepath)
        
        self.drawRectangle(0,0, w,h)
        self.drawPixbuf(1,1,pixbuf)


    # Helper Functions

    def _drawPrepare(self):
        gc = self.frameEditor.get_style().fg_gc[gtk.STATE_NORMAL]
        
        black = gtk.gdk.Color(0,0,0)
        white = gtk.gdk.Color(255,255,255)

        gc.set_rgb_fg_color(black)
        gc.set_rgb_bg_color(white)
        
        return gc

    def drawRectangle(self, x, y, w, h):
        gc = self._drawPrepare()
        
        self.frameEditor.window.draw_rectangle(gc, False, x, y, w-1, h-1)

    def drawPixbuf(self, x, y, pixbuf):
        gc = self._drawPrepare()      
        
        pw, ph = pixbuf.get_width(), pixbuf.get_height()
        self.frameEditor.window.draw_pixbuf(gc, pixbuf, 0, 0, x, y)

    def quit(self):
        """ Finish the application, saving current projects.
            TODO: Save projects before quit. """
        gtk.main_quit()


def run():
    app = SeffaApplication()
    gtk.main()
