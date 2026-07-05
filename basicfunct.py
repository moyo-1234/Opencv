import cv2
import numpy as np

rimg = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\rugby.png",1)
cv2.imshow("Rugby Ball",rimg)
cv2.waitKey(0)
rrimg = cv2.resize(rimg,(300,300))
cv2.imshow("rugby ball",rrimg)
cv2.waitKey(0)

cimg = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\crcketball.png",1)
cv2.imshow("Cricket Ball",cimg)
cv2.waitKey(0)
crimg = cv2.resize(cimg,(300,300))
cv2.imshow("cricket ball",crimg)
cv2.waitKey(0)

var = cv2.addWeighted(crimg,0.2,rrimg,0.8,0)
cv2.imshow("weight",var)
cv2.waitKey(0)
subres = cv2.subtract(rrimg,crimg)
cv2.imshow("subresult",subres)
cv2.waitKey(0)

# print(rimg)
k = np.ones((1,1),np.uint8)
resimg = cv2.erode(rrimg,k) 
cv2.imshow("rugby ball",resimg)
cv2.waitKey(0)

gb = cv2.GaussianBlur(crimg,(15,15),1)
cv2.imshow("Blurred image",gb)
cv2.waitKey(0)

mb = cv2.medianBlur(rrimg,15)
cv2.imshow("Blurred image",mb)
cv2.waitKey(0)

bb = cv2.bilateralFilter(crimg,18,100,70)
cv2.imshow("bilateral image",bb)
cv2.waitKey(0)

bi = cv2.copyMakeBorder(rrimg,15,15,15,15,cv2.BORDER_CONSTANT,value = (0,0,0))
cv2.imshow("Bordered image",bi)
cv2.waitKey(0)

rbi = cv2.copyMakeBorder(rrimg,15,15,15,15,cv2.BORDER_REFLECT)
cv2.imshow("Bordered image",rbi)
cv2.waitKey(0)

