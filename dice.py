import cv2
import numpy as np
import imutils
import time
cap = cv2.VideoCapture(0)
max=-1
while(1):
    _, frame = cap.read()

    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    
    lower_orange = np.array([0 , 60, 180])
    upper_orange = np.array([255 ,100, 250])
    font = cv2.FONT_HERSHEY_SIMPLEX
    topLeftCornerOfText = (10,30)
    fontScale = 1
    fontColor = (0,0,0)
    lineType = 2
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    mask = cv2.bitwise_not(mask)
    circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1, 20,param1=30,param2=15,minRadius=2,maxRadius=40)
    if circles is not None:
        output = mask.copy()
        circles = np.round(circles[0, :]).astype("int")
        if ((len(circles) > 0) and (len(circles) <=6)):
            if ((len(circles))>max):
               max=len(circles)
    cv2.imshow("Preview", mask)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
    	break
print(max)
cv2.destroyAllWindows()
cap.release()
