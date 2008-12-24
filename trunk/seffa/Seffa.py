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
        self.setupFrameEditor()

    def __getattr__(self, name):
        widget = self.get_widget(name)
        if widget is not None:
            return widget
        else:
            raise AttributeError, name

    # Gtk Callbacks

    def on_mainWindow_delete_event(self, *args, **kargs):
        self.quit()

    def on_frameEditor_expose_event(self, frameEditor, event):
        
        mw, mh = self.movieDimensions()
        fx, fy, fw, fh = frameEditor.get_allocation()
        cx = (fw/2) - (mw/2)
        cy = (fh/2) - (mh/2)

        frameEditor.window.draw_drawable(frameEditor.window.new_gc(),
            self.framePixmap, 0, 0, cx, cy, fw, fh)
        return False


    # Helper Functions
    
    def setupFrameEditor(self):
        w, h = self.movieDimensions() 
        
        self.frameEditor.set_size_request(w, h)
        self.framePixmap = gtk.gdk.Pixmap(self.frameEditor.window, w, h)
        
        black = gtk.gdk.color_parse("#000000")
        white = gtk.gdk.color_parse("#ffffff")
        
        self.frameGC = self.framePixmap.new_gc()
        self.frameGC.set_foreground(black)
        self.frameGC.set_background(white)
        
        self.createBackground()

    def createTilePixmap(self):
        path = os.path.join(DATADIR, "images", "bg-tile.png")
        pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        w, h = pixbuf.get_width(), pixbuf.get_height()
        pixmap = gtk.gdk.Pixmap(self.frameEditor.window, w, h)
        pixmap.draw_pixbuf(pixmap.new_gc(), pixbuf, 0, 0, 0, 0)
        return pixmap

    def createBackground(self):
        w, h = self.movieDimensions()
        tile = self.createTilePixmap()
        gc = self.framePixmap.new_gc(tile=tile, fill=gtk.gdk.TILED)
        
        self.framePixmap.draw_rectangle(
            gc, True, 0, 0, w, h)

    def drawPixbuf(self, x, y, pixbuf):
        gc = self._drawPrepare()
        
        pw, ph = pixbuf.get_width(), pixbuf.get_height()
        self.framePixmap.window.draw_pixbuf(gc, pixbuf, 0, 0, x, y)

    def movieDimensions(self):
        return self.project.movie.width, self.project.movie.height

    def quit(self):
        """ Finish the application, saving current projects.
            TODO: Save projects before quit. """
        gtk.main_quit()


def run():
    app = SeffaApplication()
    gtk.main()
