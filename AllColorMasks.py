import cv2
import numpy as np

img = cv2.imread('images/top-view.jpg')
val = 40

# colors from Colorzilla -> BGR
real_colors = {
    "yellow": [48, 212, 237],
    "red": [62, 54, 220],
    "white": [237, 232, 221],
    "green": [11, 105, 45],
}

for color in real_colors:
    lower = np.array(real_colors[color]) - np.array([val, val, val])
    upper = np.array(real_colors[color]) + np.array([val, val, val])
    mask = cv2.inRange(img, lower, upper)
    # cv2.imshow(f"Mask {color}", mask)
    cv2.waitKey(0)

cv2.imshow(f"Mask Sum", sum)
cv2.waitKey(0)