import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

img3 = cv2.imread('mainlogo.png')
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY) #Creates a grayed out version of the logo.
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) #Binary threshold, 0 or 1. 220 is the threshold value. If it's above 220, then it gets converted to 255. If it's below 220, it gets turned to 0
#Flips the colors around because it's inverse.

#cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)

add = img1 + img2
#add = cv2.add(img1, img2) #Adds all of the pixel values together, so most reach around 255, 255, 255
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) #Uses weights for adding. The weights have to add up to 1.

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()

