import cv2
import numpy as np

img = cv2.imread('sublime.png')

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

edges = cv2.Canny(img, 100, 100)

img2, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (255, 255, 0), 3)
print(contours)

mask = np.zeros(img.shape, np.uint8)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #Removes tiny deviations, tries to go for straight lines.
    print(len(approx))
    if len(approx)==5:
        print("pentagon")
        cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
        print("triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print("square")
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 10:
            print("Width and height: ", w, h)
            cv2.rectangle(mask, (x, y), (x+w, y+h), (0,255,0), 2)
        #cv2.drawContours(mask,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
        print("half-circle")
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print("circle")
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)

#cv2.imshow('laplacian', laplacian)
#cv2.imshow('sobelx', sobelx)
#cv2.imshow('sobely', sobely)
cv2.imshow('edges', edges)
cv2.imshow('img2', img)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()