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
        contours_img = cv2.Canny(gray, 240, 240)  # считываем картинку контуров
        contour, node = cv2.findContours(contours_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # считываем контуры и узлы
        return len(contour)  # смотрим количество контуров

    def save_csv(self, path, subdir, img_name, output_name = "templates_out.csv"):
        my_list = [img_name, self.col()]
        if subdir != None:
            os.makedirs(os.path.join(path, subdir), exist_ok=True)
            with open(str(os.path.join(path, subdir, output_name)), 'a', newline='') as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(my_list)
        else:
            with open(str(os.path.join(path, output_name)), 'a', newline='') as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(my_list)

    def set_contours(self):
        img = self.img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # делаем картинку черно-белой
        contours_img = cv2.Canny(gray, 240, 240)  # считываем картинку контуров
        contours, _ = cv2.findContours(
            contours_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  # считываем контуры и узлы
        num = 0
        for i in contours:
            if num != 0:
                cv2.drawContours(img, [i], 0, (0, 0, 160), 2)  # накладываем контуры
            num += 1
        return img

    def save_photo(self, img, path, subdir, name):  # сохранение изображения в директорию
        if subdir != None:
            os.makedirs(os.path.join(path, subdir), exist_ok=True)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_PIL = Image.fromarray(img)
            img_PIL.save(os.path.join(path, subdir, name))
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_PIL = Image.fromarray(img)
            img_PIL.save(os.path.join(path, name))

    def file_name_no_path(self):
        return os.path.basename(self.file_name)
