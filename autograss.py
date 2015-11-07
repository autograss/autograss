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
        photo = Photo(1024,768,'0')
        photo.take_photo_with_picamera()
        movementalgorithm = "../movementalgorithm/bin/movimentalgorithm"
        direction = str(commands.getoutput(movementalgorithm + ' ' + photo.path()))
        control = MoveControl()
        control.move(direction)

def main():
    start_time = time.time()
    autograss = AutoGrass()
    autograss.direction()
    #print("%s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()
