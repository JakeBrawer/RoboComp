# Created on Fri February 26 2016

from kovan import *

#numbers of the IR sensors
IR_left = 0
IR_right = 1

#numbers of motor ports
motor_left = 1
motor_right = 3

#threshold for the IR sensors
IR_thresh = 500

#number of milliseconds between each loop
tic = 50

while(True):
	msleep(tic)
	if analog10(IR_left) > thresh:
		turn_right()
	elif analog10(IR_right) > thresh:
		turn_left()
	else:
		fwd()
	
def fwd():
	motor(motor_left, 100)
	motor(motor_right, 100)
	
def turn_right(in_place=True):
	motor(motor_left, 100)
	motor(motor_right, -100)

def turn_left(in_place=True):
	motor(motor_left, -100)
	motor(motor_right, 100)
