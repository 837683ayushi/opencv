import cv2
img=cv2.imread('Desktop/ayushi.jpg',0)
img1=cv2.imread('Desktop/sahil.jpg',0)
img2=cv2.resize(img,(800,500))
img3=cv2.resize(img1,(800,500))
imgnew=cv2.addWeighted(img2,0.8,img3,0.2,0)
cv2.imshow("aa",imgnew)
cv2.waitKey(0)
cv2.destroyAllWindows()
