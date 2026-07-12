import cv2

pika = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\basic_intro\pika.png",1)
cv2.imshow("pikachu",pika)
cv2.waitKey(0)
sg = cv2.cvtColor(pika,cv2.COLOR_BGR2HSV)
cv2.imshow("Grey Pikachu",sg)
cv2.waitKey(0)

(rows,cols) = pika.shape[0:2]

print(rows)
print(cols)

rm = cv2.getRotationMatrix2D((rows/2,cols/2),90,1)
rimg = cv2.warpAffine(pika,rm,(rows,cols))
cv2.imshow("rotated image",rimg)
cv2.waitKey(0)

ied = cv2.Canny(pika,50,200)
cv2.imshow("edges",ied)
cv2.waitKey(0)