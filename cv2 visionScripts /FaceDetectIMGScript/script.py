import cv2

face_cascase = cv2.CascadeClassifier( "haarcascade_frontalface_default.xml" )       # creates a cascade classifier object
# can find other cascade classifier xmls at https://github.com/opencv/opencv/tree/master/data/haarcascades

img = cv2.imread( "news.jpg" )
gray_img = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY )

faces = face_cascase.detectMultiScale(
    gray_img , 
    scaleFactor = 1.05 ,    # 5%. Smaller value is higher curiosity. 50% or 1.50 is less curious. 
    minNeighbors = 3 )    

for x , y , w , h in faces:
    img = cv2.rectangle(                # draw rectagle arround face
        img , 
        ( x , y ) ,                     # starting point. From top left corner to start of rectangle
        ( ( x + w ) , ( y + h ) ) ,     # starting point x + wigth , starting point y + height 
        ( 0 , 255 , 0 ) ,               # green  
        3 )                             # width

print( type(faces) )
print( faces )

scale = 3
scaledWidth = round( int(img.shape[1]) / scale )    # img.shape is ( height , width )
scaledHeight = round( int(img.shape[0]) / scale )

resized_image = cv2.resize( img , ( scaledWidth , scaledHeight ) )

cv2.imshow( "Grey" , resized_image )
cv2.waitKey( 4000 )
cv2.destroyAllWindows()

