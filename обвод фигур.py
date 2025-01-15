import cv2
import numpy
import matplotlib

import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading image
img = cv2.imread('templates/template_in_0.jpg')

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# using a findContours() function
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
num = 0
for i in contours:
    if num != 0:
        cv2.drawContours(img, [i], 0, (25, 125, 0), 2)
    num += 1
cv2.imshow('фигуры с маской', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
