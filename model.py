import cv2
import os
import numpy as np

hardfile = (r"C:\Users\femia\Desktop\python_game_dev\Opencv\Facial Recognition\haarcascade_frontalface_default.xml")
familyfolder = (r"C:\Users\femia\Desktop\python_game_dev\Opencv\Facial Recognition\Family Folders")
imglist = []
labels = []
startlab = 1
keypoints = {}
totalimg = 0

for folder,subfolder,files in os.walk(familyfolder):
    for subfolders in subfolder:
        keypoints[startlab] = subfolders
        print(subfolders,keypoints)
        path = os.path.join(familyfolder,subfolders)
        for i in os.listdir(path):
            nameandpath = os.path.join(path,i)
            imglist.append(cv2.imread(nameandpath,0))
            labels.append(startlab)
        startlab = startlab + 1
images = np.array(imglist)
text = np.array(labels)
print(imglist)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,text)

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
        preres = model.predict(rface)
        print(preres)
        key = preres[0]
        prediction = keypoints[key]
        cv2.putText(img,prediction,(50,60),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2,cv2.LINE_AA)
    cv2.imshow("Moyo",img)
    cv2.waitKey(10)
# font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
# text = ("Captured: "+str(totalimg)+" / 30")
# facecount = cv2.putText(img,text,(10,60),font,1,(0,0,0),2,cv2.LINE_AA)
# cv2.imshow("text",facecount)
# cv2.waitKey(0)
