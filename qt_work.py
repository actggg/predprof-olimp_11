from FileWorker import FileWorker
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 500)
        MainWindow.setWindowTitle("Главный экран")

        self.label = QtWidgets.QLabel(MainWindow)   # текст выбора
        self.label.setGeometry(80, 30, 560, 30)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.setText("Выберите файл, который хотите проанализировать")

        self.lineEdit = QtWidgets.QLineEdit(MainWindow)  # поле ввода пути
        self.lineEdit.setGeometry(80, 60, 450, 30)
        self.lineEdit.setStyleSheet("color: rgb(150, 150, 150);")
        self.lineEdit.setText("Путь к файлу")
        self.lineEdit.setObjectName("lineEdit")


        self.pushButton = QtWidgets.QPushButton(MainWindow)  # кнопка, выбор файла для анализа
        self.pushButton.setGeometry(540, 60, 100, 30)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton.setText("Выбрать")
        self.labels_for_img()

        self.button = QtWidgets.QPushButton(MainWindow)  # кнопка, выбор директории и скачивания изображения
        self.button.setGeometry(360, 360, 160, 50)
        self.button.setText("Скачать изображение")
        self.button.pressed.connect(self.download_file)
        self.button.hide()

        self.button2 = QtWidgets.QPushButton(MainWindow)  # кнопка, скачивание количества контуров
        self.button2.setGeometry(150, 360, 200, 50)
        self.button2.setText("Посчитать количество контуров")
        self.button2.pressed.connect(self.save_in_csv)
        self.button2.hide()

    def download_file(self):  # функция, скачивание обработанного изображения
        try:
            dirlist = QtWidgets.QFileDialog.getExistingDirectory(None, "Выбрать папку", ".")
            self.label_download.show()
            self.file_f.save_photo(img=self.img, path='\\'.join(dirlist.split("/")), subdir=None, name=self.file_f.file_name_no_path())
        except Exception as e:
            print(e)

    def save_in_csv(self):  # функция, скачивание количества контуров
        try:
            self.label_download2.show()
            self.file_f.save_csv(self.file_f.file_name_no_path())
        except Exception as e:
            print(e)


    def labels_for_img(self):
        self.label_photo = QtWidgets.QLabel(MainWindow)  # изображение 1
        self.label_photo.setObjectName("label")
        self.label_photo.setGeometry(80, 105, 240, 240)

        self.label_photo2 = QtWidgets.QLabel(MainWindow)  # изображение 2
        self.label_photo2.setObjectName("label")
        self.label_photo2.setGeometry(390, 105, 240, 240)

        self.label_arrow = QtWidgets.QLabel(MainWindow)  # изображение стрелка
        self.label_arrow.setObjectName("label")
        self.label_arrow.setGeometry(334, 200, 45, 45)

        self.label_mistake = QtWidgets.QLabel(MainWindow)  # вывод ошибки, строка 1
        self.label_mistake.setObjectName("label")
        self.label_mistake.setGeometry(80, 90, 500, 40)
        self.label_mistake.setText("Размер файла не соответствует 240 х 240 пикселей, предпросмотр недоступен")

        self.label_mistake2 = QtWidgets.QLabel(MainWindow)  # вывод ошибки, строка 1
        self.label_mistake2.setObjectName("label")
        self.label_mistake2.setGeometry(80, 130, 500, 40)
        self.label_mistake2.setText("Скачивание и анализ контуров доступны к использованию")

        self.label_mistake2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_mistake.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        self.label_mistake2.hide()
        self.label_mistake.hide()

        self.label_download = QtWidgets.QLabel(MainWindow)  # уведомление 1
        self.label_download.setObjectName("label")
        self.label_download.setText("Изображение успешно скачано")
        self.label_download.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_download.setGeometry(80, 420, 500, 50)
        self.label_download.hide()

        self.label_download2 = QtWidgets.QLabel(MainWindow)  # уведомление 2
        self.label_download2.setObjectName("label")
        self.label_download2.setText("Проанализировано, результат в файле templates_out.csv")
        self.label_download2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_download2.setGeometry(80, 450, 500, 50)
        self.label_download2.hide()


    def open_file(self):   # обработка информации
        try:
            self.file_name = QtWidgets.QFileDialog.getOpenFileName(None, "Open", "", "JPG Files (*.jpg)")
        except Exception as e:
            print(e)
        if self.file_name[0] != '':
            self.lineEdit.setText(self.file_name[0])
            self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
            self.file_f = FileWorker(self.file_name[0])
            self.img = self.file_f.set_contours()
            self.button.show()
            self.button2.show()
            self.label_download.hide()
            self.label_download2.hide()
            if self.file_f.width == 240 and self.file_f.height == 240:
                self.label_photo.show()
                self.label_photo2.show()
                self.label_arrow.show()


                pixmap = QPixmap(self.file_name[0])
                self.label_photo.setPixmap(pixmap)

                h, w = 240, 240

                qimage = QImage(self.img.data, w, h, 3 * w, QImage.Format_RGB888).rgbSwapped()


                qimage = QPixmap.fromImage(qimage)
                self.label_photo2.setPixmap(qimage)

                pixmap = QPixmap('templates/arrow.png')
                self.label_arrow.setPixmap(pixmap)

                self.label_mistake2.hide()
                self.label_mistake.hide()
            else:
                self.label_photo.hide()
                self.label_photo2.hide()
                self.label_arrow.hide()
                self.label_mistake2.show()
                self.label_mistake.show()



if __name__ == "__main__":  # запуск
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())