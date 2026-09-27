import cv2
import numpy as np


image1 = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\Homework\image1.png" , 1)
cv2.imshow("object", image1)
img2 = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\Homework\image2.png" , 1)
cv2.imshow("no object", img2)
shape = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\Homework\shape.png"  ,  1)
cv2.imshow("shape", shape)
image2 = cv2.resize(img2,(380,462))
cv2.imshow("without",image2)
cv2.waitKey(0)

subres = cv2.subtract(image2,image1)
cv2.imshow("subresult",subres)
cv2.waitKey(0)

#You could subtract two images from eachother to check any differences in a room if you had to look at two different images from different times

k = np.ones((15,15),np.uint8)
resimg = cv2.erode(shape,k) 
cv2.imshow("shape",resimg)
cv2.waitKey(0)

