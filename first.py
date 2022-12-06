import sys
from time import sleep

import cv2
import numpy as np
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QImage, QPixmap

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

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

       self.th = Thread(self)




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

       self.videoButton.setCheckable(True)
       self.videoButton.clicked.connect(self.cam_open)


# 속도계
       self.startButton.setCheckable(True)
       self.startButton.clicked.connect(self.function_start)





   def cam_open(self):

       if self.videoButton.isChecked():
          self.videoButton.setText("Stop")

          self.th.working = True  # 영상 읽어오기 반복 여부 참
          self.th.changePixmap.connect(self.setImage)
          self.th.start()



       else:
          self.videoButton.setText("Go")

          self.th.working = False  # 영상 읽어오기 반복 여부 거짓
          self.th.exec_()




   # 라벨에 이미지 출력하기 함수
   def setImage(self, image):
       self.video_viewer_label.setPixmap(QPixmap.fromImage(image))



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


       else:

          self.GoButton.setText("Go")
          self.second.close()
        




   def function_start(self):
       if self.startButton.isChecked():

          self.startButton.setText("T")

          self.qPixmapFileVar = QPixmap()
          self.qPixmapFileVar.load("car_Speed.png")
          self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
          self.insideCar.setPixmap(self.qPixmapFileVar)

       else:

          self.qPixmapFileVar = QPixmap()
          self.qPixmapFileVar.load("insideCar.png")
          self.qPixmapFileVar = self.qPixmapFileVar.scaled(600, 500)
          self.insideCar.setPixmap(self.qPixmapFileVar)


#  영상 클래스(미완성)
class Thread(QThread):
       working = True
       cap = None
       video_path = "04.mp4"

       changePixmap = pyqtSignal(QImage, np.ndarray)
       recordVideo = pyqtSignal(QImage)

       def run(self):

           self.cap = cv2.VideoCapture(self.video_path)  # 0번 카메라 연결
           # self.cap = cv2.VideoCapture('move_file.avi')  # 동영상 파일
           while self.working:  # 영상 가져오기 무한 반복
               sleep(0.005)  # 영상 1프레임당 0.01초로 이걸로 영상 재생속도 조절하면됨 0.02로하면 0.5배속인거임
               ret, frame = self.cap.read()  # 카메라에서 영상 받기 (넘파이 배열)
               if not ret:
                   self.cap = cv2.VideoCapture(self.video_path)
                   continue  # 영상이 없으면 (동영상 끝 등) 반복 종료
               # 제대로 1배속 하려면 여기서 동영상의 초당 프레임수의 역수만큼 기다려야 할 듯

               rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB 변환
               h, w, ch = rgbImage.shape  # 영상의 세로, 가로, 채널수
               bytes_per_line = ch * w

               print(type(rgbImage.data))
               print(rgbImage.data)
               print(type(rgbImage))

               cvc = QImage(
                   rgbImage.data,
                   w, h, bytes_per_line,
                   QImage.Format_RGB888)

               self.changePixmap.emit(
                   cvc.scaled(640, 480, Qt.KeepAspectRatio),
                   frame)

           self.cap.release()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    sys.exit(app.exec_())
