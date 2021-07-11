import cv2 , time , pandas
from datetime import datetime

first_frame = None

status_list = [ None , None ]        # list of active moving or not moving objects
times = []              # to record times of active detected moving objects
df = pandas.DataFrame( columns = [ "Start" , "End" ] )      # Data Frame

video = cv2.VideoCapture( 0 )

numFramesRecorded = 0
time.sleep( 2 )

while True:
    numFramesRecorded = numFramesRecorded + 1
    check , frame = video.read()        # check is boolean data type and frame is numpy array
    status = 0      # to denote there is no motion in current frame       
    # print( check )
    # print( frame )
                                       
    grey = cv2.cvtColor( frame , cv2.COLOR_BGR2GRAY )     # turn frame into greyscale
    grey = cv2.GaussianBlur( grey , ( 21 , 21 ) , 0 )     # to remove noice and increase accuracy for later calculation of difference 
                                                          # (21,21) are parameters of bluriness , 0 is standard devation
    if first_frame is None:
        first_frame = grey      # When script is first run gets a frame
                                # first frame in first loop is made greyscale
                                # first_grame is no longer none
                                # condition execution only needed for first frame 
        continue                # continues to begining of loop as below is not needed for first frame

    delta_frame = cv2.absdiff( first_frame , grey )

    threshold_frame = cv2.threshold( delta_frame , 30 , 255 , cv2.THRESH_BINARY )[1]
    
    threshold_frame = cv2.dilate( threshold_frame , None , iterations = 2 )      # for contours. # Higher the iterations, the smoother the image will be
    
    ( cnts , _ ) = cv2.findContours( threshold_frame.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE )      # To find all countours

    for contour in cnts:
        if cv2.contourArea( contour ) < 10000 :     # larger means to detect bigger objects
            continue
        
        status = 1      # to denote there is a motion in current frame
        
        ( x , y , w , h ) = cv2.boundingRect( contour )
        cv2.rectangle( 
                frame , 
                ( x , y ) , 
                ( x + w , y + h ) ,
                ( 0 , 255 , 0 ) ,
                3 )
    
    status_list.append( status )
    
    status_list = status_list[-2:]      # saving memory by only keeping last 2 values in list

    if status_list[ -1 ] == 1 and status_list[ -2 ] == 0 :      # when status changes from 0 to 1 eg: [0 , 0 , 1 ]
        times.append( datetime.now() )
    if status_list[ -1 ] == 0 and status_list[ -2 ] == 1 :      # when status changes from 1 to 0 eg: [1 , 1 , 0 ]
        times.append( datetime.now() )
    
    cv2.imshow( "Grey Frame" , grey )
    cv2.imshow( "Delta Frame" , delta_frame )
    cv2.imshow( "Threshold Frame" , threshold_frame )
    cv2.imshow( "Color Frame" , frame )

    key = cv2.waitKey( 1 ) 
    
    if key == ord( 'q' ):       # press q key to exit
        if status == 1 :
            times.append( datetime.now() )      # to record an end time for when window is closed
        break
    
    
print( status_list )
print( times )

for i in range( 0 , len(times) , 2 ) :      # 0 to len(times) with step of 2
    df = df.append( {                        
            "Start" : times[ i ] , 
            "End" : times[ i + 1 ] } , 
        ignore_index = True )               # every row gets start and end time. 
                                            # first loop i=1, second loop i=3 as step of 2
    
df.to_csv( "Times.csv" )

print( "Num of frames recorded: %s" % ( numFramesRecorded ) )
video.release()
cv2.destroyAllWindows
