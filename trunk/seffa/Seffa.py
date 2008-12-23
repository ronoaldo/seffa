#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import sys

import gtk
import gtk.gdk
import gtk.glade

from seffa.constants import *
from seffa.animation import MovieFrame, MovieImage
from seffa.project import AnimationProject

class SeffaApplication(gtk.glade.XML):
    """ Seffa main application GUI. """

    filename = os.path.join(DATADIR,"glade","main.glade")

    # Python Object code

    def __init__(self):
        gtk.glade.XML.__init__(self, self.filename)
        
        self.mainWindow = self.get_widget("mainWindow")
        self.mainWindow.show_all()

        self.signal_autoconnect(self)

        # TODO: fix the project resolution
        self.project = AnimationProject()

        # Setup the frameEditor
        w, h = self.movieDimensions() 
        self.frameEditor.set_size_request(w, h)

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
        
        self.drawBackground()
        #self.drawPixbuf(1,1,pixbuf)


    # Helper Functions

    def _drawPrepare(self):
        gc = self.frameEditor.get_style().fg_gc[gtk.STATE_NORMAL]
        
        black = gtk.gdk.Color(0,0,0)
        white = gtk.gdk.Color(255,255,255)

        gc.set_rgb_fg_color(black)
        
        return gc

    def drawBackground(self):
        # TODO: Draw the background image, not a gray color...
        gray = gtk.gdk.Color(255,255,255)
        w, h = self.movieDimensions()
        
        fx, fy, fw, fh = self.frameEditor.get_allocation()
        x = (fw / 2) - (w / 2)
        y = (fh / 2) - (h / 2)

        self.drawRectangle(x, y, w, h, bg=gray)
        

    def drawRectangle(self, x, y, w, h, bg=None):
        gc = self._drawPrepare()
                
        self.frameEditor.window.draw_rectangle(
            gc, False, x,y, w-1,h-1)

        if bg is not None:
            gc.set_rgb_bg_color(bg)
            self.frameEditor.window.draw_rectangle(
                gc, True, x,y, w-1,h-1)

    def drawPixbuf(self, x, y, pixbuf):
        gc = self._drawPrepare()      
        
        pw, ph = pixbuf.get_width(), pixbuf.get_height()
        self.frameEditor.window.draw_pixbuf(gc, pixbuf, 0, 0, x, y)

    def movieDimensions(self):
        return self.project.movie.width, self.project.movie.height

    def quit(self):
        """ Finish the application, saving current projects.
            TODO: Save projects before quit. """
        gtk.main_quit()


def run():
    app = SeffaApplication()
    gtk.main()
