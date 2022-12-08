import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic

from first import *

form_secondwindow = uic.loadUiType("second.ui")[0]

class secondwindow(QDialog, form_secondwindow):
   def __init__(self):
      super(secondwindow,self).__init__()
      self.initUI()
#      self.show()



   def initUI(self):
    self.setupUi(self)
#    self.BackButton.clicked.connect(self.Home)
    self.move(750,25)

    self.base = QPixmap()
    self.base.load("base.png")
    self.base = self.base.scaled(851, 531)
    self.label_base.setPixmap(self.base)


# ligth function
   def funtion_lightOn(self):
          self.light = QPixmap()
          self.light.load("light_On.png")
          self.light = self.light.scaled(261, 531)
          self.label_light.setPixmap(self.light)

   def funtion_lightOff(self):
       self.light = QPixmap()
       self.light.load(".png")
       self.label_light.setPixmap(self.light)

   def funtion_DOWO(self): # 문 열림 & 창문 열림
       self.OpenDoor = QPixmap()
       self.OpenDoor.load("DoorAndWindowOpen.png")
       self.OpenDoor = self.OpenDoor.scaled(851, 531)
       self.label_base.setPixmap(self.OpenDoor)

   def funtion_DOWC(self): # 문 열림 & 창문 닫힘
       self.OpenDoor = QPixmap()
       self.OpenDoor.load("OpenDoor.png")
       self.OpenDoor = self.OpenDoor.scaled(851, 531)
       self.label_base.setPixmap(self.OpenDoor)

   def funtion_DCWO(self): # 문 닫힘 & 창문 열림
       self.OpenDoor = QPixmap()
       self.OpenDoor.load("Open_window.png")
       self.OpenDoor = self.OpenDoor.scaled(851, 531)
       self.label_base.setPixmap(self.OpenDoor)

   def funtion_DCWC(self): # 문 닫힘 & 창문 닫힘
       self.OpenDoor = QPixmap()
       self.OpenDoor.load("base.png")
       self.OpenDoor = self.OpenDoor.scaled(851, 531)
       self.label_base.setPixmap(self.OpenDoor)

   def funtion_BREON(self):
       self.BreakOn = QPixmap()
       self.BreakOn.load("BreakOn.png")
       self.BreakOn = self.BreakOn.scaled(851, 531)
       self.break_light.setPixmap(self.BreakOn)

   def funtion_BREOFF(self):
       self.base = QPixmap()
       self.base.load("")
       self.base = self.base.scaled(851, 531)
       self.break_light.setPixmap(self.base)
