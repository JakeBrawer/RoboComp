from kovan import *

import sys
#sys.path.insert(0, '/Users/nb/desktop/RoboComp/Sensorimotor')
from camera_code import calculateStdError
import math

#numbers of the IR sensors
IR_left = 3
IR_right = 5
IR_front = 0

# ports for bump sensors
bump_left = 14
bump_right = 15

#numbers of motor ports
motor_left = 3
motor_right = 1

mid_thresh = 420

#expected_left, expected_right, expected_front = 0


def sigmoid(array , deriv=False):
    if(deriv==True):
        return array*(1-array)
    return 1/(1+numpy.exp(-array))

class Expected:
	def __init__(self):
		self.left_avg = 0
		self.right_avg = 0
		self.front_avg = 0
		self.left_samples = []
		self.right_samples = []
		self.front_samples = []
		self.left_err = 0
		self.right_err = 0
		self.front_err = 0
		
	def calculateStdError(self, list_of_vals, average):
		stddev = 0.0
		diffsquared = 0.0
		sum_diffsquared = 0.0
		#need to initialize stderror before?
		for val in list_of_vals:
			diffsquared = (val- average)**2.0
			sum_diffsquared += diffsquared 
		stddev = math.sqrt((sum_diffsquared)/len(list_of_vals))
		stderror = stddev / math.sqrt(len(list_of_vals))
		return stderror
	
	def update(self, IR_left, IR_right, IR_front):
		self.left_samples.append(IR_left)
		self.right_samples.append(IR_right)
		self.front_samples.append(IR_front)
		
		self.left_avg = sum(self.left_samples)/len(self.left_samples)
		self.right_avg = sum(self.right_samples)/len(self.right_samples)
		self.front_avg = sum(self.front_samples)/len(self.front_samples)
		
		self.left_err = self.calculateStdError(self.left_samples, self.left_avg)
		self.right_err = self.calculateStdError(self.right_samples, self.right_avg)
		self.front_err = self.calculateStdError(self.front_samples, self.front_avg)
		
	def checks_out(self, IR_left, IR_right, IR_front):
		arr = [True, True, True]
		if (IR_left < (self.left_avg - self.left_err)):
				arr[0] = False
		if (IR_right < (self.right_avg - self.right_err)):
				arr[1] = False
		if ((IR_front > (self.front_avg + self.front_err)) or (IR_front < (self.front_avg - self.front_err))):
				arr[2] = False
		return arr
		
	def printer(self):
		print "self.left_avg ", self.left_avg
		print "self.left_err ", self.left_err
		print "self.right_avg ", self.right_avg
		print "self.right_err ", self.right_err
		print "self.front_avg ", self.front_avg
		print "self.front_err ", self.front_err
				
class localExpector:
	def __init__(self, drop_rate):
		self.left_avg = 0
		self.right_avg = 0
		self.front_avg = 0
		self.left_samples = []
		self.right_samples = []
		self.front_samples = []
		self.left_err = 0
		self.right_err = 0
		self.front_err = 0
		
		self.drop_rate = drop_rate
		
	def calculateStdError(self, list_of_vals, average):
		stddev = 0.0
		diffsquared = 0.0
		sum_diffsquared = 0.0
		#need to initialize stderror before?
		for val in list_of_vals:
			diffsquared = (val- average)**2.0
			sum_diffsquared += diffsquared 
		stddev = math.sqrt((sum_diffsquared)/len(list_of_vals))
		stderror = stddev / math.sqrt(len(list_of_vals))
		return stderror
	
	def update(self, IR_left, IR_right, IR_front):
		self.left_samples.append(IR_left)
		self.right_samples.append(IR_right)
		self.front_samples.append(IR_front)
		if (len(self.left_samples) >= self.drop_rate):
			self.left_samples.pop(0)
			self.right_samples.pop(0)
			self.front_samples.pop(0)
		
		self.left_avg = sum(self.left_samples)/len(self.left_samples)
		self.right_avg = sum(self.right_samples)/len(self.right_samples)
		self.front_avg = sum(self.front_samples)/len(self.front_samples)
		
		self.left_err = self.calculateStdError(self.left_samples, self.left_avg)
		self.right_err = self.calculateStdError(self.right_samples, self.right_avg)
		self.front_err = self.calculateStdError(self.front_samples, self.front_avg)
		
	def checks_out(self, IR_left, IR_right, IR_front):
		arr = [True, True, True]
		if (IR_left < (self.left_avg - self.left_err)):
				arr[0] = False
		if (IR_right < (self.right_avg - self.right_err)):
				arr[1] = False
		if ((IR_front > (self.front_avg + self.front_err)) or (IR_front < (self.front_avg - self.front_err))):
				arr[2] = False
		return arr
	
	def printer(self):
		print "self.left_avg ", self.left_avg
		print "self.left_err ", self.left_err
		print "self.right_avg ", self.right_avg
		print "self.right_err ", self.right_err
		print "self.front_avg ", self.front_avg
		print "self.front_err ", self.front_err

def stay_mid():
	
	left_IR_val = analog_et(IR_left)
	right_IR_val = analog_et(IR_right)
	print('Left IR: %s,  Right IR: %s' % (left_IR_val, right_IR_val))
	
	#how we found this constant:
	#we want the IR val of 400 to produce a speed of 70 (for forward motion), so
	#70x = 400
	#-> x = 400/70 = .175
	CONST = .175
	right = right_IR_val * CONST
	left = left_IR_val * CONST
	
	CAP = 90
	#cap our outputs at the cap
	if (right > CAP):
		right = CAP
	if (left > CAP):
		left = CAP
	
	motor(motor_right,int(right))
	motor(motor_left,int(left))
   

def bump():
    global bump_left,bump_right
    left_bump = analog_et(bump_left)
    right_bump = analog_et(bump_right)
    if left_bump == 1:
        #Move back for a bit
        motor(motor_left, 60)
        motor(motor_right, 60)
        msleep(800)
        # Turn towards the right
        motor(motor_right, -60)
        msleep(600)
    if right_bump == 1:
        #Move back for a bit
        motor(motor_left, 60)
        motor(motor_right, 60)
        msleep(800)
        # Turn towards the right
        motor(motor_left, -60)
        msleep(600)
