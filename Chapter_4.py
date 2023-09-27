import cv2
import numpy as np

img = np.zeros((300,300,3),np.uint8)
# print(img.shape)
# print(img)
# img[:] = 255,0,0

cv2.line(img,(0,0),(img.shape[1], img.shape[0]),(0,255,0),1)
cv2.rectangle(img,(0,0),(100,150),(0,0,255),2)
cv2.circle(img,(250,50),30,(255,255,0),4)
cv2.putText(img,"OPENCV ", (100,100),cv2.FONT_ITALIC,1,(0,150,0),2)
cv2.imshow("Image",img)
cv2.waitKey(0)
