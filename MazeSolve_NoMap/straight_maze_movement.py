from kovan import *

#numbers of the IR sensors
IR_left = 3
IR_right = 5
IR_front = 0

#numbers of motor ports
motor_left = 3
motor_right = 1

mid_thresh = 420
front_IR_val = analog_et(IR_front)

def stay_mid():
    left_IR_val = analog_et(IR_left)
    right_IR_val = analog_et(IR_right)
    print('Left IR: %s,  Right IR: %s' % (left_IR_val, right_IR_val))
    #if(left_IR_val > mid_thresh ):
    motor(motor_right,70*(left_IR_val/800))
    #if(right_IR_val > mid_thresh):
    motor(motor_left,70*(right_IR_val/800))

'''
while(True):
    motor(motor_right, 70)
    motor(motor_left, 70)
    stay_mid()
'''
