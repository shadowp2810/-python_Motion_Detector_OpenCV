import cv2
import glob

images = glob.glob("*.jpg")     # creates a list of filenames with a path

for image in images:
    img = cv2.imread( image , 0 )
    re = cv2.resize( img , ( 100 , 100 ) )      # ( width , height )
    cv2.imshow( "Hey" , re )
    cv2.waitKey( 500 )
    cv2.destroyAllWindows()
    cv2.imwrite( "exported_images/resized_" + image + ".jpg" , re )

    