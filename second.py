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
      self.show()



   def initUI(self):
    self.setupUi(self)
#    self.BackButton.clicked.connect(self.Home)
    self.move(750,25)

    self.base = QPixmap()
    self.base.load("base.png")
    self.base = self.base.scaled(851, 531)
    self.label_base.setPixmap(self.base)


# light

#    self.lightOn.setCheckable(True)
#   self.lightOn.clicked.connect(self.funtion_lightOn)


#window
#    self.WindowOn.setCheckable(True)
#    self.WindowOn.clicked.connect(self.funtion_windowOn)


#Door
#    self.DoorOn.setCheckable(True)
#    self.DoorOn.clicked.connect(self.funtion_DoorOn)

#Break
 #   self.breakOnButton.setCheckable(True)
 #   self.breakOnButton.clicked.connect(self.funtion_BreakOn)



   #def Home(self):
    #self.close()


# ligth function
   def funtion_lightOn(self):
       # if self.lightOn.isChecked():

          # self.lightOn.setText("OFF")
          self.light = QPixmap()
          self.light.load("light_On.png")
          self.light = self.light.scaled(261, 531)
          self.label_light.setPixmap(self.light)

          # self.first = MainWindow()
          # self.first.lightAction2()

       # else:
       #     # self.lightOn.setText("ON")
       #     self.light = QPixmap()
       #     self.light.load("")
       #     self.light = self.light.scaled(261, 531)
       #     self.label_light.setPixmap(self.light)

           # self.first = MainWindow()
           # self.first.lightActionOFF2()





   def funtion_lightOn2(self):

       # self.light = QPixmap()
       self.light.load("light_On.png")
       self.light = self.light.scaled(261, 531)
       self.label_light.setPixmap(self.light)

       # self.first = MainWindow()
       # self.first.lightAction2()

   def funtion_lightOff(self):
       self.light = QPixmap()
       self.light.load(".png")
       self.label_light.setPixmap(self.light)


   def funtion_lightOff2(self):
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

   # window function 함수들에 조건문
   def funtion_windowOn(self):
       if self.DoorOn.isChecked() == True:
           if self.WindowOn.isChecked() == True:  # 문 열림 & 창문 열림
               self.WindowOn.setText("OFF")
               self.OpenDoor = QPixmap()
               self.OpenDoor.load("DoorAndWindowOpen.png")
               self.OpenDoor = self.OpenDoor.scaled(851, 531)
               self.label_base.setPixmap(self.OpenDoor)

       if self.DoorOn.isChecked() == True:
           if self.WindowOn.isChecked() == False:  # 문 열림 & 창문 닫힘
               self.WindowOn.setText("ON")
               self.DoorAndWindowOpen = QPixmap()
               self.DoorAndWindowOpen.load("OpenDoor.png")
               self.DoorAndWindowOpen = self.DoorAndWindowOpen.scaled(851, 531)
               self.label_base.setPixmap(self.DoorAndWindowOpen)

       if self.DoorOn.isChecked() == False:
           if self.WindowOn.isChecked() == True:  # 문 닫힘 & 창문 열림
               self.WindowOn.setText("OFF")
               self.base = QPixmap()
               self.base.load("Open_window.png")
               self.base = self.base.scaled(851, 531)
               self.label_base.setPixmap(self.base)

       if self.DoorOn.isChecked() == False:
           if self.WindowOn.isChecked() == False:  # 문 닫힘 & 창문 닫힘
               self.WindowOn.setText("ON")
               self.Open_window = QPixmap()
               self.Open_window.load("base")
               self.Open_window = self.Open_window.scaled(851, 531)
               self.label_base.setPixmap(self.Open_window)







# door function
   def funtion_DoorOn(self):

       if self.WindowOn.isChecked() == True:
            if self.DoorOn.isChecked() == True:  # 문 열림 & 창문 열림
                self.DoorOn.setText("OFF")
                self.DoorAndWindowOpen = QPixmap()
                self.DoorAndWindowOpen.load("DoorAndWindowOpen.png")
                self.DoorAndWindowOpen = self.DoorAndWindowOpen.scaled(851, 531)
                self.label_base.setPixmap(self.DoorAndWindowOpen)

       if self.WindowOn.isChecked() == True:
            if self.DoorOn.isChecked() == False:  # 문 닫힘 & 창문 열림
                self.DoorOn.setText("ON")
                self.Open_window = QPixmap()
                self.Open_window.load("Open_window")
                self.Open_window = self.Open_window.scaled(851, 531)
                self.label_base.setPixmap(self.Open_window)

       if self.WindowOn.isChecked() == False:  # 문 열림 & 창문 닫힘
           if self.DoorOn.isChecked() == True:
               self.DoorOn.setText("OFF")
               self.OpenDoor = QPixmap()
               self.OpenDoor.load("OpenDoor.png")
               self.OpenDoor = self.OpenDoor.scaled(851, 531)
               self.label_base.setPixmap(self.OpenDoor)

       if self.WindowOn.isChecked() == False:
           if self.DoorOn.isChecked() == False:  # 문 닫힘 & 창문 닫힘
               self.DoorOn.setText("ON")
               self.base = QPixmap()
               self.base.load("base.png")
               self.base = self.base.scaled(851, 531)
               self.label_base.setPixmap(self.base)





#break_funtion
   def funtion_BreakOn(self):
       if self.breakOnButton.isChecked():

           self.breakOnButton.setText("OFF")
           self.BreakOn = QPixmap()
           self.BreakOn.load("BreakOn.png")
           self.BreakOn = self.BreakOn.scaled(851, 531)
           self.break_light.setPixmap(self.BreakOn)

       else:
           self.breakOnButton.setText("ON")
           self.base = QPixmap()
           self.base.load("")
           self.base = self.base.scaled(851, 531)
           self.break_light.setPixmap(self.base)




   #def Home(self):
          # self.first = MainWindow()
          # self.first.GoButton.setCheckable(False)
          # self.close()

