#Using image in cv2
import cv2
import numpy as np
# print("Package imported")
#
# img = cv2.imread("Resources/Nikh_pic.jpg")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

#Using video to upload

# cap = cv2.VideoCapture("Resources/vido1.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break

#Using Webcam

#
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)#For increasing brightness
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break


img = cv2.imread("Resources/ap.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgGray,(7,7),0)
imgcanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgcanny, kernel, iterations=1)
imgerode = cv2.erode(imgDialation, kernel,iterations=1)


cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgblur)
cv2.imshow("Canny Image", imgcanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erode Image", imgerode)
cv2.waitKey(0)