import cv2 as cv
import numpy as np 

img = cv.imread("../images/mini.jpg")
blank = np.zeros((500,800,3), dtype='uint8')
# cv.imshow("jendela blank", blank)

# blank[100:200, 300:400] = 0,255,0
# cv.imshow("jendela hijau", blank)

# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0) ,thickness=2)
# cv.imshow("jendela", blank)

capture = cv.VideoCapture("../videos/jakarta.mp4")

while True:
    isTrue, frame = capture.read()
    # cv.rectangle(frame, (0,0), (200,200), (0,255,0), thickness=2)
    # cv.circle(frame, (frame.shape[1]//2,frame.shape[0]//2), 100, (0,0,255), thickness=2)
    # cv.line(frame, (0,0), (frame.shape[1]//2,frame.shape[0]//2),(255,0,0), thickness=2)
    cv.putText(frame, "Helloo taufik", (frame.shape[1]//3, frame.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)

    # frameScale = rescaleFrame(frame, 0.5)

    cv.imshow("jendela rescale", frame)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)
