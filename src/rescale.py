import cv2 as cv

def rescaleFrame(frame, scale):
    h = int(frame.shape[0] * scale)
    w = int(frame.shape[1] * scale)

    dimensi = (w, h)

    return cv.resize(frame, dimensi, interpolation=cv.INTER_AREA)

# img = cv.imread("../images/minions.jpg")
# imgScale = rescaleFrame(img, 0.1);

# cv.imshow("jendela rescale", imgScale)
capture = cv.VideoCapture("../videos/jakarta.mp4")

while True:
    isTrue, frame = capture.read()
    frameScale = rescaleFrame(frame, 0.5)

    cv.imshow("jendela rescale", frameScale)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break

capture.release()
cv.destroyAllWindows()


# cv.waitKey(0)
    