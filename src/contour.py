import cv2 as cv
import numpy as np

img = cv.imread("../images/robot.jpg")
# cv.imshow("jendela", img)

img_new = cv.resize(img, (int(img.shape[1] * 0.1), int(img.shape[0] * 0.1)))

# create a blank canvas
blank = np.zeros(img_new.shape)
# cv.imshow("blank", blank)

# convert img to grey
gray = cv.cvtColor(img_new, cv.COLOR_BGRA2GRAY)
cv.imshow("jendela 1", gray)

# convert to blur
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("jendela 3", blur)

# convert blur to canny
canny = cv.Canny(blur, 125, 175)
# cv.imshow("jendela 2", canny)

# trying to thershold from grey
ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("hasil threshold", thres)

# find the contours
contours, hierarchies = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))

# draw the contours
hasil = cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow("hasil", hasil)

cv.waitKey(0)