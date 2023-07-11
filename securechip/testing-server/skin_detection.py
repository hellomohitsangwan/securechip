import cv2
import imutils
import numpy as np
import os
import glob

path = r"dbNudeDetection\non_nude\nonnude65.jpg"

# HSV Color Space
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
cap = cv2.imread(path)
cap = imutils.resize(cap,width=400)
converted = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
skinMask = cv2.inRange(converted, lower, upper)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
skinMask = cv2.erode(skinMask, kernel, iterations = 2)
skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
skin = cv2.bitwise_and(cap, cap, mask = skinMask)
cv2.imshow("HSV", np.hstack([cap, skin]))

# DB_PATH = "./dbNudeDetection/"
# # if not(os.path.isdir(DB_PATH+"/skin")):
# #     os.mkdir(DB_PATH+"/skin")
# for i in glob.glob(DB_PATH+"nude/"+"*.jpg"):
#     filename = i[len("./dbNudeDetection/nude/"):]
#     cap = cv2.imread(i)
#     cap = imutils.resize(cap,width=400)
#     converted = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
#     skinMask = cv2.inRange(converted, lower, upper)
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
#     skinMask = cv2.erode(skinMask, kernel, iterations = 2)
#     skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
#     skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
#     skin = cv2.bitwise_and(cap, cap, mask = skinMask)
#     cv2.imwrite(DB_PATH+"/skin/"+filename,skin)
    # cv2.imshow("images", np.hstack([cap, skin]))

# YCrCb Space
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([235,173,127],np.uint8)
image = cv2.imread(path)
image = imutils.resize(image,width=400)
imageYCrCb = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)
skinRegionYCrCb = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)
skinYCrCb = cv2.bitwise_and(image, image, mask = skinRegionYCrCb)
cv2.imshow("YCrCb Space", np.hstack([image,skinYCrCb]))

cv2.waitKey(0)
cv2.destroyAllWindows()

# vid = cv2.VideoCapture(0)
# while(True):
#     ret, frame = vid.read()
#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# vid.release()
# cv2.destroyAllWindows()