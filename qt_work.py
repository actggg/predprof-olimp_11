import sys
import qimage2ndarray
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from FileWorker import FileWorker
from PyQt5.QtGui import QPixmap, QColor, QImage
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QMenuBar, QFileDialog, QApplication, QMainWindow


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(80, 30, 560, 30)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(80, 60, 450, 30)
        self.lineEdit.setStyleSheet("color: rgb(150, 150, 150);")
        self.lineEdit.setText("Путь к файлу")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)


        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(540, 60, 100, 30)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file)

        self.label_photo = QtWidgets.QLabel(MainWindow)
        self.label_photo.setObjectName("label")
        self.label_photo.setGeometry(80, 140, 340, 340)

        self.label_photo2 = QtWidgets.QLabel(MainWindow)
        self.label_photo2.setObjectName("label")
        self.label_photo2.setGeometry(390, 140, 640, 340)

        self.label_mistake = QtWidgets.QLabel(MainWindow)
        self.label_mistake.setObjectName("label")
        self.label_mistake.setGeometry(80, 140, 500, 40)
        self.label_mistake.setText("Привет, файл не стандартный, поэтому мы не можем показаеть его содержимое")

        self.label_mistake2 = QtWidgets.QLabel(MainWindow)
        self.label_mistake2.setObjectName("label")
        self.label_mistake2.setGeometry(80, 240, 500, 40)
        self.label_mistake2.setText("Однако ты все еще можешь скачать обработанную версию!!!")
        self.label_mistake2.hide()
        self.label_mistake.hide()

        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главный экран"))
        self.label.setText(_translate("MainWindow", "Выберите файл который хотите проанализировать"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать"))

    def open_file(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(None, "Open", "", "JPG Files (*.jpg)")
        if self.file_name[0] != '':
            file_f = FileWorker(self.file_name[0])
            if file_f.width == 240 and file_f.height == 240:
                try:
                    self.lineEdit.setText(self.file_name[0])
                    self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);")


                    pixmap = QPixmap(self.file_name[0])
                    self.label_photo.setPixmap(pixmap)

                    img = file_f.set_contours()
                    h, w = 240, 240

                    qimage = QImage(img.data, w, h, 3 * w, QImage.Format_RGB888).rgbSwapped()


                    qimage = QPixmap.fromImage(qimage)
                    self.label_photo2.setPixmap(qimage)
                    self.label_mistake2.hide()
                    self.label_mistake.hide()
                except Exception as e:
                    print(e)
            else:
                print(1)
                self.label_mistake2.show()
                self.label_mistake.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())