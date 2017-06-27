import numpy as np
import cv2
img= cv2.imread('Desktop/ayushi.jpg',cv2.IMREAD_COLOR)
px=img[55,55]
img[55,55]=[255,255,255]
px=img[55,55]
print px
img[100:150,100:150]=[255,255,255]
watch_face=img[37:311,107:394]
img[0:274,0:287]=watch_face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

