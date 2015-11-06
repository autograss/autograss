#!/usr/bin/env python

import base_control
import logging


class MoveControl:
    STOP_MOVE = "stop_move"
    MOVE_FOWARD = "move_foward"
    MOVE_BACKWARD = "move_backward"
    MOVE_LEFT = "move_left"
    MOVE_RIGHT = "move_right"
    ROTATE_LEFT = "rotate_left"
    ROTATE_RIGHT = "rotate_right"

    def __init__(self):
        pass

    def move(self, direction):
        if direction == self.STOP_MOVE:
            self.stop_move()
        elif direction == self.MOVE_LEFT:
            self.move_left()
        elif direction == self.MOVE_RIGHT:
            self.move_right()
        elif direction == self.MOVE_LEFT:
            self.move_left()
        elif direction == self.ROTATE_LEFT:
            self.rotate_left()
        elif direction == self.ROTATE_RIGHT:
            self.rotate_right()

    def exit(self):
        self.stop_move()
        base_control.exit()

    def stop_move(self):
        speed_left = 0.0
        speed_right = 0.0

        self.update_speed(speed_left, speed_right)

    def move_foward(self):
        speed_left = -0.8
        speed_right = -0.8

        self.update_speed(speed_left, speed_right)

    def move_backward(self):
        speed_left = 0.8
        speed_right = 0.8

        self.update_speed(speed_left, speed_right)

    def move_left(self):
        speed_left = -0.4
        speed_right = -0.7

        self.update_speed(speed_left, speed_right)

    def move_right(self):
        speed_right = -0.4
        speed_left = -0.7

        self.update_speed(speed_left, speed_right)

    def rotate_left(self):
        speed_left = 0
        speed_right = -0.8

        self.update_speed(speed_left, speed_right)

    def rotate_right(self):
        speed_left = -0.8
        speed_right = -0

        self.update_speed(speed_left, speed_right)

    def update_speed(self, speed_left, speed_right):
        logging.info("speed_left: speed_left")
        logging.info("speed_right: speed_right")

        base_control.setMotorLeft(speed_left)
        base_control.setMotorRight(speed_right)
