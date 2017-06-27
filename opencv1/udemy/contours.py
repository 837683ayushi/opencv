import cv2
import numpy as np
image=cv2.imread('Desktop/as.png')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,threshold=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)																																																																																																																																															contours,_=cv2.findContours(threshold,1,2)
cnt=contours[0]
cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
cv2.imshow('Display',image)
cv2.waitKey(0)
