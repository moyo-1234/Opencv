import cv2
import os

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

    
    