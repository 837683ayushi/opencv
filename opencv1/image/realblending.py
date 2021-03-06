import cv2
import numpy as np
A=cv2.imread('Desktop/ayushi.jpg')
B=cv2.imread('Desktop/sahil.jpg')
G=A.copy()
gpa=[G]
for i in xrange(6):
  G=cv2.pyrDown(G)
  gpa.append(G)

G=B.copy()
gpb=[G]
for i in xrange(6):
  G=cv2.pyrDown(G)
  gpb.append(G)
lpa=[gpa[5]]

for i in xrange(5,0,-1):
  GE=cv2.pyrUp(gpa[i])
  L=cv2.subtract(gpa[i-1],GE)
  lpa.append(L)
lpb=[gpb[5]]

for i in xrange(5,0,-1):
  GE=cv2.pyrUp(gpb[i])
  L=cv2.subtract(gpb[i-1],GE)
  lpa.append(L)

LS=[]
for la,lb in zip(lpa,lpb):
  rows,cols,dpt=la.shape
  ls=np.hstack((la[:,0:cols/2],lb[:,cols/2:]))
  LS.append(ls)

ls_=LS[0]
for i in xrange(1,6):
  ls_=cv2.pyrUp(ls_)
  ls_=cv2.add(ls_,LS[i])

real=np.hstack((A[:,:cols/2],B[:,cols/2:]))
cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_bkending.jpg',real)

