import numpy as np
import cv2
img=cv2.imread('Desktop/ayushi.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.circle(img,(100,63),55,(0,0,255),-1)
pts=np.array([[10,5],[20,300],[710,2000],[500,1000]],np.int32)
#pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Open CVTuts!',(0,130),font,0.5,(200,255,255),3,cv2.CV_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



