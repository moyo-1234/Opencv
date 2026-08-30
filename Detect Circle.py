import cv2
import numpy as np

Coin = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\Homework\Coins.jpg",1)
cv2.imshow("Coin",Coin)
cv2.waitKey(0)

Coins = cv2.cvtColor(Coin,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey",Coins)
cv2.waitKey(0)

Blurred = cv2.GaussianBlur(Coins,(15,15),1)
cv2.imshow("Gaussian",Blurred)
cv2.waitKey(0)

det_coin = cv2.HoughCircles(Blurred,cv2.HOUGH_GRADIENT,1,20,param1 = 45,param2 = 30,minRadius=35,maxRadius=60)
det_coin = np.uint16(np.around(det_coin))


for i in det_coin[0,:]:
     print(i)
     xv = i[0]
     yv = i[1]
     rv = i[2]
     detected = cv2.circle(Coin,(xv,yv),rv,(0,0,255),2)
     cv2.imshow("outlined",detected)
     cv2.waitKey(0)
