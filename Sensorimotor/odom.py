#odom.py

from kovan import *

class Odometry:
	def __init__(self, motor_left_num, motor_right_num, front_IR):

		self.motor_left = motor_left_num
		self.motor_right = motor_right_num
		self.front_IR = front_IR
		self.last_dist = False
		self.distance_traveled = 0
		self.last_rot = 0

		
		#clear motors
		clear_motor_position_counter(motor_left)
		clear_motor_position_counter(motor_right)

	def get_num_rotations(self, mot_num):
		ticks_to_rotations = 1100.0 #according to LINK manual, but let's tune this
		return (get_motor_position_counter(mot_num)/ticks_to_rotations)

	def update(self):
		rot_left = self.get_num_rotations(self.motor_left)
		rot_right = self.get_num_rotations(self.motor_right)
		self.last_dist = analog(self.front_IR)
		self.last_rot = ((rot_left + rot_right)/2.0)

	#assumes relatively forward motion
	def diff_in_rotations(self):
		rot_left = self.get_num_rotations(self.motor_left)
		rot_right = self.get_num_rotations(self.motor_right)
		return (((rot_left + rot_right)/2.0) - self.last_rot)

	def estimate_IR_change(self):
		#we will need to tune this a lot/probably completely rewrite
		IR_per_rot = 10
		diff = self.diff_in_rotations()
		

