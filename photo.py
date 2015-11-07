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


    def take_photo_with_raspistill(self):
        rasp_cmd = "raspistill -o " + self.path + self.options() + ' -t 300'
        subprocess.call([rasp_cmd], shell=True)

    def take_photo_with_picamera(self):
        camera = picamera.PiCamera()
        camera.resolution = (self.width, self.height)
        camera.framerate = 30
        camera.capture_sequence([self.path()])

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
