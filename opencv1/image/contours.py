import numpy as np
import cv2
img = cv2.imread('Desktop//ayushi.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours, hierarchy = cv2.findContours(thresh,1,2)
cnt=contours[0]
M=cv2.moments(cnt)
print M
