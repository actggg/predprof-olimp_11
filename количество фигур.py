import os
from PIL import Image
import PIL
# loading the image
import cv2
import numpy
import matplotlib

img = cv2.imread("templates/template_in_0.jpg", cv2.IMREAD_COLOR)
#img = cv2.imread("templates/template_in_0.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # делаем картинку черно-белой
contours_img = cv2.Canny(gray, 240, 240) # считываем контуры
contour, node = cv2.findContours(contours_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #считываем контуры и узлы
print(len(contour)) # смотрим количество