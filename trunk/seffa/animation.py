# -*- coding:utf8 -*-

""" Movie and MovieObject classes and helper functions. """

from seffa.constants import *

#
# MovieObject specific classes.
#

class MovieObject:
    """ A simple movie object.
        
        This is a base class for other movie objects.
        It defines some basic objects properties and methods.

        You may subclass this to implement other Movie Objects,
        such as new sprites. """

    name = "unamed"
    x = 0
    y = 0

class MovieImage(MovieObject):
    """ A movie image.

        This class is a movie object that handles an
        Image.

        It has some image specific fields and helper functions. """
    
    type   = IMAGE_PNG
    alpha  = 100
    scale  = 100
    rotate = 0
    width  = 0
    height = 0
    data   = None

    def __init__(self, type=IMAGE_PNG, data=None):
        """ Instantiates a new Image object.
            
            'type' is the image type. Must be one of 
                constants.IMAGE_* values.
            'data' is the image data. Must be valid for 
                the specified format. """

        self.type = type
        self.data = data

class FlashMovie(MovieObject):
    """ A FlashMovie object.
        
        This class handles embeded Flash Movies inside the current
        one.

        WARNING: It may not be valid for some exporting formats. """

    width  = 0
    height = 0

# 
# Movie specific classes
#

class MovieFrame:
    """ A MovieFrame object.

        This class handles a movie frame, with an object stack,
        and the object properties.

        This properties are used for creating and manipulating
        the object properties for other frames, specially the
        frames that hasn't been specified. """

    objectStack  = None
    movieObjects = None
    frameNumber  = -1

    def __init__(self, frameNumber = -1):
        """ Instantiates a new MovieFrame object.
        
            @param frameNumber the number of this frame. """

        self.frameNumber = frameNumber

class MovieAnimation:
    """ A MovieAnimation object.

        This class implements the movie animation.
        You can add frames to it, remove frames from it
        and also get frames at any position.

        If a frame is not specified, it is aproximated by the
        information found on previous defined frames or by the
        forward ones. """

    timeLine = None
    width = 640
    height = 480

    def __init__(self, duration=0, type=DURATION_BY_FRAME):
        """ Instantiates a new MovieAnimation object.
            
            'duration' is the movie duration.
            'type' is the duration type. Must be one of 
                constants.DURATION_BY_* values. """
        pass

    def addFrame(self, frame=MovieFrame()):
        """ Add a new specified frame.
            
            'frame' is the new MovieFrame object to be added to 
                the timeline. """
        pass

    def delFrame(self, framenumber):
        """ Removes a specified frame.
            
            'framenumber' is the number of the frame to be removed. """
        pass

    def getFrame(self, framenumber):
        """ Calculates the frame specified by framenumber.
            
            'framenumber' is the number of the frame to get. """
    
    def getPreviousFrame(self, framenumber):
        """ Calculates the frame previous to framenumber and returns it.
            
            Returns the calculated frame. """
        pass

    def getNextFrame(self, framenumber):
        """ Calculates the frame after framenumber and returns it.
            
            Returns the calculated frame. """
        pass
