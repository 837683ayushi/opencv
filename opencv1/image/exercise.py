import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
  pass
img=cv2.imread("Desktop/sahil.jpg",0)
cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)
while(1):

 r= cv2.getTrackbarPos('R','image')
 g= cv2.getTrackbarPos('G','image')
 s= cv2.getTrackbarPos(switch,'image')
 if s == 0:
    edges=img
 else:
    edges=cv2.Canny(img,r,g)
 cv2.imshow('original', img)
 cv2.imshow('canny', edges)
 k = cv2.waitKey(1) & 0xFF
 if k == 27:
   break
cv2.destroyAllWindows()
