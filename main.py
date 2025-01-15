import cv2
import numpy
import matplotlib

f = cv2.imread("templates/template_in_0.jpg")
print(len(f))

for i in f:
    print(i)