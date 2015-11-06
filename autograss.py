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
        photo.take_photo()
        movementalgorithm = "../movementalgorithm/bin/movimentalgorithm"
        start_time1 = time.time()
        direction = commands.getoutput(movementalgorithm + ' ' +  photo.path())
        print("%s seconds processamento" % (time.time() - start_time1))
        print direction


def main():
    start_time = time.time()
    autograss = AutoGrass()
    autograss.direction()
    #print("%s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    main()
