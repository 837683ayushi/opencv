import numpy as np
import cv2
from matplotlib import pyplot as plt
img=np.zeros((512,512,3),np.uint8)
img=cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.namedWindow('image')
cv2.setMouseCallback('image',img)
while(1):
  cv2.imshow('image',img)
  if cv2.waitKey(20) & 0xFF == 27:
    break
cv2.destroyAllWindows()

