import numpy as np
import cv2
from matplotlib import pyplot as plt
img=cv2.imread("Desktop/1.jpg",0)
plt.imshow(img,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.show()
