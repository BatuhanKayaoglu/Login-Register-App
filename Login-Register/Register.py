import  sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti_olustur()
        
        
        
    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database2.db")

        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")
        
        adi = self.kullaniciOlustur.text()
        par = self.parolaOlustur.text()
        
        if len(adi)==0:
            self.yazi_alani.setText("")
            
        elif len(par)>=10:
            self.yazi_alani.setText("10 karakterden fazla kullanmayınınız..!")
        
        else:
            self.cursor.execute("INSERT INTO üyeler VALUES(?,?)",(adi,par))
            baglanti.commit()
        
            self.yazi_alani.setText("Kayıt Başarıyla tamamlandı.")
        
        
        
    
    def init_ui(self):
        
        self.kullaniciOlustur=QtWidgets.QLineEdit()
        self.parolaOlustur=QtWidgets.QLineEdit()
        self.parolaOlustur.setEchoMode(QtWidgets.QLineEdit.Password)
        self.yazi_alani = QtWidgets.QLabel("")
        self.kayitOl = QtWidgets.QPushButton("KAYIT OL")
        
        
        
        
        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullaniciOlustur)
        v_box.addWidget(self.parolaOlustur)
        v_box.addWidget(self.kayitOl)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        


        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)



        self.setWindowTitle("Kayıt Olma")
        
        
        self.kayitOl.clicked.connect(self.baglanti_olustur)
        
        self.show()
        

             
        
        
        

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
