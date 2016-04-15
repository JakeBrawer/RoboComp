from kovan import *

import sys
sys.path.insert(0, '/Users/nb/desktop/RoboComp/Sensorimotor')
from camera_code import calculateStdError

#numbers of the IR sensors
IR_left = 3
IR_right = 5
IR_front = 0

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
		if ((IR_left > (self.left_avg + self.left_err)) or 
			(IR_left < (self.left_avg - self.left_err)):
				arr[0] = False
		if ((IR_right > (self.right_avg + self.right_err)) or 
			(IR_right < (self.right_avg - self.right_err)):
				arr[1] = False
		if ((IR_front > (self.front_avg + self.front_err)) or 
			(IR_front < (self.front_avg - self.front_err)):
				arr[2] = False
		return arr
				

def stay_mid():
	#put in da sigmoid func. (how do you do sigmoid)
	#S(z) = 1/(1+e^-z) #math
	# ok so we input the ir values as the x values and that spits out y values that never go above or below a certain value. Why do we want that? Because we dont want our ir sensor values to go above or below a certain value so this limits them with an asymptote. We also want the motor to be very reactive. ooooh wait ok the y values will be the motor output? So ok wait. 
	
	#motor(motor_right, (expit(left_IR_val)))
	#motor(motor_left, (expit(right_IR_val)))
	
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
   

