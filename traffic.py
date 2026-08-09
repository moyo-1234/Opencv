import cv2
blank = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\blank.png",1)
cv2.imshow("page",blank)
cv2.waitKey(0)


sp = (40,40)
ep = (180,360)

traffic = cv2.rectangle(blank,sp,ep,(0,0,0),-1)
cv2.imshow("rectangle",traffic)
cv2.waitKey(0)


circimg = cv2.circle(traffic,(120,100),30,(0,0,255),-1)
cv2.imshow("circle",circimg)
cv2.waitKey(0)

circimg = cv2.circle(traffic,(120,180),30,(0,255,255),-1)
cv2.imshow("circle",circimg)
cv2.waitKey(0)

circimg = cv2.circle(traffic,(120,260),30,(0,128,0),-1)
cv2.imshow("circle",circimg)
cv2.waitKey(0)