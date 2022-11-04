import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("Moring.ui")[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setGeometry(1300, 1500, 1400, 1300)

        self.Button_test.setCheckable(True)
        self.Button_test.clicked.connect(self.loadImageFromFile2)

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("Moring_test.jpeg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(1100, 669)
        self.label_test.setPixmap(self.qPixmapFileVar)

        self.label_test.setGeometry(190, 30, 1181, 669)
        self.Button_test.setGeometry(670, 750, 100, 100) # x,y,가로 세로



    def loadImageFromFile2(self,state):
     # QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시

     if self.Button_test.isChecked():
          self.Button_test.setText("OFF")
          qPixmapFileVar = QPixmap()
          qPixmapFileVar.load("testImage.png")
          qPixmapFileVar = qPixmapFileVar.scaled(100, 100)
          self.right_light.setPixmap(qPixmapFileVar)
     else:
         self.Button_test.setText("ON")
         qPixmapFileVar = QPixmap()
         qPixmapFileVar.load("")
         self.right_light.setPixmap(qPixmapFileVar)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
