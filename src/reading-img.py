import cv2 as cv

img = cv.imread("../images/mini.jpg")
cv.imshow("jendela", img)

cv.waitKey(0)
cv.destroyAllWindows()