from kovan import *
import sys
from scipy.special import expit
sys.path.insert(0, '/home/jake/org/classes/RoboComp/Sensorimotor')
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
        return 1/(1+np.exp(-array))

def calculate_expected_vals(num_samples):
        left_samples =[]
        right_samples = []
        front_samples = []
        while(num_samples > 0):
                left_samples.append(analog_et(IR_left))
                right_samples.append(analog_et(IR_right))
                front_samples.append(analog_et(IR_front))
                msleep(200)
                num_samples -= 1
        left_avg = sum(left_samples)/len(left_samples)
        right_avg = sum(right_samples)/len(right_samples)
        front_avg = sum(front_samples)/len(front_samples)
        return {"expected left": [left_avg, calculateStdError(left_samples, left_avg)],
                     "expected right": [right_avg, calculateStdError(right_samples, right_avg)],
                     "expected front":[front_avg, calculateStdError(front_samples, front_avg)] }
def stay_mid():
	#put in da sigmoid func. (how do you do sigmoid)
	#S(z) = 1/(1+e^-z) #math
	# ok so we input the ir values as the x values and that spits out y values that never go above or below a certain value. Why do we want that? Because we dont want our ir sensor values to go above or below a certain value so this limits them with an asymptote. We also want the motor to be very reactive. ooooh wait ok the y values will be the motor output? So ok wait. 
	
        motor(motor_right, (expit(left_IR_val)))
        motor(motor_left, (expit(right_IR_val)))

        left_IR_val = analog_et(IR_left)
        right_IR_val = analog_et(IR_right)
        print('Left IR: %s,  Right IR: %s' % (left_IR_val, right_IR_val))
        #if(left_IR_val > mid_thresh ):
        motor(motor_right,70*(left_IR_val/500))
        #if(right_IR_val > mid_thresh):
        motor(motor_left,70*(right_IR_val/500))
   

