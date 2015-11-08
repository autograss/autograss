#! /usr/bin/python

import sys
sys.path.insert(0, 'motor_control/')
from os import path
import commands
import time
from photo import Photo
from move_control import MoveControl


class AutoGrass:

    def direction(self):
        photo = Photo(1024,768,'0',30)
        i = 0
        start = True
        while start:
            photo.take_photo_with_picamera()
            move_robot()
            i+=1

    def move_robot(self):
        movementalgorithm = "../movementalgorithm/bin/movimentalgorithm"
        direction = str(commands.getoutput(movementalgorithm + ' ' + photo.path()))
        control = MoveControl()
        control.move(direction)

    @staticmethod
    def direction_without_camera(self):
        images = Photo.use_photos_test_images()
        for image in images:
            cmd = 'cp photos_test/%s photos/direction.jpg' % image
            system(cmd)
            move_robot()

def main():
    start_time = time.time()
    autograss = AutoGrass()
    autograss.direction()
    #print("%s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()
