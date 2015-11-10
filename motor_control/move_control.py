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
        self.set_speed(0.0, 0.0)

    def move_foward(self):
        limit_left = 0.8
        limit_right = 0.8

        increment_left = 0.05
        increment_right = 0.05

        self.update_speed(increment_left, increment_right, limit_left,
                          limit_right)

    def move_backward(self):
        limit_left = -0.8
        limit_right = -0.8

        increment_left = -0.05
        increment_right = -0.05

        self.update_speed(increment_left, increment_right, limit_left,
                          limit_right)

    def move_left(self):
        limit_left = -0.4
        limit_right = 0.8

        increment_left = -0.05
        increment_right = 0.05

        self.update_speed(increment_left, increment_right, limit_left,
                          limit_right)

    def move_right(self):
        limit_left = 0.8
        limit_right = -0.4

        increment_left = 0.05
        increment_right = -0.05

        self.update_speed(increment_left, increment_right, limit_left,
                          limit_right)

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def set_speed(self, speed_left, speed_right):
        self.speed_left = speed_left
        self.speed_right = speed_right

        base_control.setMotorLeft(self.speed_left)
        base_control.setMotorRight(self.speed_right)

    def update_speed(self, increment_left, increment_right, limit_left,
                     limit_right):
        self.speed_left = self.speed_left + increment_left
        self.speed_right = self.speed_right + increment_right

        if abs(self.speed_left) > abs(limit_left):
            self.speed_left = limit_left

        if abs(self.speed_right) > abs(limit_right):
            self.speed_right = limit_right

        base_control.setMotorLeft(self.speed_left)
        base_control.setMotorRight(self.speed_right)
