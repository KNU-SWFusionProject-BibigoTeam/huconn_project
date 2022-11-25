import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic
import second
from second import *

## 화면에따라 사이즈가 바뀌게
## 연결하면 새로 이미지 뜸


form_main = uic.loadUiType("first.ui")[0]



class MainWindow(QMainWindow,form_main):
   def __init__(self):
    super().__init__()
    self.initUI()
    self.show()





   def initUI(self):

       self.setupUi(self)
       self.pushButton.clicked.connect(self.button_Second)
      # self.second = secondwindow()
      # self.lightOn.clicked.connect(lambda:self.second.funtion_lightOn())
       self.base = QPixmap()
       self.base.load(".png")
       self.base = self.base.scaled(851, 531)
       self.insideCar.setPixmap(self.base)

       self.clockshtion.setCheckable(True)
       self.clockshtion.clicked.connect(self.Klaxon)

       self.qPixmapFileVar = QPixmap()
       self.qPixmapFileVar.load("carimage.png")
       self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
       self.insideCar.setPixmap(self.qPixmapFileVar)



       self.radio1 = QRadioButton("radio1", self)
       self.radioButton.clicked.connect(self.radio1_fun)

       self.radio2 = QRadioButton("radio2", self)
       self.radioButton_2.clicked.connect(self.radio2_fun)

       self.radio3 = QRadioButton("radio3", self)
       self.radioButton_3.clicked.connect(self.radio3_fun)

       self.radio3 = QRadioButton("radio4", self)
       self.radioButton_4.clicked.connect(self.radio4_fun)


       self.lightOn.clicked.connect(self.lightAction)
       self.lightOff.clicked.connect(self.lightActionOFF)

   def Klaxon(self, state):
       if self.clockshtion.isChecked():
           self.clockshtion.setText("OFF")
           qPixmapFileVar = QPixmap()
           qPixmapFileVar.load("pushimage.png")
           qPixmapFileVar = qPixmapFileVar.scaled(600, 500)
           self.insideCar_4.setPixmap(qPixmapFileVar)
       else:
           self.clockshtion.setText("Push")
           qPixmapFileVar = QPixmap()
           qPixmapFileVar.load("")
           self.insideCar_4.setPixmap(qPixmapFileVar)

   def radio1_fun(self, checked):
       if checked:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Rimage.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
       else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)

   def radio2_fun(self, checked):
       if checked:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Pimage.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
       else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)

   def radio3_fun(self, checked):
       if checked:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Nimage.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
       else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)

   def radio4_fun(self, checked):
       if checked:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Dimage.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
       else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)

   def button_Second(self):
       self.second = secondwindow()
       self.second.exec_()
       self.show()




   def lightAction(self):
        self.second = secondwindow()
        self.second.funtion_lightOn2()
       # self.second.hide()

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("insideCar_light.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.insideCar.setPixmap(self.qPixmapFileVar)

   def lightActionOFF(self):
       self.second = secondwindow()
       self.second.funtion_lightOff2()


       self.qPixmapFileVar = QPixmap()
       self.qPixmapFileVar.load("carimage.png")
       self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
       self.insideCar.setPixmap(self.qPixmapFileVar)


   def lightAction2(self):
       self.qPixmapFileVar = QPixmap()
       self.qPixmapFileVar.load("insideCar_light.png")
       self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
       self.insideCar.setPixmap(self.qPixmapFileVar)

   def lightActionOFF2(self):
       self.qPixmapFileVar = QPixmap()
       self.qPixmapFileVar.load("carimage.png")
       self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
       self.insideCar.setPixmap(self.qPixmapFileVar)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

