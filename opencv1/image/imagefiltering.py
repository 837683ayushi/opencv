import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('Desktop/1.jpg')
kernel=np.ones((6,7),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)
plt.imshow(img)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.show()
