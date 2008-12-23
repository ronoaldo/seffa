# -*- coding:utf8 -*-

from seffa.animation import MovieAnimation

class AnimationProject:
    
    name = "Untitled Animation"
    duration = 0.0
    saved = False
    movie = MovieAnimation(duration)

    def __init__(self):
        # TODO: Fix movie sizes, resizes...
        self.movie.width = 640
        self.movie.height = 480
