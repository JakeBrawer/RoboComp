# Created on Thu March 31 2016

from kovan import *
import straight_maze_movement as jake

#numbers of the IR sensors
IR_left = 5
IR_right = 3
IR_front = 0

#numbers of motor ports
motor_left = 3
motor_right = 1


IR_normalize = 0
IR_diff_thresh = 40
IR_thresh_collision = 480
IR_thresh_wall = 300
front_IR_thresh = 430#420

speed = 60
speed_right = 63
speed_left = 73

#number of milliseconds between each loop
tick = 30

	
nudge_dec = 20
nudge_inc = 0

		
###### SENSOR PREDICATE FUNCTIONS ######
def something_front(front_val):
	return front_val > front_IR_thresh
def collision_side(val):
	return val > IR_thresh_collision
def wall_side(val):
	return val > IR_thresh_wall

###### MOTOR BEHAVIORS (NO SET AMT OF TIME) #######
def fwd():
	motor(motor_left, speed_left)
	motor(motor_right, speed_right)
def nudge_right():
	motor(motor_left, speed_left+nudge_inc)
	motor(motor_right, speed_right-nudge_dec)
def nudge_left():
	motor(motor_left, speed_left-nudge_dec)
	motor(motor_right, speed_right+nudge_inc)
def turn_right(in_place=True):
	#if in place, opposite motor goes backward
	if in_place:
		motor_right_vel = -1*speed_right
	else:
		motor_right_vel = 40
	motor(motor_left, speed_left)
	motor(motor_right, motor_right_vel)
def turn_left(in_place=True):
	if in_place:
		motor_left_vel = -1*speed
	else:
		motor_left_vel = 40
	motor(motor_left, motor_left_vel)
	motor(motor_right, speed)
def stop_left():
	motor(motor_left, 0)
	motor(motor_right, speed_right-5)
def stop_right():
	motor(motor_right, 0)
	motor(motor_left, speed_left-5)
def stop():
	motor(motor_left, 0)
	motor(motor_right, 0)
def wobble_fwd(left_IR_val, right_IR_val, front_IR_val):
	if (left_IR_val > IR_thresh_collision):
		print "Nudge right"
		stop_left()
	elif (right_IR_val > IR_thresh_collision):
		print "Nudge left"
		stop_right()
	else:
		#if we're about to hit a wall from the front, stop
		if (front_IR_val > front_IR_thresh):
			turn_right()
		else:
			fwd()

##### MOTOR BEHAVIORS (SET AMT OF TIME) ######
def one_eighty():
	turn_left()
	msleep(1200)
	stop()

motor_out_left = 0
motor_out_right = 0
expector = jake.Expected()
counter = 0
arr = [True, True, True]
##### MAIN LOOP! ##########
while(True):
	counter += 1
	arr = [True, True, True]
	#read the sensor vals
	
	front_IR_val = analog_et(IR_front)
	left_IR_val = analog_et(IR_left)
	right_IR_val = analog_et(IR_right)
	expector.update(left_IR_val, right_IR_val, front_IR_val)
	'''
	if (something_front(front_IR_val) and wall_side(left_IR_val) 
			and wall_side(right_IR_val)):
				print "DEAD END"
				one_eighty()
	else:
		wobble_fwd(left_IR_val, right_IR_val, front_IR_val)
	'''
	if (something_front(front_IR_val) and wall_side(left_IR_val) 
			and wall_side(right_IR_val)):
				print "DEAD END"
				one_eighty()
	else:
		#motor(motor_right, 70)
		#motor(motor_left, 70)
		#if we're about to hit a wall from the front, stop
		if (front_IR_val > front_IR_thresh):
			print "SOMETHING FRONT"
			turn_right()
		else:
			if (counter > 5):
				arr = expector.checks_out(left_IR_val, right_IR_val, front_IR_val)
			print "STAY MID"
			if (not arr[0]):
				turn_left()
				msleep(100)
				fwd()
				msleep(100)
			elif (not arr[1]):
				turn_right()
				msleep(100)
				fwd()
				msleep(100)
			else:
				jake.stay_mid()
	if (a_button() or b_button() or c_button()):
		ao()
		break
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
