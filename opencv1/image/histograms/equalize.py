import cv2
import numpy as np
img = cv2.imread('Desktop/template.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite('res1.png',cl1)
cv2.imwrite('res.png',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
