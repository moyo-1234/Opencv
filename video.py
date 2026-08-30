import cv2
import os
from PIL import Image

os.chdir("C:/Users/femia/Desktop/python_game_dev/Opencv/images folder")
imgpath = ("C:/Users/femia/Desktop/python_game_dev/Opencv/images folder")

imgs = []
width = 0
height = 0

for i in os.listdir("."):
    if i.endswith((".jpg",".png",".jpeg",".avif" )):
        imgs.append(i)
print(imgs)



for i in imgs:
    A = Image.open(os.path.join(imgpath,i))
    awidth , aheight = A.size
    print(awidth)
    print(aheight)
    width = width + awidth
    height = height + aheight
width = width//len(imgs)
height = height//len(imgs)
print(width)
print(height)
for i in imgs:
    B = Image.open(os.path.join(imgpath,i))
    rimg = B.resize((width,height),Image.Resampling.LANCZOS)
    rimg.save(i,"JPEG",quality = 95)

Sports = "Sports.mp4"
videofile = cv2.VideoWriter(Sports,cv2.VideoWriter_fourcc(*"mp4v"),1,(width,height))
for i in imgs:
    videofile.write(cv2.imread(os.path.join(imgpath,i)))