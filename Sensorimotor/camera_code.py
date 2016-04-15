import math
#import numpy
from kovan import *

average_black_blob = 0
stderr_black_blob = 0
black_channel = 0 #

def calculateStdError(list_of_vals, average):
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

def calculateBlackBlobs():
    # These are global variables that this func will modify
    global average_black_blob, stderr_black_blob
    print("no camera")
    #camera_open_at_res(LOW_RES)
    print("camera open")
    # Will store a list of num_samples averages
    # Will themselves be averaged to calculate final mean
    average_black_blobs_list = []
    num_samples = 5 # Num snapshots we will use to calculate blob stats
    for j in range(num_samples):
        print("camera_update()....")
        camera_update()# Take a snapshot
        # Counts the number of black blobs seen in snapshot
        object_count = get_object_count(0)
        if object_count > 0:
			print "OBJECT COUNT: ", object_count
			# Stores sums to calculates averages
			sum_area_black_blobs = 0
			#loops through each blob detected and calculates area
			for i in range(0, object_count):
				sum_area_black_blobs += get_object_area(black_channel, i)
			# calculates and stores average total area takwn up by blobs
			if (not (object_count == 0)):
				average_black_blobs_list.append(sum_area_black_blobs/ object_count)
			else: 
				print "NO OBJECTS!"
			#Sleep for 1 second. Will allow the bot to move around the room
			# and take samples
			# NOTE: if sleep does not work, try wheel ticks
			print "Average black blobs in sample", average_black_blobs_list
			msleep(1000)
    if (not (len(average_black_blobs_list) == 05)):
        average_black_blob = sum(average_black_blobs_list)/float(len(average_black_blobs_list))
        stderr_black_blob = calculateStdError(average_black_blobs_list, average_black_blob) 
        #camera_close()
        return average_black_blob, stderr_black_blob
    else:
        #camera_close()
        return 0, 0
>>>>>>> e2f6272c360a8576c705c467fe5305ab568289d4


#print ("Average saved black blob: %s\nStd err: %s " %  (average_black_blob, stderr_black_blob))
