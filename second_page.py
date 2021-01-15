import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
# from girdi import Girdi
import numpy as np
from PyQt5.uic import loadUi
#from PyQt5 import QHBoxLayout


class SecondPage(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("siralama_window.ui", self)
        # self.initUI()    
        
app = QApplication([])
window = SecondPage()
window.show()
sys.exit(app.exec_())
