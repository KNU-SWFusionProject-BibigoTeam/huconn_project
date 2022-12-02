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
       self.base = self.base.scaled(600, 500)
       self.insideCar.setPixmap(self.base)

       self.clockshtion.setCheckable(True)
       self.clockshtion.clicked.connect(self.Klaxon)

       self.qPixmapFileVar = QPixmap()
       self.qPixmapFileVar.load("carimage.png")
       self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
       self.insideCar.setPixmap(self.qPixmapFileVar)


# 기어 버튼 4개
       self.radio1 = QRadioButton("radio1", self)
       self.radioButton.clicked.connect(self.radio1_fun)

       self.radio2 = QRadioButton("radio2", self)
       self.radioButton_2.clicked.connect(self.radio2_fun)

       self.radio3 = QRadioButton("radio3", self)
       self.radioButton_3.clicked.connect(self.radio3_fun)

       self.radio3 = QRadioButton("radio4", self)
       self.radioButton_4.clicked.connect(self.radio4_fun)

# light
       self.lightButton.setCheckable(True)
       self.lightButton.clicked.connect(self.funtion_lightOn)

# window
       self.WindowButton.setCheckable(True)
       self.WindowButton.clicked.connect(self.funtion_windowOn)

# Door
       self.DoorButton.setCheckable(True)
       self.DoorButton.clicked.connect(self.funtion_DoorOn)

       # self.lightOn.clicked.connect(self.lightAction)
       # self.lightOff.clicked.connect(self.lightActionOFF)

   def Klaxon(self, state):
       if self.clockshtion.isChecked():
           self.clockshtion.setText("OFF")
           qPixmapFileVar = QPixmap()
           qPixmapFileVar.load("pushimage.png")
           qPixmapFileVar = qPixmapFileVar.scaled(600, 500)
           self.insideCar_5.setPixmap(qPixmapFileVar)
       else:
           self.clockshtion.setText("Push")
           qPixmapFileVar = QPixmap()
           qPixmapFileVar.load("")
           self.insideCar_5.setPixmap(qPixmapFileVar)

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

# ligth function
   def funtion_lightOn(self):
       if self.lightButton.isChecked():

           self.lightButton.setText("OFF")
           self.light = QPixmap()
           self.light.load("light.png")
           self.light = self.light.scaled(600, 500)
           self.insideCar_4.setPixmap(self.light)

           self.second = secondwindow()
           self.second.funtion_lightOn2()

       else:
           self.lightButton.setText("ON")
           self.light = QPixmap()
           self.light.load("")
           self.light = self.light.scaled(600, 500)
           self.insideCar_4.setPixmap(self.light)

           self.second = secondwindow()
           self.second.funtion_lightOff2()



   def funtion_lightOn2(self):
        self.lightButton.setText("OFF")
        self.light = QPixmap()
        self.light.load("light.jpg")
        self.light = self.light.scaled(600, 500)
        self.insideCar_4.setPixmap(self.light)

   def funtion_lightOFF2(self):
       self.lightButton.setText("ON")
       self.light = QPixmap()
       self.light.load("")
       self.light = self.light.scaled(600, 500)
       self.insideCar_4.setPixmap(self.light)






# window function 함수들에 조건문
   def funtion_windowOn(self):

       if self.DoorButton.isChecked() == True:
           if self.WindowButton.isChecked() == True:
               self.WindowButton.setText("OFF")
               self.OpenDoor = QPixmap()
               self.OpenDoor.load("DOWO.png")
               self.OpenDoor = self.OpenDoor.scaled(600, 500)
               self.insideCar.setPixmap(self.OpenDoor)

       if self.DoorButton.isChecked() == True:
           if self.WindowButton.isChecked() == False:  # 창문 아무것도 없는 상태
               self.WindowButton.setText("ON")
               self.DoorAndWindowOpen = QPixmap()
               self.DoorAndWindowOpen.load("DOWC.png")
               self.DoorAndWindowOpen = self.DoorAndWindowOpen.scaled(600, 500)
               self.insideCar.setPixmap(self.DoorAndWindowOpen)

       if self.DoorButton.isChecked() == False:
           if self.WindowButton.isChecked() == True:
               self.WindowButton.setText("OFF")
               self.base = QPixmap()
               self.base.load("DCWO.png")
               self.base = self.base.scaled(600, 500)
               self.insideCar.setPixmap(self.base)

       if self.DoorButton.isChecked() == False:
           if self.WindowButton.isChecked() == False:
               self.WindowButton.setText("ON")
               self.Open_window = QPixmap()
               self.Open_window.load("carimage")
               self.Open_window = self.Open_window.scaled(600, 500)
               self.insideCar.setPixmap(self.Open_window)

# door function
   def funtion_DoorOn(self):

       if self.WindowButton.isChecked() == True:
           if self.DoorButton.isChecked() == True:
               self.DoorButton.setText("OFF")
               self.DoorAndWindowOpen = QPixmap()
               self.DoorAndWindowOpen.load("DOWO.png")
               self.DoorAndWindowOpen = self.DoorAndWindowOpen.scaled(600, 500)
               self.insideCar.setPixmap(self.DoorAndWindowOpen)

       if self.WindowButton.isChecked() == True:
           if self.DoorButton.isChecked() == False:
               self.DoorButton.setText("ON")
               self.Open_window = QPixmap()
               self.Open_window.load("DCWO")
               self.Open_window = self.Open_window.scaled(600, 500)
               self.insideCar.setPixmap(self.Open_window)

       if self.WindowButton.isChecked() == False:  # 창문 아무것도 없는 상태
           if self.DoorButton.isChecked() == True:
               self.DoorButton.setText("OFF")
               self.OpenDoor = QPixmap()
               self.OpenDoor.load("DOWC.png")
               self.OpenDoor = self.OpenDoor.scaled(600, 500)
               self.insideCar.setPixmap(self.OpenDoor)

       if self.WindowButton.isChecked() == False:
           if self.DoorButton.isChecked() == False:
               self.DoorButton.setText("ON")
               self.base = QPixmap()
               self.base.load("carimage.png")
               self.base = self.base.scaled(600, 500)
               self.insideCar.setPixmap(self.base)

   def button_Second(self):
       self.second = secondwindow()
       self.second.exec_()
       self.show()




   # def lightAction(self):
   #      self.second = secondwindow()
   #      self.second.funtion_lightOn2()
   #     # self.second.hide()
   #
   #      self.qPixmapFileVar = QPixmap()
   #      self.qPixmapFileVar.load("insideCar_light.png")
   #      self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
   #      self.insideCar.setPixmap(self.qPixmapFileVar)
   #
   # def lightActionOFF(self):
   #     self.second = secondwindow()
   #     self.second.funtion_lightOff2()
   #
   #
   #     self.qPixmapFileVar = QPixmap()
   #     self.qPixmapFileVar.load("carimage.png")
   #     self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
   #     self.insideCar.setPixmap(self.qPixmapFileVar)
   #
   #
   # def lightAction2(self):
   #     self.qPixmapFileVar = QPixmap()
   #     self.qPixmapFileVar.load("insideCar_light.png")
   #     self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
   #     self.insideCar.setPixmap(self.qPixmapFileVar)
   #
   # def lightActionOFF2(self):
   #     self.qPixmapFileVar = QPixmap()
   #     self.qPixmapFileVar.load("carimage.png")
   #     self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
   #     self.insideCar.setPixmap(self.qPixmapFileVar)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

