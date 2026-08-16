import cv2
import numpy as np

# circle = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\image1.jfif",1)
# cv2.imshow("circle",circle)
# cv2.waitKey(0)

# gcircle = cv2.cvtColor(circle,cv2.COLOR_BGR2GRAY)
# bcircle = cv2.blur(gcircle,(3,3))

# det_circ = cv2.HoughCircles(bcircle,cv2.HOUGH_GRADIENT,1,20,param1 = 45,param2 = 30,minRadius=1,maxRadius=35)
# det_circ = np.uint16(np.around(det_circ))
# print(det_circ)

# for i in det_circ[0,:]:
#     print(i)
#     xv = i[0]
#     yv = i[1]
#     rv = i[2]
#     detected = cv2.circle(circle,(xv,yv),rv,(0,0,255),2)
#     cv2.imshow("outlined",detected)
#     cv2.waitKey(0)

oriimg = cv2.imread(r"C:\Users\femia\Desktop\python_game_dev\Opencv\image1.jfif",1)
cv2.imshow("original circle",oriimg)
cv2.waitKey(0)

det_blob = cv2.SimpleBlobDetector_Params()
det_blob.filterByCircularity = True
det_blob.minCircularity = 0.9
det_blob.filterByArea = True
det_blob.minArea = 80
det_blob.filterByConvexity = True
det_blob.minConvexity = 0.3

detect = cv2.SimpleBlobDetector_create(det_blob)
sdc = detect.detect(oriimg)
dkp = cv2.drawKeypoints(oriimg,sdc,oriimg,(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
print(sdc)
cv2.imshow("New Circle",oriimg)
cv2.waitKey(0)



