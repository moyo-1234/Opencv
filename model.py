import cv2
import os
import numpy as np

hardfile = (r"C:\Users\femia\Desktop\python_game_dev\Opencv\Facial Recognition\haarcascade_frontalface_default.xml")
familyfolder = (r"C:\Users\femia\Desktop\python_game_dev\Opencv\Facial Recognition\Family Folders")
imglist = []
labels = []
startlab = 1
keypoints = {}

for folder,subfolder,files in os.walk(familyfolder):
    for subfolders in subfolder:
        keypoints[startlab] = subfolders
        print(subfolders,keypoints)
        path = os.path.join(familyfolder,subfolders)
        for i in os.listdir(path):
            nameandpath = os.path.join(path,i)
            imglist.append(nameandpath)
            labels.append(startlab)
        startlab = startlab + 1
images = np.array(imglist)
text = np.array(labels)

