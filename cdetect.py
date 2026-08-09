import cv2
import numpy as np

circle = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\image1.jfif",1)
cv2.imshow("circle",circle)
cv2.waitKey(0)

gcircle = cv2.cvtColor(circle,cv2.COLOR_BGR2GRAY)
bcircle = cv2.blur(gcircle,(3,3))

det_circ = cv2.HoughCircles(bcircle,cv2.HOUGH_GRADIENT,1,20,param1 = 45,param2 = 30,minRadius=1,maxRadius=20)
# det_circ = np.uint16(np.around(det_circ))
print(det_circ)

# for i in det_circ:
#     print(i)
