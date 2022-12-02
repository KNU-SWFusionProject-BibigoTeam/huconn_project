import sys
from time import sleep

import cv2
from PyQt5 import uic
from PyQt5.QtGui import QImage

from second import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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


       self.base = QPixmap()
       self.base.load(".png")
       self.base = self.base.scaled(600, 500)
       self.insideCar.setPixmap(self.base)

       self.clockshtion.clicked.connect(self.Klaxon)

       self.qPixmapFileVar = QPixmap()
       self.qPixmapFileVar.load("insideCar.png")
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

       self.breakButton.setCheckable(True)
       self.breakButton.clicked.connect(self.funtion_break)

# 두번째 창으로
       self.GoButton.setCheckable(True)
       self.GoButton.clicked.connect(self.GoNext)

# 영상?
       self.videoButton.clicked.connect(self.Video_to_frame)



# 클락션 함수 수정
   def Klaxon(self):
       QTimer.singleShot(3000, self.KlaxonOff)
       self.clockshtion.setText("OFF")
       qPixmapFileVar = QPixmap()
       qPixmapFileVar.load("pushimage.png")
       qPixmapFileVar = qPixmapFileVar.scaled(600, 500)
       self.insideCar_5.setPixmap(qPixmapFileVar)


   def KlaxonOff(self):
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
           self.light.load("insidelight.png")
           self.light = self.light.scaled(600, 500)
           self.insideCar_4.setPixmap(self.light)

           if self.GoButton.isChecked():
              self.second.funtion_lightOn()

       else:
           self.lightButton.setText("ON")
           self.light = QPixmap()
           self.light.load("")
           self.light = self.light.scaled(600, 500)
           self.insideCar_4.setPixmap(self.light)

           if self.GoButton.isChecked():
              self.second.funtion_lightOff()


# window function 함수들에 조건문
   def funtion_windowOn(self):

       if self.DoorButton.isChecked() == True:
           if self.WindowButton.isChecked() == True:
               self.WindowButton.setText("OFF")
               self.OpenDoor = QPixmap()
               self.OpenDoor.load("DOWO.png")
               self.OpenDoor = self.OpenDoor.scaled(600, 500)
               self.insideCar.setPixmap(self.OpenDoor)

               if self.GoButton.isChecked():
                  self.second.funtion_DOWO()

       if self.DoorButton.isChecked() == True:
           if self.WindowButton.isChecked() == False:  # 창문 아무것도 없는 상태
               self.WindowButton.setText("ON")
               self.DoorAndWindowOpen = QPixmap()
               self.DoorAndWindowOpen.load("DOWC.png")
               self.DoorAndWindowOpen = self.DoorAndWindowOpen.scaled(600, 500)
               self.insideCar.setPixmap(self.DoorAndWindowOpen)

               if self.GoButton.isChecked():
                  self.second.funtion_DOWC()

       if self.DoorButton.isChecked() == False:
           if self.WindowButton.isChecked() == True:
               self.WindowButton.setText("OFF")
               self.base = QPixmap()
               self.base.load("DCWO.png")
               self.base = self.base.scaled(600, 500)
               self.insideCar.setPixmap(self.base)

               if self.GoButton.isChecked():
                  self.second.funtion_DCWO()

       if self.DoorButton.isChecked() == False:
           if self.WindowButton.isChecked() == False:
               self.WindowButton.setText("ON")
               self.Open_window = QPixmap()
               self.Open_window.load("insideCar")
               self.Open_window = self.Open_window.scaled(600, 500)
               self.insideCar.setPixmap(self.Open_window)

               if self.GoButton.isChecked():
                  self.second.funtion_DCWC()

# door function
   def funtion_DoorOn(self):

       if self.WindowButton.isChecked() == True:
           if self.DoorButton.isChecked() == True:
               self.DoorButton.setText("OFF")
               self.DoorAndWindowOpen = QPixmap()
               self.DoorAndWindowOpen.load("DOWO.png")
               self.DoorAndWindowOpen = self.DoorAndWindowOpen.scaled(600, 500)
               self.insideCar.setPixmap(self.DoorAndWindowOpen)

               if self.GoButton.isChecked():
                  self.second.funtion_DOWO()

       if self.WindowButton.isChecked() == True:
           if self.DoorButton.isChecked() == False:
               self.DoorButton.setText("ON")
               self.Open_window = QPixmap()
               self.Open_window.load("DCWO")
               self.Open_window = self.Open_window.scaled(600, 500)
               self.insideCar.setPixmap(self.Open_window)

               if self.GoButton.isChecked():
                  self.second.funtion_DCWO()

       if self.WindowButton.isChecked() == False:  # 창문 아무것도 없는 상태
           if self.DoorButton.isChecked() == True:
               self.DoorButton.setText("OFF")
               self.OpenDoor = QPixmap()
               self.OpenDoor.load("DOWC.png")
               self.OpenDoor = self.OpenDoor.scaled(600, 500)
               self.insideCar.setPixmap(self.OpenDoor)

               if self.GoButton.isChecked():
                  self.second.funtion_DOWC()

       if self.WindowButton.isChecked() == False:
           if self.DoorButton.isChecked() == False:
               self.DoorButton.setText("ON")
               self.base = QPixmap()
               self.base.load("insideCar.png")
               self.base = self.base.scaled(600, 500)
               self.insideCar.setPixmap(self.base)

               if self.GoButton.isChecked():
                  self.second.funtion_DCWC()






   def lightAction(self):

        self.second.funtion_lightOn2()

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("insideCar_light.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
        self.insideCar.setPixmap(self.qPixmapFileVar)

   def lightActionOFF(self):


       self.second.funtion_lightOff2()


       self.qPixmapFileVar = QPixmap()
       self.qPixmapFileVar.load("insideCar.png")
       self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
       self.insideCar.setPixmap(self.qPixmapFileVar)






   def funtion_break(self):
       if self.breakButton.isChecked():
           self.breakButton.setText("OFF")

           if self.GoButton.isChecked():
              self.second.funtion_BREON()


       else:
           self.breakButton.setText("ON")

           if self.GoButton.isChecked():
              self.second.funtion_BREOFF()


   def GoNext(self):

       if self.GoButton.isChecked():

          self.GoButton.setText("Back")
          self.second = secondwindow()
          self.second.exec_()
          self.show()

          self.GoButton.setCheckable(False)

       else:

          self.GoButton.setText("Go")
          self.second.close()
          self.GoButton.setCheckable(True)


#  영상(미완성)

   def Video_to_frame(self, MainWindow):

       cap = cv2.VideoCapture('04.mp4')  # 저장된 영상 가져오기 프레임별로 계속 가져오는 듯

       ###cap으로 영상의 프레임을 가지고와서 전처리 후 화면에 띄움###
       while True:
           self.ret, self.frame = cap.read()  # 영상의 정보 저장

           if self.ret:
               self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)  # 프레임에 색입히기
               self.convertToQtFormat = QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0],
                                               QImage.Format_RGB888)

               self.pixmap = QPixmap(self.convertToQtFormat)
               # self.p = self.pixmap.scaled(400, 300, QtCore.Qt.IgnoreAspectRatio)  # 프레임 크기 조정

               self.video_viewer_label.setPixmap(self.pixmap)
               self.video_viewer_label.update()  # 프레임 띄우기

               sleep(0.005)  # 영상 1프레임당 0.01초로 이걸로 영상 재생속도 조절하면됨 0.02로하면 0.5배속인거임



           else:
               break

       cap.release()
       cv2.destroyAllWindows()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
