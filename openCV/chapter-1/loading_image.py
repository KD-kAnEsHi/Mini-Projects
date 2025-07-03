import cv2 as cv 
import sys

img = cv.imread(cv.samples.findFile("starry_night.jpg"))

if img is None:
    sys.exit("Could not load the image")

cv.imshow("Display Img", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("Starry_night.png", img)