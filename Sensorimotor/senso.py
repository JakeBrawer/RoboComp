# Created on Fri February 26 2016

from kovan import *

#numbers of the IR sensors
IR_left = 0
IR_right = 1
IR_fwd = 2

#numbers of motor ports
motor_left = 1
motor_right = 3

#clear motors
#clear_motor_position_counter(motor_left)
#clear_motor_position_counter(motor_right)

#threshold for the IR sensors
IR_thresh = 500

#number of milliseconds between each loop
tick = 50

while(True):
	#this variable indicates whether or not an action runs for a specific amount of time
	diff_time_for_action = False

	#if there's something left, turn right
	if analog10(IR_left) > thresh:
		turn_right()
	#else if there's something right, turn left
	elif analog10(IR_right) > thresh:
		turn_left()
	#else go forward
	else:
		fwd()
		
	#do selected action for tick num of milliseconds, unless the selected action
	#runs for a specific amount of time different than tick
	if not diff_time_for_action:
		msleep(tick)
	
def fwd():
	motor(motor_left, 100)
	motor(motor_right, 100)
	
def turn_right(in_place=True):
	#if in place, opposite motor goes backward
	if in_place:
		motor_right_vel = -100
	else:
		motor_right_vel = 40
	motor(motor_left, 100)
	motor(motor_right, motor_right_vel)

def turn_left(in_place=True):
	if in_place:
		motor_left_vel = -100
	else:
		motor_left_vel = 40
	motor(motor_left, motor_left_vel)
	motor(motor_right, 100)
