import cv2
import numpy as np
import matplotlib.pyplot as plt

#Video and image analyzing is interchangeable

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE) #Image read. if you don't specify anything, then it'll read it in as a colour image. Convert it to grayscale, because it's simplified.
#A lot easier to perform analysis on a grayscale image. Only deal with one colour, a lot faster.

#We can show the image in a lot of ways. Can plot and other things with matplotlib.
#plt.imgshow(img, cmap='gray', interpolation='bicubic')


#OpenCV show image
cv2.imshow('image', img) #Image show
cv2.waitKey(0) #Waits for any key to be pressed
cv2.destroyAllWindows()

#Saves picture
#cv2.imwrite('watchgray.png', img)

"""
capture = cv2.VideoCapture(0) #Captures first webcam on your system.

while True:
    ret, frame = capture.read()
    cv2.imshow('frame', frame) #Give it a name

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
"""