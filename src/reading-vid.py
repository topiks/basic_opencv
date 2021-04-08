import cv2 as cv

capture = cv.VideoCapture("../videos/jakarta.mp4") #untuk file
# capture = cv.VideoCapture(0) #untuk kamera

while True:
    isTrue, frame = capture.read()
    cv.imshow("jendala video", frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


