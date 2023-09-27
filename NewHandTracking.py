import cv2 as cv
import mediapipe as mp
import time
import HandTrackingModule as h

pTime = 0
cTime = 0
cam = cv.VideoCapture(0)
detector = h.handDetector()
while True:
    s, img = cam.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv.imshow("Image", img)
    cv.waitKey(1)
