import cv2
import numpy
import matplotlib
import PIL
import numpy as np


class FileWorker():
    def __init__(self, file):
        self.file = file
        img = PIL.Image.open(file)
        self.width, self.height = img.size

    def col(self):
        img = cv2.imread(self.file, cv2.IMREAD_COLOR)
        # img = cv2.imread("templates/template_in_0.jpg", cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # делаем картинку черно-белой
        contours_img = cv2.Canny(gray, 240, 240)  # считываем контуры
        contour, node = cv2.findContours(contours_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # считываем контуры и узлы
        print(len(contour))  # смотрим количество

    def set_contours(self):
        file = open(self.file, "rb")
        bytes = bytearray(file.read())
        numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
        img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(
            threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        num = 0
        for i in contours:
            if num != 0:
                cv2.drawContours(img, [i], 0, (25, 125, 0), 2)
            num += 1
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return img


