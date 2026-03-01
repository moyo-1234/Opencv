#Read an image and display it to  the user
# import cv2
# img = cv2.imread("pika.png" , cv2.IMREAD_COLOR)
# cv2.imshow("Pikachu Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#Read the image and display the image in greyscale
#Greyscale is the brightness of the image of a particular color
# import cv2
# img = cv2.imread("pika.png" , 0)# 0 --> greyscale
# cv2.imshow("Pikachu in greyscale", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 

#save the resultant(greyscale)image using aopen cv and oimpo
# import cv2 
# import os

# saved_directory =  "C:\\Users\\femia\\Desktop\\Opencv\\basic_intro\\openCV.py"

# img = cv2.imread("C:\\Users\\femia\\Desktop\\pika.png")
# cv2.imshow("Pikachu in black and white", img)

# cv2.waitkey(0)
# cv2.destroyAllWindows()

# os.chdir(saved_directory)

# cv2.imwrite("pikachuBlackWhite.png", img)
# print("Successfully saved")

#print an image in different colour formats

# import cv2

# image = cv2.imread("pika.png", 1)

# B, G, R = cv2.split(image)

# cv2.imshow("original", image)
# cv2.waitkey(0)

# cv2.imshow("original", B)
# cv2.waitkey(0)

# cv2.imshow("original", G)
# cv2.waitkey(0)

# cv2.imshow("original", R)
# cv2.waitkey(0)
# even = 7

# # cv2.destroyAllWindows()

# for i in range (11):
#     print("3 x ",(i),"=",3*i)

# if even % 2 == 0:
#     print("even")
# else:
#     print("odd")

# hi = [1,2,3,4,5]

# hi[2]

# print(hi[2])

string = ("Hi I am 12 years old")

string.count()