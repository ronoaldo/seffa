# -*- coding: utf8 -*-

""" Internal constants used by other modules """

(
    IMAGE_PNG,
    IMAGE_JPG,
    IMAGE_GIF,
    IMAGE_GDKPIXBUF,
) = range(4)

(
    DURATION_BY_FRAME,
    DURATION_BY_TIME,
) = range(2)


import os

APPDIR  = os.path.dirname( __file__ )
DATADIR = os.path.join(APPDIR, "data")

del os
