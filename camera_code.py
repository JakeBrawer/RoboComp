import math

average_black_blob = 0
stderr_black_blob = 0
black_channel = 0 #

def calculateStdError(list_of_vals, average):
    stddev = 0.0
    diffsquared = 0.0
    sum_diffsquared = 0.0
    for val in list_of_vals:
        diffsquared = (val- average)**2.0
        sum_diffsquared += diffsquared 
    stddev = math.sqrt((sum_diffsquared)/len(list_of_vals))
    stderror = stddev / math.sqrt(len(list_of_vals))
    return stderror

def calculateBlackBlobs():
    # These are global variables that this func will modify
    global average_black_blob, stderr_black_blob
    camera_open(LOW_RES)
    # Will store a list of num_samples averages
    # Will themselves be averaged to calculate final mean
    average_black_blobs_list = []
    num_samples = 5 # Num snapshots we will use to calculate blob stats
    while(num_samples > 0):
        camera_update()# Take a snapshot
        # Counts the number of black blobs seen in snapshot
        object_count = get_object_count(black_channel)
        # Stores sums to calculates averages
        sum_area_black_blobs = 0
        #loops through each blob detected and calculates area
        for i in range(0, object_count):
            sum_area_black_blobs += get_object_area(black_channel, i)
        # calculates and stores average total area takwn up by blobs
        average_black_blobs.append(sum_area_black_blobs/ object_count)
        num_samples -= 1
        #Sleep for 1 second. Will allow the bot to move around the room
        # and take samples
        # NOTE: if sleep does not work, try wheel ticks
        print "Average black blobs in sample", average_black_blobs_list
        msleep(1000)
    average_black_blob = sum(average_black_blobs_list)/float(len(average_black_blobs_list))
    stderr_black_blob = calculateStdError(average_black_blobs_list, average_black_blob)

print ("Average saved black blob: %s\nStd err: %s " %  (average_black_blob, stderr_black_blob)) 
