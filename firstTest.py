import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from second import secondwindow


form_main = uic.loadUiType("first.ui")[0]

class MainWindow(QMainWindow,form_main):
   def __init__(self):
    super().__init__()
    self.initUI()
    self.show()



   def initUI(self):
       self.setupUi(self)
       self.pushButton.clicked.connect(self.button_Second)

   def button_Second(self):
       self.close()
       self.second = secondwindow()
       self.second.exec_()
       self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())