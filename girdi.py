import sys
from PyQt5 import  QtWidgets
import numpy as np

class Girdi(QtWidgets.QWidget): #miras alıyoruz
    def __init__(self): #class başında ilk çalıştırılan fonksiyon

        super().__init__()

        self.init_ui()

    def init_ui(self):
        
        self.baslangic_yazisi.setText("Başlangıç Değerini giriniz")
        self.baslangic_yazisi.move(205,50)
        self.baslangic = QtWidgets.QLineEdit()
        

        self.bitis_yazisi.setText("Bitiş Değerini giriniz")
        self.bitis_yazisi.move(205,75)
        self.bitis = QtWidgets.QLineEdit()
        
        

        self.uretilensayi_yazisi.setText("Bitiş Değerini giriniz")
        self.uretilensayi_yazisi.move(205,100)
        self.uretilensayi = QtWidgets.QLineEdit()
        
        
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Yazdır")
        
        self.yazi1 = QtWidgets.QLabel()
        self.yazi1.setText("18360859026")
       
        v_box = QtWidgets.QVBoxLayout()
        baslangic=self.baslangic
        baslangic=(int(input("Başlangıç Değerini Giriniz")))
        bitis=self.bitis
        bitis=(int(input("Bitiş Değerini Giriniz")))
        uretilensayi=self.uretilensayi
        uretilensayi=int(input("Üretilmesini İstediğiniz Sayı Miktarını Giriniz"))
        sayilar=np.random.randint(baslangic,bitis,uretilensayi)
        print(type(sayilar))
        print(min(sayilar))
        print(max(sayilar))
        print("üretilen sayılar:",sayilar)
        # self.tum_sayilar=QtWidgets.QLineEdit()
        # self.tum_sayilar.setText(sayilar)
        
        
        #baslangic = self.baslangic
        
       
        v_box.addWidget(self.baslangic)
        v_box.addWidget(self.bitis)
        v_box.addWidget(self.uretilensayi)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)
        v_box.addStretch()

        self.setLayout(v_box)


        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)



        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Temizle":
            self.yazi_alani.clear()

        else:
            print(self.yazi_alani.text())