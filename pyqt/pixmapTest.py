import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("pixmapTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn_loadFromFile1.clicked.connect(self.loadImageFromFile1)
        self.btn_loadFromFile2.clicked.connect(self.loadImageFromFile2)



    def loadImageFromFile1(self) :
        #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("testImage.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(500,500)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)



    def loadImageFromFile2(self):
     # QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
     self.qPixmapFileVar = QPixmap()
     self.qPixmapFileVar.load("testImage2.png")
     self.qPixmapFileVar = self.qPixmapFileVar.scaled(500,500)
     self.lbl_picture.setPixmap(self.qPixmapFileVar)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()