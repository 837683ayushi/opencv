import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while(1):
  _,frame=cap.read()
  hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  lower_blue = np.array([110,50,50])
  upper_blue = np.array([130,255,255])  
  lower_green=np.array([50,50,120])
  upper_green=np.array([60,255,255])
  mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
  mask2 = cv2.inRange(hsv, lower_green, upper_green)
  mask=mask1+mask2
  res = cv2.bitwise_and(frame,frame, mask= mask)
  cv2.imshow('frame',frame)
  cv2.imshow('hsv',hsv)
  cv2.imshow('mask',mask)
  cv2.imshow('res',res) 
  k = cv2.waitKey(5) & 0xFF
  if k == 27:
    break
cv2.destroyAllWindows()
