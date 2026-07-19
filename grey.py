import cv2

pika = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\basic_intro\pika.png",1)
cv2.imshow("pikachu",pika)
cv2.waitKey(0)
# sg = cv2.cvtColor(pika,cv2.COLOR_BGR2HSV)
# cv2.imshow("Grey Pikachu",sg)
# cv2.waitKey(0)

# (rows,cols) = pika.shape[0:2]

# print(rows)
# print(cols)

# rm = cv2.getRotationMatrix2D((rows/2,cols/2),90,1)
# rimg = cv2.warpAffine(pika,rm,(rows,cols))
# cv2.imshow("rotated image",rimg)
# cv2.waitKey(0)

# ied = cv2.Canny(pika,50,200)
# cv2.imshow("edges",ied)
# cv2.waitKey(0)

sp = (60,60)
ep = (180,180)
limg = cv2.line(pika,sp,ep,(0,165,255),3)
cv2.imshow("line",limg)
cv2.waitKey(0)

rectimg = cv2.rectangle(pika,ep,sp,(30,144,255),-1)
cv2.imshow("rectangle",rectimg)
cv2.waitKey(0)

circimg = cv2.circle(pika,(120,120),8,(0,0,255),-1)
cv2.imshow("circle",circimg)
cv2.waitKey(0)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
text = cv2.putText(pika,"Hi my name is Moyo",(10,60),font,1,(255,0,0),2,cv2.LINE_AA)
cv2.imshow("text",text)
cv2.waitKey(0)
