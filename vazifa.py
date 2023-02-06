import sys
from PyQt5.QtGui import *
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os
os.system("cls")

class ilova(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        # asosiy oyna uchun
                 
        self.setMaximumSize(1570,850)
        self.setMinimumSize(1570,850)
        self.setFont(QFont("Calibri",20))

        # Tanlash uchun
        self.radio_btn = QRadioButton(self)
        self.radio_btn.setFont(QFont("Calibri",16))
        self.radio_btn.setText("Omad (30/5)")
        self.radio_btn.setGeometry(20,50,195,50)

        self.sharq_btn = QRadioButton(self)
        self.sharq_btn.setFont(QFont("Calibri",16))
        self.sharq_btn.setText("Sharqona(30/6)")
        self.sharq_btn.setGeometry(230,50,235,50)

        self.super_btn = QRadioButton(self)
        self.super_btn.setFont(QFont("Calibri",16))
        self.super_btn.setText("Super(30/7)")
        self.super_btn.setGeometry(500,50,235,50)

        #input uchun
        self.input = QLineEdit(self)
        self.input.setGeometry(20, 120, 540, 75)
        self.input.setStyleSheet("""
            background-color: white;
            border-radius: 20px;
            border-width: 5px;
            border-color:blue;
            border-style:solid;
        """)
        # border uchun
        self.input_btn=QPushButton("+",self)
        self.input_btn.setGeometry(590,120,100,75)
        self.input_btn.setStyleSheet("""
        background-color: gray;
        border-radius: 20px;
        border-width: 5px;
        border-style:solid;
        border-color:red;
        """)

        # Dumaloq buttonlar uchun
        self.start_btn=QPushButton("Start",self)
        self.start_btn.setGeometry(750,50,100,60)
        self.start_btn.setStyleSheet("""
        background-color: lightgray;
        border-radius: 20px;
        border-width: 5px;
        border-style:solid;
        border-color:green;
        """)

        self.btn1=QPushButton(self)
        self.btn1.setGeometry(880,50,60,60)
        self.btn_for(self.btn1)

        self.btn1=QPushButton(self)
        self.btn1.setGeometry(980,50,60,60)
        self.btn_for(self.btn1)

        self.btn1=QPushButton(self)
        self.btn1.setGeometry(1080,50,60,60)
        self.btn_for(self.btn1)

        self.btn1=QPushButton(self)
        self.btn1.setGeometry(1180,50,60,60)
        self.btn_for(self.btn1)

        self.btn1=QPushButton(self)
        self.btn1.setGeometry(1280,50,60,60)
        self.btn_for(self.btn1)

        self.btn1=QPushButton(self)
        self.btn1.setGeometry(1380,50,60,60)
        self.btn_for(self.btn1)

        self.btn1=QPushButton(self)
        self.btn1.setGeometry(1480,50,60,60)
        self.btn_for(self.btn1)
        #input uchun katta ekran uchun
        self.input = QLineEdit(self)
        self.input.setGeometry(750, 120, 800, 570)
        self.input.setStyleSheet("""
            background-color: lightblue;
            border-radius: 20px;
            border-width: 5px;
            border-color:black;
            border-style:solid;
        """)
        # Raqamlar uchun
        self.one = QPushButton("1", self)
        self.one.setGeometry(20, 220, 75,75)
        self.numbers(self.one)

        self.two = QPushButton("2",self)
        self.two.setGeometry(140,220,75,75)
        self.numbers(self.two)
        
        self.three = QPushButton("3", self)
        self.three.setGeometry(260, 220,75, 75)
        self.numbers(self.three)

        self.four = QPushButton("4", self)
        self.four.setGeometry(380,220,75, 75)
        self.numbers(self.four)

        self.five = QPushButton("5", self)
        self.five.setGeometry(500,220,75,75)
        self.numbers(self.five)

        self.six = QPushButton("6", self)
        self.six.setGeometry(620,220,75,75)
        self.numbers(self.six)

        self.seven = QPushButton("7", self)
        self.seven.setGeometry(20, 320, 75,75)
        self.numbers(self.seven)

        self.eight = QPushButton("8", self)
        self.eight.setGeometry(140, 320, 75,75)
        self.numbers(self.eight)

        self.nine = QPushButton("9", self)
        self.nine.setGeometry(260, 320, 75,75)
        self.numbers(self.nine)

        self.ten = QPushButton("10", self)
        self.ten.setGeometry(380, 320, 75,75)
        self.numbers(self.ten)

        self.eleven = QPushButton("11", self)
        self.eleven.setGeometry(500, 320, 75,75)
        self.numbers(self.eleven)

        self.twelve = QPushButton("12", self)
        self.twelve.setGeometry(620, 320, 75,75)
        self.numbers(self.twelve)

        self.onuch = QPushButton("13", self)
        self.onuch.setGeometry(20, 420, 75,75)
        self.numbers(self.onuch)

        self.ontort = QPushButton("14", self)
        self.ontort.setGeometry(140, 420, 75,75)
        self.numbers(self.ontort)

        self.onbesh = QPushButton("15", self)
        self.onbesh.setGeometry(260, 420, 75,75)
        self.numbers(self.onbesh)

        self.onolti = QPushButton("16", self)
        self.onolti.setGeometry(380, 420, 75,75)
        self.numbers(self.onolti)

        self.onyetti = QPushButton("17", self)
        self.onyetti.setGeometry(500, 420, 75,75)
        self.numbers(self.onyetti)

        self.onsakkiz = QPushButton("18", self)
        self.onsakkiz.setGeometry(620, 420, 75,75)
        self.numbers(self.onsakkiz)

        self.onuch = QPushButton("19", self)
        self.onuch.setGeometry(20, 520, 75,75)
        self.numbers(self.onuch)

        self.yigirma = QPushButton("20", self)
        self.yigirma.setGeometry(140, 520, 75,75)
        self.numbers(self.yigirma)

        self.yigirmabir = QPushButton("21", self)
        self.yigirmabir.setGeometry(260, 520, 75,75)
        self.numbers(self.yigirmabir)

        self.yigirmaikki = QPushButton("22", self)
        self.yigirmaikki.setGeometry(380, 520, 75,75)
        self.numbers(self.yigirmaikki)

        self.yigirmauch = QPushButton("23", self)
        self.yigirmauch.setGeometry(500, 520, 75,75)
        self.numbers(self.yigirmauch)

        self.yigirmatort = QPushButton("24", self)
        self.yigirmatort.setGeometry(620, 520, 75,75)
        self.numbers(self.yigirmatort)
        #djdflbndfslibndflbjna;jnb;sdbjndfs;bjndf;
        self.yigirmabesh = QPushButton("25", self)
        self.yigirmabesh.setGeometry(20, 620, 75,75)
        self.numbers(self.yigirmabesh)

        self.yigirmaolti = QPushButton("26", self)
        self.yigirmaolti.setGeometry(140, 620, 75,75)
        self.numbers(self.yigirmaolti)

        self.yigirmayetti = QPushButton("27", self)
        self.yigirmayetti.setGeometry(260, 620, 75,75)
        self.numbers(self.yigirmayetti)

        self.yigirmasakkiz = QPushButton("28", self)
        self.yigirmasakkiz.setGeometry(380, 620, 75,75)
        self.numbers(self.yigirmasakkiz)

        self.yigirmatoqqiz = QPushButton("29", self)
        self.yigirmatoqqiz.setGeometry(500, 620, 75,75)
        self.numbers(self.yigirmatoqqiz)

        self.uttiz = QPushButton("30", self)
        self.uttiz.setGeometry(620, 620, 75,75)
        self.numbers(self.uttiz)

        # telegram uchun button
        self.tg_btn=QPushButton("Telegram",self)
        self.tg_btn.setFont(QFont("Calibri",10))
        self.tg_btn.setGeometry(20,760,300,40)
        self.tg_btn.setStyleSheet("""
            background-color: lightblue;
            border-radius: 20px;
            border-width: 3px;
            border-style:solid;
            border-color:blue;
        """)
        # yutube uchun button
        self.yt_btn=QPushButton("YOU TUBE",self)
        self.yt_btn.setFont(QFont("Calibri",10))
        self.yt_btn.setGeometry(380,760,300,40)
        self.yt_btn.setStyleSheet("""
            background-color: lightblue;
            border-radius: 20px;
            border-width: 3px;
            border-style:solid;
            border-color:blue;
        """)
        

    @staticmethod
    def numbers(number):
        number.setStyleSheet("""
            background-color: lightpink;
            border-radius: 37px;
            border-width: 5px;
            border-style:solid;
            border-color:red;
        """)
    
    @staticmethod
    def btn_for(btn):
        btn.setStyleSheet("""
        background-color: orange;
        border-radius: 29px;
        border-width: 5px;
        border-style:solid;
        border-color:black;
        """)



app = QApplication(sys.argv)
application = ilova()
application.show()
sys.exit(app.exec_())
