import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500.0:
            print(area)
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # cv2.putText(imgContour, "Square",
            #            (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
            #           (0, 0, 0), 2)



# colors from Colorzilla -> BGR
real_colors = {
    "yellow": [48, 212, 237],
    "red": [220, 54, 62],
    "white": [237, 232, 221],
    "green": [11, 105, 45],
}

img = cv2.imread('images/top-view.jpg')
# Image Resizing ton Half
img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
# cv2.imshow("Bottles Top View",img)

lower = np.array(real_colors['yellow']) - np.array([30, 30, 30])
upper = np.array([78, 242, 255])

mask = cv2.inRange(img, lower, upper)
cv2.imshow("Bottles Top View", img)
cv2.imshow("Yellow Mask", mask)

imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

kernal = np.ones((5,5))
imgErode = cv2.erode(imgCanny,np.ones((1,1)),iterations=1)
imgDialate = cv2.dilate(imgErode,kernal,iterations=1)

getContours(mask)

cv2.imshow("Drawn Countour", imgContour)

cv2.waitKey(0)
cv2.destroyAllWindows()
