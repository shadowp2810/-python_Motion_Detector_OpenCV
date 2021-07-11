import cv2 

imgG = cv2.imread( "galaxy.jpg" , 0 ) # 1 to read as is. 0 to read in b&w. -1 for color with transperency. 

print( type( imgG ) )    # <class 'numpy.ndarray'>
print( imgG )            # 
                        # [[14 18 14 ... 20 15 16]
                        #  [12 16 12 ... 20 15 17]
                        #  [12 13 16 ... 14 24 21]
                        #  ...
                        #  [ 0  0  0 ...  5  8 14]
                        #  [ 0  0  0 ...  2  3  9]
                        #  [ 1  1  1 ...  1  1  3]]
                        #
print( imgG.shape )      # (1485, 990) 1495 by 990
print( imgG.ndim )       # 2 dimensions

imgC = cv2.imread( "galaxy.jpg" , 1 ) # 1 to read as is in color. 0 to read in b&w. -1 for color with transperency. 

print( type( imgC ) )   # <class 'numpy.ndarray'>
print( imgC )           # 
                        # [[[19 15 10]
                        #   [23 19 14]
                        #   [21 15  8]
                        #   ...
                        #   [27 22 13]
                        #   [22 17  8]
                        #   [23 18  9]]

                        #  [[17 13  8]
                        #   [21 17 12]
                        #   [19 13  6]
                        #   ...
                        #   [27 22 13]
                        #   [22 17  8]
                        #   [24 19 10]]

                        #  [[17 14  6]
                        #   [18 15  7]
                        #   [21 18 10]
                        #   ...
                        #   [23 16  7]
                        #   [33 26 17]
                        #   [30 23 14]]

                        #  ...

                        #  [[ 0  0  0]
                        #   [ 0  0  0]
                        #   [ 0  0  0]
                        #   ...
                        #   [ 5  5  5]
                        #   [ 8  8  8]
                        #   [14 14 14]]

                        #  [[ 0  0  0]
                        #   [ 0  0  0]
                        #   [ 0  0  0]
                        #   ...
                        #   [ 2  2  2]
                        #   [ 3  3  3]
                        #   [ 9  9  9]]

                        #  [[ 1  1  1]
                        #   [ 1  1  1]
                        #   [ 1  1  1]
                        #   ...
                        #   [ 1  1  1]
                        #   [ 1  1  1]
                        #   [ 3  3  3]]]
print( imgC.shape[0] )      # (1485, 990, 3) 1495 by 990
print( imgC.ndim )       # 3 dimensions

halfWidth = round( int(imgG.shape[1]) / 2 )
halfHeight = round( int(imgG.shape[0]) / 2 )

resized_image = cv2.resize( imgG , ( halfWidth , halfHeight ) )     # resizes the numpy array # ( width , height )
cv2.imshow( "galaxy" , resized_image )
cv2.imwrite( "galaxy_resized_half.jpg" , resized_image )
cv2.waitKey( 4000 )
cv2.destroyAllWindows()



