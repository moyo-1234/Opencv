import cv2
import os
totalimg = 0

hardfile = (r"C:\Users\femia\Desktop\python_game_dev\Opencv\Facial Recognition\haarcascade_frontalface_default.xml")
Family = (r"C:\Users\femia\Desktop\python_game_dev\Opencv\Facial Recognition\Family Folders")
Moyo = (r"C:\Users\femia\Desktop\python_game_dev\Opencv\Facial Recognition\Family Folders\Moyo")
if not os.path.isdir(Moyo):
    os.mkdir(Moyo)
 
face = cv2.CascadeClassifier(hardfile)
camon = cv2.VideoCapture(0)
for i in range(30):
    ToF,img =camon.read()
    imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    facecoord = face.detectMultiScale(imggrey,1.3,4)
    print(facecoord)
    print(ToF)
    if ToF == True:
        totalimg = totalimg + 1
    for x,y,w,h in facecoord:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        facesize = imggrey[y:y+h,x:x+w]
        rface = cv2.resize(facesize,(150,120))
        os.chdir(Moyo)
        cv2.imwrite("Moyo%s.png"%i,rface)
        print(x,y,w,h)
    cv2.imshow("Moyo",img)
    cv2.waitKey(10)
    


print(totalimg)


    
    