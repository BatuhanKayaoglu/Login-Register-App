import sys
from PyQt5 import QtWidgets
import sqlite3


class Pencere(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.baglantiOlustur()
        
        self.init_ui()
        
        
        
    
    def baglantiOlustur(self):
        baglanti=sqlite3.connect("database1.db")
        self.cursor=baglanti.cursor()
        
        self.cursor.execute("Create Table If not exists uyeler(kullaniciAdi TEXT,parola TEXT) ")
        
        baglanti.commit()
        
    
    
    def init_ui(self):
        
        self.setWindowTitle("Kullanıcı Girişi")
        
        
        self.kullaniciAdi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password) ##Normal parola gibi yıldızlıyor..!!!!!
        self.giris=QtWidgets.QPushButton("Giriş Yap")
        self.yaziAlani=QtWidgets.QLabel("")
        
        
        
        vBox=QtWidgets.QVBoxLayout()
        vBox.addWidget(self.kullaniciAdi)
        vBox.addWidget(self.parola)
        vBox.addWidget(self.yaziAlani)
        vBox.addStretch()
        vBox.addWidget(self.giris)
        
        
        
        hBox=QtWidgets.QHBoxLayout()
        hBox.addStretch()
        hBox.addLayout(vBox)
        hBox.addStretch()  
        self.setLayout(hBox)
        
        
        self.giris.clicked.connect(self.login)
         
        self.show()
        
        
    def login(self):
        adi=self.kullaniciAdi.text()
        par=self.parola.text()
        
        self.cursor.execute("Select * from uyeler where kullaniciAdi=? and parola=?",(adi,par))
        
        data=self.cursor.fetchAll()
        
        if len(data)==0: ##Girdiğim değere göre bir data yoksa
            self.yaziAlani.setText("Böyle bir kullanıcı bulunamadı \nLütfen tekrar deneyiniz...")
            
        else:
            self.yaziAlani.setText(f"Hoşgeldiniz {self.kullaniciAdi}")
        
        
        
        
        
        
        
        
        
    


app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())