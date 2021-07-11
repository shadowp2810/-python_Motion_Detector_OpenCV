import cv2, time

# video = cv2.VideoCapture( "movie.mp4" )
video = cv2.VideoCapture( 0 )

numFramesRecorded = 0

while True:
    numFramesRecorded = numFramesRecorded + 1
    check , frame = video.read()        # check is boolean data type and frame is numpy array

    print( check )
    print( frame )

    grey = cv2.cvtColor( frame , cv2.COLOR_BGR2GRAY ) # turn frame into greyscale
        # time.sleep( 3 )     # captures footage for 3 seconds, used if not using loop
    cv2.imshow( "Capturing" , grey )
        # cv2.waitKey( 0 )    # press 0 key to exit window , for wait by ms enter eg: 3000 for 3sec
    key = cv2.waitKey( 1 ) 
    
    if key == ord( 'q' ):       # press q key to exit
        break
    

print( "Num of frames recorded: %s" % ( numFramesRecorded ) )
video.release()
cv2.destroyAllWindows
