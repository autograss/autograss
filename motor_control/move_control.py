#!/usr/bin/env python

import base_control
import logging


STOP_MOVE = "stop_move"
MOVE_FOWARD = "move_foward"
MOVE_BACKWARD = "move_backward"
MOVE_LEFT = "move_left"
MOVE_RIGHT = "move_right"
ROTATE_LEFT = "rotate_left"
ROTATE_RIGHT = "rotate_right"


def move(direction):
    if direction == STOP_MOVE:
        stop_move()
    elif direction == MOVE_LEFT:
        move_left()
    elif direction == MOVE_RIGHT:
        move_right()
    elif direction == MOVE_LEFT:
        move_left()
    elif direction == ROTATE_LEFT:
        rotate_left()
    elif direction == ROTATE_RIGHT:
        rotate_right()


def stop_move():
    speed_left = 0.0
    speed_right = 0.0

    update_speed(speed_left, speed_right)


def move_foward():
    speed_left = -0.8
    speed_right = -0.8

    update_speed(speed_left, speed_right)


def move_backward():
    speed_left = 0.8
    speed_right = 0.8

    update_speed(speed_left, speed_right)


def move_left():
    speed_left = -0.4
    speed_right = -0.7

    update_speed(speed_left, speed_right)


def move_right():
    speed_right = -0.4
    speed_left = -0.7

    update_speed(speed_left, speed_right)


def rotate_left():
    speed_left = 0
    speed_right = -0.8

    update_speed(speed_left, speed_right)


def rotate_right():
    speed_left = -0.8
    speed_right = -0

    update_speed(speed_left, speed_right)


def update_speed(speed_left, speed_right):
    logging.info("speed_left: speed_left")
    logging.info("speed_right: speed_right")

    base_control.setMotorLeft(speed_left)
    base_control.setMotorRight(speed_right)
