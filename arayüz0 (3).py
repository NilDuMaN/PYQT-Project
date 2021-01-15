
import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
# from girdi import Girdi
import numpy as np
from PyQt5.uic import loadUi
#from PyQt5 import QHBoxLayout


def Pencere(): #iskelet
    

        
    app = QtWidgets.QApplication(sys.argv) #uygulama objesi
  
    
   

    
    #uygulama sürekli çalışsın diye döngüye sokmalıyız
    sys.exit(app.exec_())

class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("main_page.ui", self)
        # self.initUI()        

    # def initUI(self):

    #     self.okay = QtWidgets.QLabel("TAMAM")
    #     self.cancel = QtWidgets.QLabel("İPTAL")
        
    #     self.h_box = QtWidgets.QHBoxLayout() #vertical için h yazan yerlere v geliyor
        
    #     self.h_box.addStretch() #yaslamak için bir alta da gidebilir iki alta da
    #     self.h_box.addWidget(self.okay)
    #     self.h_box.addWidget(self.cancel)
        
    #     self.v_box = QtWidgets.QVBoxLayout()
        
    #     self.v_box.addStretch()
    #     self.v_box.addLayout(self.h_box)
        
    #     self.pencere = QtWidgets.QWidget() #pencere objesi
    #     self.pencere.setWindowTitle("Algoritma Analizi ve Tasarımı Ders Projesi /n") #pencereyi adlandırma
        
    #     self.etiket = QtWidgets.QLabel(self.pencere)
    #     self.etiket.setText("18360859026")
    
        
    #     self.buton = QtWidgets.QPushButton(self.pencere)
    #     self.buton.setText("Burası bir butondur")

        
    #     self.buton.clicked.connect(self.girdi_click)

    
    #     self.etiket.move(195,70)
    #     self.buton.move(180,100)
        
    #     self.etiket1 = QtWidgets.QLabel(self.pencere)
    # # etiket2 = QtWidgets.QLabel(pencere)
    # # etiket2.setPixmap(QtGui.QPixmap("logo.jpg"))
    
    #     self.etiket1.setText("Nil DUMAN")
    #     self.etiket1.move(205,50) #yerini ayarladık
    # # etiket2.move(10,50) 
    
    #     self.pencere.setLayout(self.v_box) #gösterelim
    #     self.pencere.setGeometry(100,100,500,500) #pencerenin yeri ve büyüklüğünü ayarladık
    
        
    #     self.pencere.show() #pencereyi gösterelim

    # def girdi_click(self):
    #     self.girdi = Girdi()
    

app = QApplication([])
window = MainPage()
window.show()
sys.exit(app.exec_())


