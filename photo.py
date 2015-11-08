#!/usr/bin/python
import os
import time
from subprocess import call
import picamera
from os import listdir
from os.path import isfile, join

class Photo:

    def __init__(self,width,height,rotate,framerate):
        self.width  = width
        self.height = height
        self.rotate = rotate
        self.framerate = framerate
        self.img_name = 'direction.jpg'


    def take_photo_with_raspistill(self):
        rasp_cmd = "raspistill -o " + self.path + self.options() + ' -t 300'
        call([rasp_cmd], shell=True)

    def take_photo_with_picamera(self):
        camera = picamera.PiCamera()
        camera.resolution = (self.width, self.height)
        camera.framerate = 30
        camera.capture_sequence([self.path()])
        camera.close()

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

    def use_photos_test_images(self):
        img_path = 'photos_test'
        images = [f for f in listdir(img_path)]
        full_img = []
        for i in range(50):
            full_img.append(images[3])
        return full_img
