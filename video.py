import cv2
import os
from PIL import Image

os.chdir("C:/Users/femia/Desktop/python_game_dev/Opencv/images folder")
imgpath = ("C:/Users/femia/Desktop/python_game_dev/Opencv/images folder")

imgs = []

for i in os.listdir("."):
    if i.endswith((".jpg",".png",".jpeg",".avif" )):
        imgs.append(i)
print(imgs)
