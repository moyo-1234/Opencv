import cv2
import os

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
        startlab = startlab + 1
