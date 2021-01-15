import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import numpy as np


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()        

    def initUI(self):
        
        self.setWindowTitle("ANASAYFA")
          
        self.giris_yazisi=QtWidgets.QLabel("Yapmak istediğiniz eylemi seçiniz")
        self.giris_yazisi.move(50,100)
        
        self.arama=QtWidgets.QPushButton("Arama Algoritmaları")
        self.siralama=QtWidgets.QPushButton("Sıralama Algoritmaları")
        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.arama)
        self.h_box.addWidget(self.siralama)
          
             
            
        self.isim = QtWidgets.QLabel("Nil DUMAN")
        self.okul_no = QtWidgets.QLabel("18360859026")
            
        self.h_box = QtWidgets.QHBoxLayout() #vertical için h yazan yerlere v geliyor
            
        self.h_box.addStretch() #yaslamak için bir alta da gidebilir iki alta da
        self.h_box.addWidget(self.isim)
        self.h_box.addWidget(self.okul_no)
            
        self.v_box = QtWidgets.QVBoxLayout()
            
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box)
          
        
          
        self.ders_adi = QtWidgets.QLabel("Algoritma Analizi ve Tasarimi Ders Projesi ")
        
            
        self.h_box = QtWidgets.QHBoxLayout() #vertical için h yazan yerlere v geliyor
            
        
        self.h_box.addWidget(self.ders_adi)
        self.h_box.addStretch() #yaslamak için bir alta da gidebilir iki alta da
            
        self.v_box = QtWidgets.QVBoxLayout()
            
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box)
        self.setGeometry(100,100,1000,700)
        self.show()
          
          
          
          
            
         
 
        
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())