import cv2
import numpy as np

img = cv2.imread('sublime2.png')

edges = cv2.Canny(img, 100, 200)

img2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

mask = np.zeros(img.shape, np.uint8)
image = 0

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #Removes tiny deviations, tries to go for straight lines.
    if len(approx) == 4:
        print("square")
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 10:
            print("Width and height: ", w, h)
            cv2.rectangle(mask, (x, y), (x+w, y+h), (0,255,0), 2)
            image = img[y:y+h, x:x+w]

cv2.imshow('image', img)
cv2.imshow('edges', edges)
cv2.imshow('img2', image)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()