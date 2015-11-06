#!/usr/bin/env python

import sys
import termios
import tty
import os

from move_control import MoveControl


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def update_print_screen(move_control):
    os.system('clear')
    print("w/s: direction")
    print("a/d: steering")
    print("q: stops the motors")
    print("x: exit")
    print("========== Speed Control ==========")
    print "left motor:  ", move_control.speedleft
    print "right motor: ", move_control.speedright


if __name__ == "__main__":

    print("w/s: direction")
    print("a/d: steering")
    print("y/c: rotate")
    print("q: stops the motors")
    print("p: print motor speed (L/R)")
    print("x: exit")

    run = True
    move_control = MoveControl()

    while run:
        char = getch()

        if char == "w":
            move_control.move_foward()
        elif char == "s":
            move_control.move_backward()
        elif char == "a":
            move_control.move_left()
        elif char == "d":
            move_control.move_right()
        elif char == "y":
            move_control.rotate_left()
        elif char == "c":
            move_control.rotate_right()
        elif char == "q":
            move_control.stop_move()
        elif char == "x":
            run = False
            move_control.exit()
