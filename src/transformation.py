import cv2 as cv
import numpy as np

img = cv.imread("../images/mini.jpg")
cv.imshow("jendela 1", img)

# translation
def transMat(src, x, y):
    trans = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans, dimensions)

# rotate
def rotateMat(src, angle, rotPoint=None):
    (h,w) = img.shape[:2]
    
    if rotPoint == None:
        rotPoint = (w//2, h//2)
    
    rot = cv.getRotationMatrix2D(rotPoint, angle, 1)
    dimensions = (w,h)

    return cv.warpAffine(src, rot, dimensions)


# flip
flip = cv.flip(img, -1)
# coba = transMat(img, 100, 100)
# coba = rotateMat(img, -45)
cv.imshow("coba", flip)

cv.waitKey(0)