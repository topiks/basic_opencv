import cv2 as cv

img = cv.imread("../images/soccer.jpg")
dimensi = (int(img.shape[1]*0.1), int(img.shape[0]*0.1))

img_new = cv.resize(img, dimensi,  interpolation=cv.INTER_AREA)
# cv.imshow("jendela", img_new)

# converting to grayscale
gray = cv.cvtColor(img_new, cv.COLOR_BGRA2GRAY)
# cv.imshow("jendela 1", gray)

# blur
blur = cv.GaussianBlur(img_new, (71,71), cv.BORDER_DEFAULT)
# cv.imshow("jendela 2", blur)

# edge cascade
canny = cv.Canny(img_new, 125, 175)
# cv.imshow("jendela 3", canny)

# dilate
dilate = cv.dilate(canny, (3,3), iterations=5)
# cv.imshow("jendela 4", dilate)

# erode
erode = cv.erode(dilate, (3,3), iterations=7)
# cv.imshow("jendela 5", erode)

# resized
resized = cv.resize(img_new, (500,500))
cv.imshow("jendela 6", resized)

# cropped
cropped = img_new[50:200, 200:400]
cv.imshow("jendela 7", cropped)

cv.waitKey(0)