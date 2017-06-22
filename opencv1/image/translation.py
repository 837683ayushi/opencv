import numpy as np
import cv2
img=cv2.imread('Desktop/1.jpg',0)
rows,cols=img.shape
M=np.float32([[1,0,500],[0,1,500]])
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
