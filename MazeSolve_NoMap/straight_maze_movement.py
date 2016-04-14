from kovan import *
from scipy.special import expit

#numbers of the IR sensors
IR_left = 3
IR_right = 5
IR_front = 0

#numbers of motor ports
motor_left = 3
motor_right = 1

mid_thresh = 420
front_IR_val = analog_et(IR_front)

def sigmoid(array , deriv=False):
    if(deriv==True):
        return array*(1-array)
    return 1/(1+np.exp(-array))

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
   

'''
while(True):
    motor(motor_right, 70)
    motor(motor_left, 70)
    stay_mid()
'''
