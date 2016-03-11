# Created on Fri February 26 2016

from kovan import *
import camera_code

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
IR_thresh = 280

#number of milliseconds between each loop
tick = 50

speed = 85


def fwd():
	motor(motor_left, speed)
	motor(motor_right, speed)
	
def turn_right(in_place=True):
	#if in place, opposite motor goes backward
	if in_place:
		motor_right_vel = -1*speed
	else:
		motor_right_vel = 40
	motor(motor_left, speed)
	motor(motor_right, motor_right_vel)

def turn_left(in_place=True):
	if in_place:
		motor_left_vel = -1*speed
	else:
		motor_left_vel = 40
	motor(motor_left, motor_left_vel)
	motor(motor_right, speed)
	
camera_open_at_res(LOW_RES)
while(True):
	average_black_blob = 0
	stderr_black_blob = 0
	black_channel = 0 #
	average_black_blob, stderr_black_blob = camera_code.calculateBlackBlobs()
	print "av: ", average_black_blob
	print "std: ", stderr_black_blob
camera_close()

'''
while(True):
	#this variable indicates whether or not an action runs for a specific amount of time
	diff_time_for_action = False
	left = analog_et(IR_left)

	#if there's something left, turn right
	if left > IR_thresh:
		print "TURNING RIGHT! IR_LEFT: ", left 
		turn_right()
	#else if there's something right, turn left
	elif analog_et(IR_right) > IR_thresh:
		turn_left()
	#else go forward
	else:
		print "FORWARD!"
		fwd()
		
	#do selected action for tick num of milliseconds, unless the selected action
	#runs for a specific amount of time different than tick
	if not diff_time_for_action:
		msleep(tick)

'''
