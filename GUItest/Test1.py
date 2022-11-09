import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("GUItest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("base1.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base1.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load("window_close.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base2.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load("base3.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base3.setPixmap(self.qPixmapFileVar)

        self.Light_On.clicked.connect(self.LightOn)
        self.Light_Off.clicked.connect(self.Return)

        self.Window_open.clicked.connect(self.Window)
        self.Window_close.clicked.connect(self.Return)

    def LightOn(self):
        self.qPixmapFileVar.load("light1.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base1.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load("light2.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base2.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load("light3.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base3.setPixmap(self.qPixmapFileVar)

    def Window(self):
        self.qPixmapFileVar.load("window_open.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base2.setPixmap(self.qPixmapFileVar)

    def Return(self):
        self.qPixmapFileVar.load("base1.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base1.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load("window_close.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base2.setPixmap(self.qPixmapFileVar)

        self.qPixmapFileVar.load("base3.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.Base3.setPixmap(self.qPixmapFileVar)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()