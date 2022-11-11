import sys
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

   def Home(self):
    self.close()