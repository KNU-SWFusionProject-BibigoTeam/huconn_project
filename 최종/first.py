import sys

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
from PyQt5 import uic
import second
from second import *
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
import gpio

import cv2
import numpy as np

class Worker(QThread):
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
    def run(self):
        while True:
            gpio.setup()
            try:
                
                gpio.loop()

                # light
                self.parent.funtion_lightOn()
                # window
                self.parent.funtion_windowOn()
                # door
                self.parent.funtion_DoorOn()
                # Klaxon
                if gpio.onOff[3] == True:
                    self.parent.Klaxon()
                # Gear
                if gpio.Gearclicked == 1:
                    self.parent.GearP()
                elif gpio.Gearclicked == 2:
                    self.parent.GearR()
                elif gpio.Gearclicked == 3:
                    self.parent.GearN()
                elif gpio.Gearclicked == 4:
                    self.parent.GearD()
                elif gpio.Gearclicked == 0:
                    self.parent.GearE()
                # Start
                self.parent.funtion_start()
                # Break
                self.parent.funtion_break()
                
                self.parent.cam_open()
                


            except KeyboardInterrupt:
                print("keyboard interrupt detected")
                gpio.endprogram()
                break
            finally:
                gpio.endprogram()

#  영상 클래스(미완성)
class Thread(QThread):
       working = True
       cap = None
       
       changePixmap = pyqtSignal(QImage, np.ndarray)
       recordVideo = pyqtSignal(QImage)

       def run(self):

           self.cap = cv2.VideoCapture(0)  # 0번 카메라 연결
           
           while self.working:  # 영상 가져오기 무한 반복
               time.sleep(0.005)  # 영상 1프레임당 0.01초로 이걸로 영상 재생속도 조절하면됨 0.02로하면 0.5배속인거임
               ret, frame = self.cap.read()  # 카메라에서 영상 받기 (넘파이 배열)
               if not ret:
                   #self.cap = cv2.VideoCapture(0)
                   continue  # 영상이 없으면 (동영상 끝 등) 반복 종료
               # 제대로 1배속 하려면 여기서 동영상의 초당 프레임수의 역수만큼 기다려야 할 듯

               rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB 변환
               h, w, ch = rgbImage.shape  # 영상의 세로, 가로, 채널수
               bytes_per_line = ch * w

               cvc = QImage(rgbImage.data, w, h, bytes_per_line, QImage.Format_RGB888)

               self.changePixmap.emit(cvc.scaled(360, 360, Qt.IgnoreAspectRatio), frame)

           self.cap.release()
        

              


form_main = uic.loadUiType("first.ui")[0]

class MainWindow(QMainWindow,form_main):
   def __init__(self):
    super().__init__()
    self.initUI()

    self.second = secondwindow()
    self.worker = Worker(self)
    self.th = Thread(self)
    self.th.start()

    self.worker.start()
    self.show()

   def initUI(self):

       self.setupUi(self)
       self.base = QPixmap()
       self.base.load(".png")

       
       self.base = self.base.scaled(1011, 741)
       self.insideCar.setPixmap(self.base)
       
       self.pushButton.clicked.connect(self.button_Second)
       self.pushButton.setFlat(True)

       self.qPixmapFileVar = QPixmap()
       self.qPixmapFileVar.load("insideCar.png")
       self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
       self.insideCar.setPixmap(self.qPixmapFileVar)
       

   def button_Second(self):
       self.second.show()
       self.second.exec_()


   def cam_open(self):
       if gpio.onOff[6] == True:
       #if self.videoButton.isChecked():
          self.th.working = True  # 영상 읽어오기 반복 여부 참
          self.th.changePixmap.connect(self.setImage)
          self.th.start()

       else:

          self.th.working = False  # 영상 읽어오기 반복 여부 거짓
          
          qPixmapFileVar = QPixmap()
          qPixmapFileVar.load("")
          
          self.video_viewer_label.setPixmap(qPixmapFileVar)
          self.insideCar_5.setPixmap(qPixmapFileVar)
          #self.th.quit()
          
          #self.th.exec_()


   # 라벨에 이미지 출력하기 함수
   def setImage(self, image):
       self.video_viewer_label.setPixmap(QPixmap.fromImage(image))


