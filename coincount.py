import cv2
import numpy as np

CoinCount = 0

Coins = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\Homework\Coins.jpg",1)
cv2.imshow("Coins",Coins)
cv2.waitKey(0)

det_blob = cv2.SimpleBlobDetector_Params()
det_blob.filterByCircularity = True
det_blob.minCircularity = 0.6
det_blob.filterByArea = True
det_blob.minArea = 150
det_blob.filterByConvexity = True
det_blob.minConvexity = 0.5

detect = cv2.SimpleBlobDetector_create(det_blob)
sdc = detect.detect(Coins)
dkp = cv2.drawKeypoints(Coins,sdc,Coins,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("New Image",Coins)
cv2.waitKey(0)