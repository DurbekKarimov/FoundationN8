import sys
from PyQt5.QtGui import *
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os
os.system("cls")
class menyu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Menyu yozuvi uchun 
        self.resize(1000,1000)
        self.main=QVBoxLayout()
        self.lbl=QLabel("Bizning Restoranimizga Xush kelibsiz!",self)
        self.lbl2=QLabel("Restorandagi menyu!",self)
        # 1- taomlar uchun
        self.lbl3=QLabel("1-taomlar!",self)
        self.lbl3.setGeometry(20,20,200,20)
        self.rdb1=QCheckBox(self)
        self.rdb1.setText("Manti-15000")
        self.rdb2=QCheckBox(self)
        self.rdb2.setText("Osh-30000")
        self.rdb3=QCheckBox(self)
        self.rdb3.setText("Shorva-30000")
        self.setFont(QFont("Calibri",22))
        self.lbl.setGeometry(250,3,600,50)
        self.lbl2.setGeometry(300,50,600,50)
        self.lbl3.setGeometry(10,90,600,50)
        self.rdb1.setGeometry(10,140,500,50)
        self.rdb2.setGeometry(10,180,500,50)
        self.rdb3.setGeometry(10,220,500,50)
        # 2-ichimliklar uchun
        self.lbl_2=QLabel("2-ichimliklar",self)
        self.lbl_2.setGeometry(20,280,200,50)
        self.rdb_1=QCheckBox(self)
        self.rdb_1.setText("cola-12000")
        self.rdb_2=QCheckBox(self)
        self.rdb_2.setText("pepsi-15000")
        self.rdb_3=QCheckBox(self)
        self.rdb_3.setText("fanta-12000")
        self.setFont(QFont("Calibri",22))
        self.rdb_1.setGeometry(10,320,500,50)
        self.rdb_2.setGeometry(10,360,500,50)
        self.rdb_3.setGeometry(10,400,500,50)
        #3-shirinliklar
        self.lbl_2=QLabel("3-shirinliklar",self)
        self.lbl_2.setGeometry(20,440,200,50)
        self.rdb_1=QCheckBox(self)
        self.rdb_1.setText("Napalyon-30000")
        self.rdb_2=QCheckBox(self)
        self.rdb_2.setText("shokalad-12000")
        self.rdb_3=QCheckBox(self)
        self.rdb_3.setText("qaymoqli perok-30000")
        self.setFont(QFont("Calibri",22))
        self.rdb_1.setGeometry(10,480,500,50)
        self.rdb_2.setGeometry(10,520,500,50)
        self.rdb_3.setGeometry(10,560,500,50)
        #4-non
        self.lbl_2=QLabel("4-non",self)
        self.lbl_2.setGeometry(20,600,200,50)
        self.rdb_1=QCheckBox(self)
        self.rdb_1.setText("kulcha-5000")
        self.rdb_2=QCheckBox(self)
        self.rdb_2.setText("buxanka-2800")
        self.rdb_3=QCheckBox(self)
        self.rdb_3.setText("tandir non-10000")
        self.setFont(QFont("Calibri",22))
        self.rdb_1.setGeometry(10,640,500,50)
        self.rdb_2.setGeometry(10,680,500,50)
        self.rdb_3.setGeometry(10,720,500,50)


        # va siz buttomlarni bosganizda
        
        self.rdb1.clicked.connect(self.tekshir)
        self.rdb2.clicked.connect(self.tekshir)
        self.rdb_1.clicked.connect(self.tekshir)
        self.rdb_2.clicked.connect(self.tekshir)
        self.rdb_3.clicked.connect(self.tekshir)

    def tekshir(self):
        # print("Sizning  buyurtmangiz!")
        if self.rdb1.isChecked():
            print(f"Manti-15000")
        elif self.rdb2.isChecked():
            print(f"Osh-30000")
        elif self.rdb3.isChecked():
            print(f"Shorva-30000")
        # Va qolganlari shunday davom etadi !
        pass


if __name__=="__main__":
    app=QApplication(sys.argv)
    print("Sizning buyurtmangiz!")
    dastur=menyu()
    dastur.show()
    sys.exit(app.exec_())
