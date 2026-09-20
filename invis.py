import cv2
import numpy as np
import time

video = cv2.VideoCapture(r"C:\Users\femia\Desktop\python_game_dev\Opencv\invvid3.mov")
time.sleep(1)
bg = None
for i in range(50):
    Boleen,Frame = video.read()
    bg = Frame
bg = np.flip(bg,axis = 1)

while video.isOpened():
    BOleen,FRame = video.read()
    FRame = np.flip(FRame,axis = 1)
    hsv = cv2.cvtColor(FRame,cv2.COLOR_BGR2HSV)
    LL = np.array([0,0,0])
    LU = np.array([180,255,50])
    Firstmask = cv2.inRange(hsv,LL,LU)
    mask = Firstmask
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations = 1)
    rmask = cv2.bitwise_not(mask)
    crop1 = cv2.bitwise_and(bg,bg,mask = mask)
    crop2 = cv2.bitwise_and(FRame,FRame,mask = rmask)
    crop = cv2.addWeighted(crop1,1,crop2,1,0)
    cv2.imshow("Image",crop)
    wait = cv2.waitKey(1)

    if wait == 65 or wait == 97:
        break