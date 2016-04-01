# Created on Thu March 31 2016

from kovan import *

#numbers of the IR sensors
IR_left = 3
IR_right = 5
IR_front = 0

#numbers of motor ports
motor_left = 3
motor_right = 1

#threshold for the IR sensors
IR_thresh = 280
front_IR_thresh = 420
left_IR_threshold = analog_et(IR_left)
right_IR_threshold = analog_et(IR_right)


speed = 60
speed_right = 55
speed_left = 55

#number of milliseconds between each loop
tick = 50

def fwd():
	motor(motor_left, speed_left)
	motor(motor_right, speed_right)
	
nudge_dec = 20
nudge_inc = 0
def nudge_right():
	motor(motor_left, speed_left+nudge_inc)
	motor(motor_right, speed_right-nudge_dec)
def nudge_left():
	motor(motor_left, speed_left-nudge_dec)
	motor(motor_right, speed_right+nudge_inc)
	
def stop():
	motor(motor_left, 0)
	motor(motor_right, 0)

IR_normalize = 0
IR_diff_thresh = 40

'''
#added stuff
if motor_left == 0 and motor_right == 0 and not stop():
	right_IR_threshold = right_IR_val
	print "right_IR_threshold: ", right_IR_threshold
	left_IR_threshold = left_IR_val
	print "left_IR_threshold: ", left_IR_threshold

init_left_IR = analog_et(IR_left)
init_right_IR = analog_et(IR_right)
init_IR_diff = init_left_IR - init_right_IR
print "left_ir init ", init_left_IR
print "right_ir init ", init_right_IR
print "init_ir_diff ", init_IR_diff
'''

while(True):
	#read the sensor vals
	front_IR_val = analog_et(IR_front)
	left_IR_val = analog_et(IR_left)
	right_IR_val = analog_et(IR_right)

	#if we're about to hit a wall from the front, stop
	if (front_IR_val > front_IR_thresh):
		stop()

	else:
		'''
		#added stuff
		if (right_IR_val > right_IR_threshold):
			nudge_left()
			print "Nudge left"
		elif (left_IR_val > left_IR_threshold) :
			nudge_right()
			print "Nudge right"
		else:
			fwd()
		'''
		IR_diff = (right_IR_val - IR_normalize) - left_IR_val
		
		#print "left ir: ", left_IR_val
		#print "right ir: ", right_IR_val
		#print "IR_diff: ", IR_diff
		
		if (IR_diff < (init_IR_diff + (-1*IR_diff_thresh))):
			print "Nudge right"
			nudge_right()
		elif (IR_diff > (init_IR_diff + IR_diff_thresh)):
			print "Nudge left"
			nudge_left()
			
		
		
	msleep(tick)

'''
pseudocode:
go straight until either
1. one of the side IRs cuts out
2. the front IR has a low reading
	then 
	turn and look (is there the goal?)
	record the direction you turned to go down this way
	if it's a dead end, then 
		turn the same direction you turned to get in to get in, so if 
		you turned left to enter, turn left to exit. this insures you will
		go a new direction each time (??)
'''
