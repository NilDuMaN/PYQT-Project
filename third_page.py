import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
# from girdi import Girdi
import numpy as np
from PyQt5.uic import loadUi
#from PyQt5 import QHBoxLayout


class ThirdPage(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("arama_window.ui", self)
        # self.initUI()    
        
app = QApplication([])
window = ThirdPage()
window.show()
sys.exit(app.exec_())
