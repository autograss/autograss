#!/usr/bin/python
import os
import time
import subprocess
import picamera

class Photo:

    def __init__(self,width,height,rotate):
        self.width  = width
        self.height = height
        self.rotate = rotate
        self.img_name = 'direction.jpg'


    def take_photo(self):
        start_time2 = time.time()
        camera = picamera.PiCamera()
        camera.resolution = (self.width, self.height)
        camera.framerate = 30
        camera.capture_sequence([self.path()])
        print("%s seconds foto" % (time.time() - start_time2))

    def path(self):
        return 'photos/' + self.img_name

    def options(self):
        options = self._width() + self._height() + self._rotate()
        return options

    def _width(self):
        return ' -w ' + self.width

    def _height(self):
        return ' -h ' + self.height

    def _rotate(self):
        return ' -rot ' + self.rotate

