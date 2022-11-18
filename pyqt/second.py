import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_secondwindow = uic.loadUiType("second.ui")[0]

class secondwindow(QDialog, form_secondwindow):
   def __init__(self):
      super(secondwindow,self).__init__()
      self.initUI()
      self.show()


   def initUI(self):
    self.setupUi(self)
    self.BackButton.clicked.connect(self.Home)
    self.move(750,25)


# light
    self.lightOn.clicked.connect(self.funtion_lightOn)
    self.lightOff.clicked.connect(self.funtion_lightOff)

#window


    if self.WindowOn.clicked:
        self.WindowOn.setCheckable(True)
        self.WindowOn.clicked.connect(self.funtion_windowOn)


    if self.WindowOff.clicked:
        self.WindowOff.setCheckable(True)
        self.WindowOff.clicked.connect(self.funtion_windowOff)




#Door
    if self.DoorOn.clicked:
        self.DoorOn.setCheckable(True)
        self.DoorOn.clicked.connect(self.funtion_DoorOn)

    if self.DoorOff.clicked:
        self.DoorOff.setCheckable(True)
        self.DoorOff.clicked.connect(self.funtion_DoorOff)




   def Home(self):
    self.close()


# ligth function
   def funtion_lightOn(self):

    if self.WindowOff.isChecked() and self.DoorOn.isChecked():
        self.base = QPixmap()
        self.base.load("DoorAndWindowOpen.png")
        self.base = self.base.scaled(851, 531)
        self.label_base.setPixmap(self.base)

    if self.WindowOff.isChecked():
       self.base = QPixmap()
       self.base.load("Open_window.png")
       self.base = self.base.scaled(851, 531)
       self.label_base.setPixmap(self.base)


    elif self.DoorOn.isChecked():
         self.base = QPixmap()
         self.base.load("OpenDoor.png")
         self.base = self.base.scaled(851, 531)
         self.label_base.setPixmap(self.base)


    else:
        self.base = QPixmap()
        self.base.load("base.png")
        self.base = self.base.scaled(851, 531)
        self.label_base.setPixmap(self.base)

    if self.DoorOff.isChecked():
        self.base = QPixmap()
        self.base.load("base.png")
        self.base = self.base.scaled(851, 531)
        self.label_base.setPixmap(self.base)


    self.light = QPixmap()
    self.light.load("UplightOn.png")
    self.light = self.light.scaled(261, 531)
    self.label_light.setPixmap(self.light)

   def funtion_lightOff(self):
       self.light = QPixmap()
       self.light.load("")
       self.label_light.setPixmap(self.light)


# window function 함수들에 조건문
   def funtion_windowOn(self):
       self.base = QPixmap()
       self.base.load("base.png")
       self.base = self.base.scaled(851, 531)
       self.label_base.setPixmap(self.base)

       if self.DoorOn.isChecked():
           self.doorOn = QPixmap()
           self.doorOn.load("OpenDoor.png")
           self.doorOn = self.doorOn.scaled(851, 531)
           self.label_base.setPixmap(self.doorOn)




   def funtion_windowOff(self):
      self.window_Open = QPixmap()
      self.window_Open.load("Open_window.png")
      self.window_Open = self.window_Open.scaled(851, 531)
      self.label_base.setPixmap(self.window_Open)



# door function
   def funtion_DoorOn(self):
       self.doorOn = QPixmap()
       self.doorOn.load("OpenDoor.png")
       self.doorOn = self.doorOn.scaled(851, 531)
       self.label_base.setPixmap(self.doorOn)

       if self.WindowOff.isChecked():
           self.DoorOnAndWindowOpen = QPixmap()
           self.DoorOnAndWindowOpen.load("DoorAndWindowOpen.png")
           self.DoorOnAndWindowOpen = self.DoorOnAndWindowOpen.scaled(851, 531)
           self.label_base.setPixmap(self.DoorOnAndWindowOpen)



   def funtion_DoorOff(self):
       if self.WindowOff.isChecked():
           self.base = QPixmap()
           self.base.load("Open_window.png")
           self.base = self.base.scaled(851, 531)
           self.label_base.setPixmap(self.base)


       else:
           self.base = QPixmap()
           self.base.load("base.png")
           self.base = self.base.scaled(851, 531)
           self.label_base.setPixmap(self.base)




       if self.WindowOn.isChecked():
           if self.WindowOff.isChecked():
               self.base = QPixmap()
               self.base.load("base.png")
               self.base = self.base.scaled(851, 531)
               self.label_base.setPixmap(self.base)



