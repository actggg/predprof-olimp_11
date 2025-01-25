import os
import cv2
import numpy
import csv
from PIL import Image


class FileWorker:
    def __init__(self, file):
        self.file_name = file
        file = open(self.file_name, "rb")
        bytes = bytearray(file.read())
        numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
        self.img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
        self.width, self.height = self.img.shape[:2]

    def col(self):
        img = self.img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # делаем картинку черно-белой
        contours_img = cv2.Canny(gray, 240, 240)  # считываем контуры
        contour, node = cv2.findContours(contours_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # считываем контуры и узлы
        return len(contour)  # смотрим количество


    def save_csv(self, file_name):
        my_list = [file_name, self.col()]

        with open('templates_out.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(my_list)

    def set_contours(self):
        img = self.img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        contours_img = cv2.Canny(gray, 240, 240)
        contours, _ = cv2.findContours(
            contours_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        num = 0
        for i in contours:
            if num != 0:
                cv2.drawContours(img, [i], 0, (25, 125, 0), 2)
            num += 1
        return img

    def save_photo(self, img, path, subdir, name):
        if subdir != None:
            os.makedirs(os.path.join(path, subdir), exist_ok=True)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_PIL = Image.fromarray(img)
            img_PIL.save(os.path.join(path, subdir, name))
        else:
            print(os.path.join(path, name))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_PIL = Image.fromarray(img)
            img_PIL.save(os.path.join(path, name))

    def file_name_no_path(self):
        return os.path.basename(self.file_name)
