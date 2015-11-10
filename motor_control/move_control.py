#!/usr/bin/env python

import base_control


class MoveControl:
    STOP_MOVE = "stop_move"
    MOVE_FORWARD = "move_forward"
    MOVE_BACKWARD = "move_backward"
    MOVE_LEFT = "move_left"
    MOVE_RIGHT = "move_right"
    ROTATE_LEFT = "rotate_left"
    ROTATE_RIGHT = "rotate_right"

    def __init__(self):
        self.speed_left = 0
        self.speed_right = 0

    def move(self, direction):
       	if direction == self.STOP_MOVE:
           self.stop_move()
      	elif direction == self.MOVE_LEFT:
           self.move_left()
       	elif direction == self.MOVE_RIGHT:
           self.move_right()
       	elif direction == self.MOVE_FORWARD:
           self.move_forward()
       	elif direction == self.ROTATE_LEFT:
           self.rotate_left()
       	elif direction == self.ROTATE_RIGHT:
           self.rotate_right()
	elif direction == self.MOVE_BACKWARD:
	   self.move_backward()

    def exit(self):
        self.stop_move()
        base_control.exit()

    def stop_move(self):
        self.speed_left = 0.0
        self.speed_right = 0.0

        self.update_speed()

    def move_forward(self):
        self.speed_left = 0.8
        self.speed_right = 0.8

        self.update_speed()

    def move_backward(self):
        self.speed_left =  - 0.8
        self.speed_right = - 0.8

        self.update_speed()

    def move_left(self):
        self.speed_left = -0.0
        self.speed_right = 0.8

        self.update_speed()

    def move_right(self):
        self.speed_right = - 0.0
        self.speed_left = 0.8

        self.update_speed()

    def rotate_left(self):
        self.speed_left = 0
        self.speed_right = 0.8

        self.update_speed()

    def rotate_right(self):
        self.speed_left = 0.8
        self.speed_right = 0

        self.update_speed()

    def update_speed(self):
        print self.speed_left
        print self.speed_right
        base_control.setMotorLeft(self.speed_left)
        base_control.setMotorRight(self.speed_right)
