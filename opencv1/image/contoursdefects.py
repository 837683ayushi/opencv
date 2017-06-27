import cv2
import numpy as np
img=cv2.imread('Desktop/ayushi.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',img_gray)
ret,thresh=cv2.threshold(img_gray,127,255,0)
cv2.imshow('thresh',thresh)
contours,hierarchy=cv2.findContours(thresh,2,1)
print contours
cnt=contours[0]
print cnt
hull=cv2.convexHull(cnt,returnPoints=False)
cv2.imshow('hull',hull)
defects = cv2.convexityDefects(cnt,hull)
for i in defects.shape[0]:
  s,e,f,d=defects[i,0]
  start=tuple(cnt[s][0])
  end=tuple(cnt[e][0])
  far=tuple(cnt[f][0])
  cv2.line(img,start,end,[0,255,0],2)
  cv2.circle(img,far,[0,0,255],-1)

cv.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
