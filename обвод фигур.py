import sys
from tkinter.filedialog import asksaveasfilename

import cv2
import numpy
import matplotlib
from tkinter import filedialog as fd, Image
import cv2
import numpy as np
from PIL import ImageTk
from matplotlib import pyplot as plt


file = open(u'templates/template_in_0.jpg', "rb")
bytes = bytearray(file.read())
numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)

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
print(img)
try:
    cv2.imwrite("file_img.jpg", img)
except Exception as e:
    print(e)
cv2.waitKey(0)
cv2.destroyAllWindows()
