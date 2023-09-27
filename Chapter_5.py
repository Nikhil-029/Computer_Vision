#Cropping image section from the orignal image

import cv2
import numpy as np

img = cv2.imread("Resources/Kings.jpg")
width, height = 250,350

pts1 = np.float32([[950,121],[1248,236],[736,480],[1088,690]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image", img)
cv2.imshow("OUTPUT ",imgOutput)
cv2.waitKey(0)