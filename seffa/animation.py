# -*- coding:utf8 -*-

from seffa.constants import *

class MovieObject:

    name = "unamed"
    x = 0
    y = 0

class Image(MovieObject):
    
    type   = IMAGE_PNG
    alpha  = 100
    scale  = 100
    rotate = 0
    width  = 0
    height = 0

class FlashMovie(MovieObject):

    width  = 0
    height = 0

class MovieFrame:

    objectStack  = None
    movieObjects = None
    frameNumber  = -1

    def __init__(self, frameNumber = -1):
        self.frameNumber = frameNumber

class MovieAnimation:

    timeLine = None

    def __init__(self, duration=0, type=DURATION_BY_FRAME):
        pass

    def addFrame(self, frame=MovieFrame()):
        pass

    def delFrame(self, framenumber):
        pass

    def getPreviousFrame(self, framenumber):
        pass

    def getNextFrame(self, framenumber):
        pass
