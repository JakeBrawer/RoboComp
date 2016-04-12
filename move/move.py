# Created on Fri February 19 2016

from kovan import *

#GO FORWARD
motor(1, 100)
motor(3, 100)

#WAIT 4 SECONDS
msleep(2500)

#A LITTLE TO THE RIGHT
motor(1, 100)
motor(3, -100)

#WAIT 1 SECOND
msleep(1000)

#A LITTLE TO THE LEFT
motor(1, -100)
motor(3, 100)

#WAIT 1 SECOND
msleep(1000)

#STOP
motor(1, 0)
motor(3, 0)