# 클락션 함수 수정
   def Klaxon(self):
        #QTimer.singleShot(3000, self.KlaxonOff)
        qPixmapFileVar = QPixmap()
        qPixmapFileVar.load("pushimage.png")
        qPixmapFileVar = qPixmapFileVar.scaled(1011, 741)
        self.insideCar_5.setPixmap(qPixmapFileVar)
        gpio.horn_start()
        self.KlaxonOff()

   def KlaxonOff(self):
       qPixmapFileVar = QPixmap()
       qPixmapFileVar.load("")
       self.insideCar_5.setPixmap(qPixmapFileVar)


   def GearE(self):
        if gpio.Gearclicked == 0:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Insidecar.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
        else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)

   def GearP(self):
       if gpio.Gearclicked == 1:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Pimage.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
       else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)

   def GearR(self):
       if gpio.Gearclicked == 2:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Rimage.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
       else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)

   def GearN(self):
       if gpio.Gearclicked == 3:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Nimage.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
       else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)

   def GearD(self):
       if gpio.Gearclicked == 4:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("Dimage.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)
       else:
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_2.setPixmap(self.qPixmapFileVar)


# ligth function
   def funtion_lightOn(self):
       #if self.lightButton.isChecked():
       if gpio.onOff[0] == True:
           self.light = QPixmap()
           self.light.load("Insidelight.png")
           self.light = self.light.scaled(1011, 741)
           self.insideCar_4.setPixmap(self.light)

           self.second.funtion_lightOn()
       elif gpio.onOff[0] == False:
           self.light = QPixmap()
           self.light.load("")
           self.light = self.light.scaled(1011, 741)
           self.insideCar_4.setPixmap(self.light)

           self.second.funtion_lightOff()


# window function 함수들에 조건문
   def funtion_windowOn(self):
       
       if gpio.onOff[2] == True:
           if gpio.onOff[1] == True:
               self.OpenDoor = QPixmap()
               self.OpenDoor.load("DOWO.png")
               self.OpenDoor = self.OpenDoor.scaled(1011, 741)
               self.insideCar.setPixmap(self.OpenDoor)

               self.second.funtion_DOWO()

           elif gpio.onOff[1] == False:
               self.DoorAndWindowOpen = QPixmap()
               self.DoorAndWindowOpen.load("DOWC.png")
               self.DoorAndWindowOpen = self.DoorAndWindowOpen.scaled(1011, 741)
               self.insideCar.setPixmap(self.DoorAndWindowOpen)

               self.second.funtion_DOWC()

       if gpio.onOff[2] == False:
            if gpio.onOff[1] == True:
               self.base = QPixmap()
               self.base.load("DCWO.png")
               self.base = self.base.scaled(1011, 741)
               self.insideCar.setPixmap(self.base)

               self.second.funtion_DCWO()
            
            elif gpio.onOff[1] == False:
               self.Open_window = QPixmap()
               self.Open_window.load("insideCar")
               self.Open_window = self.Open_window.scaled(1011, 741)
               self.insideCar.setPixmap(self.Open_window)

               self.second.funtion_DCWC()

# door function
   def funtion_DoorOn(self):

       if gpio.onOff[1] == True: 
           if gpio.onOff[2] == True: 
               self.DoorAndWindowOpen = QPixmap()
               self.DoorAndWindowOpen.load("DOWO.png")
               self.DoorAndWindowOpen = self.DoorAndWindowOpen.scaled(1011, 741)
               self.insideCar.setPixmap(self.DoorAndWindowOpen)

               self.second.funtion_DOWO()
           elif gpio.onOff[2] == False:
               self.Open_window = QPixmap()
               self.Open_window.load("DCWO")
               self.Open_window = self.Open_window.scaled(1011, 741)
               self.insideCar.setPixmap(self.Open_window)

               self.second.funtion_DCWO()

       if gpio.onOff[1] == False:
           #if self.DoorButton.isChecked() == True:
           if gpio.onOff[2] == True:
               self.OpenDoor = QPixmap()
               self.OpenDoor.load("DOWC.png")
               self.OpenDoor = self.OpenDoor.scaled(1011, 741)
               self.insideCar.setPixmap(self.OpenDoor)

               self.second.funtion_DOWC()
           elif gpio.onOff[2] == False:
               self.base = QPixmap()
               self.base.load("insideCar.png")
               self.base = self.base.scaled(1011, 741)
               self.insideCar.setPixmap(self.base)

               self.second.funtion_DCWC()

   def funtion_start(self):
        if gpio.onOff[4] == True:
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("car_speed.png")
            self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
            self.insideCar_6.setPixmap(self.qPixmapFileVar)
        else:
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("")
            self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
            self.insideCar_6.setPixmap(self.qPixmapFileVar)


   def funtion_break(self):
       #if self.breakButton.isChecked():
       if gpio.onOff[5] == True:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("break_image.png")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_7.setPixmap(self.qPixmapFileVar)

           self.second.funtion_BREON()

       else:
           self.qPixmapFileVar = QPixmap()
           self.qPixmapFileVar.load("")
           self.qPixmapFileVar = self.qPixmapFileVar.scaled(1011, 741)
           self.insideCar_7.setPixmap(self.qPixmapFileVar)

           self.second.funtion_BREOFF()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    
    if app.exec_() == 0:
        gpio.endprogram()
        sys.exit(0)
