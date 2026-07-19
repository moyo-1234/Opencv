import cv2
import numpy as np

rimg = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\otherrug.png",1)
cv2.imshow("Rugby Ball",rimg)
cv2.waitKey(0)

timg = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\track.png",1)
cv2.imshow("Track", timg)
cv2.waitKey(0)

ried = cv2.Canny(rimg,50,200)
cv2.imshow("rugby shape",ried)
cv2.waitKey(0)

tied = cv2.Canny(timg,50,200)
cv2.imshow("track shape",tied)
cv2.waitKey(0)

rrimg = cv2.resize(rimg,(740,438))
cv2.imshow("rugby ball",rrimg)
cv2.waitKey(0)

var = cv2.addWeighted(timg,0.5,rrimg,0.5,1)
cv2.imshow("weight",var)
cv2.waitKey(0)
subres = cv2.subtract(rimg,timg)
cv2.imshow("subresult",subres)
cv2.waitKey(0)