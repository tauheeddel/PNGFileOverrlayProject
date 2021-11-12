import cvzone
import cv2
import numpy as np



imgBack = cv2.imread("Resources/pc.jpg")

#For making the background
#imgBack = np.ones((480,640,3), np.uint8)*255
imgFront = cv2.imread("Resources/logo.png", cv2.IMREAD_UNCHANGED)
imgFront = cv2.resize(imgFront, (0,0), None, 0.75, 0.75)


#imgFront = cv2.imread("Resources/mario.png")
#imgBack[0:187, 0:270] = imgFront

hf, wf, cf = imgFront.shape
hb, wb, cb = imgBack.shape


imgResult = cvzone.overlayPNG(imgBack, imgFront, [0, hb-hf])

cv2.imshow("Image", imgResult)
cv2.waitKey(0)