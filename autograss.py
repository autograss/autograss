#! /usr/bin/python

import sys
sys.path.insert(0, 'motor_control/')
from os import path,system
import commands
import time
from photo import Photo
from move_control import MoveControl


class AutoGrass:

    def direction(self):
        photo = Photo(260,260,'180',30)
        i = 0
        start = True
        while i < 100:
            photo.take_photo_with_picamera()
            self.move_robot(photo)
            i+=1

    def move_robot(self, photo):
        movementalgorithm = "../movementalgorithm/bin/movimentalgorithm"
        direction = str(commands.getoutput(movementalgorithm + ' ' + photo.path()))
        print "direction: " + direction
        control = MoveControl()
        control.move(direction)

    def direction_without_camera(self):
        photo = Photo(1024,768,'0',30)
        images = photo.use_photos_test_images()
        for image in images:
            cmd = 'cp photos_test/%s photos/direction.jpg' % image
            system(cmd)
            self.move_robot(photo)

def main():
    start_time = time.time()
    #AutoGrass.direction_without_camera()
    autograss = AutoGrass()
    autograss.direction()
    print("%s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()
