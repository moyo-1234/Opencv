import cv2
import numpy as np

imagea = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\Homework\shape.png" , 1)
cv2.imshow("shape", imagea)
cv2.waitKey(0)

imageb = np.ones((7,7),np.uint8)
resimg = cv2.erode(imagea,imageb) 
cv2.imshow("shape b",resimg)
cv2.waitKey(0)
