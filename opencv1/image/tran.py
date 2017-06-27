import cv2
import numpy as np
img = cv2.imread('Desktop/ayus.png',0)
kernel = np.ones((4,4),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('img1',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
