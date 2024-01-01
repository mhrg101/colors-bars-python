import cv2
import numpy
def nothing(x):
    pass
  
# Creating a window with black image
img = numpy.zeros((300, 512, 3), numpy.uint8)
cv2.namedWindow('image')
# creating trackbars for red color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
# creating trackbars for Green color change
cv2.createTrackbar('G', 'image', 0, 255, nothing)
# creating trackbars for Blue color change
cv2.createTrackbar('B', 'image', 0, 255, nothing)
  
while(True):
    # show image
    cv2.imshow('image', img)
 
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
  
    # get positions
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    img[:] = [b, g, r]
  
# close the window
cv2.destroyAllWindows()