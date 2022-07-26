from tkinter import Toplevel
from cv2 import destroyAllWindows
import numpy as np
import cv2

img = cv2.imread("C:/Users/break/Documents/Python/circleDetectionTest2.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.medianBlur(gray, 35) #cv2.bilateralFilter(gray,10,50,50)
# Hough Circle Prams
minDist = 100
param1 = 30 #500
param2 = 50 #200 #smaller value-> more false circles
minRadius = 5
maxRadius = 500 #10
x=0
i=0
topLeft =()
#Detecting circles
circlesLocations=[]
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
while x != 1:
    
    #Converting to HSV
    imgHSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #Drawing cicles on the new imgHSV image
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]: #i = x,y, Radius
            circlesLocations.append(i[0:3])

            cv2.circle(imgHSV, (i[0], i[1]), i[2], (0, 0, 0), -1) #IMPORTANT!!! Line thickness must be -1. To fill in the circle completely
    #Setting HSV Range
    lowerBound=np.array([0,0,0])
    upperBound=np.array([1,1,1])
    #Making the mask
    myMask=cv2.inRange(imgHSV,lowerBound, upperBound)
    #Applying the mask
    myObject=cv2.bitwise_and(img, img, mask=myMask)
    i=len(circlesLocations)
    for num in range(0,len(circlesLocations)) :
        topLeft=[(circlesLocations[num][1]-circlesLocations[num][2]),(circlesLocations[num][1]+circlesLocations[num][2])]
        bottomRight=[(circlesLocations[num][0]-circlesLocations[num][2]),(circlesLocations[num][0]+circlesLocations[num][2])]

    #newFrame=img[bottomRight,topLeft]
        yes=myObject[topLeft[0]:topLeft[1], bottomRight[0]:bottomRight[1]]
        cv2.imshow('my mask', yes)
        cv2.waitKey(500)
        destroyAllWindows()
    x=1
    # Show result for testing:
    
    
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
print(bottomRight)
print(len(circlesLocations))
cv2.destroyAllWindows()