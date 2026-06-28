import cv2

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

var = cv2.addWeighted(crimg,0.5,rrimg,0.6,0)
cv2.imshow("weight",var)
cv2.waitKey(0)
subres = cv2.subtract(rrimg,crimg)
cv2.imshow("subresult",subres)
cv2.waitKey(0)