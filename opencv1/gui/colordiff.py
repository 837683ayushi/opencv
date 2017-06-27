from matplotlib import pyplot as plt
import cv2
img=cv2.imread("Desktop/1.jpg")
b,g,r=cv2.split(img)
img2=cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(img2)
plt.show()
cv2.imshow('bgr image',img)
cv2.imshow('rgb image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
