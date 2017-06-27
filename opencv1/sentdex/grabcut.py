import cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread("Desktop/ayushi.jpg")
mask=np.zeroes(img.shape[:],np.uint8)
bgdModel=np.zeroes((1,65
