import numpy as np
import cv2 as cv
import time
import HandTrackingModule as htm
wCam, hCam = 640, 480

cam = cv.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)
pTime=0

detector = htm.handDetector(detectionCon=0.7)

while True:
    s, img = cam.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList)!= 0:a
        print(lmList[4, lmList[8]])

    cTime = time.time()
    fps = 1/(cTime- pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (40, 50), cv.FONT_HERSHEY_COMPLEX, 1,
               (255, 0, 0), 3)

    cv.imshow("Image", img)
    cv.waitKey(1)
