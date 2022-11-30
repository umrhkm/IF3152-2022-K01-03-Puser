import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor, QPixmap, QIntValidator
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton, QWidget)
import client.fonts
# from client.menu_window import MenuWindow

nomorMeja = 0

class nomejaWindow(QWidget):
    switch = pyqtSignal(str,dict)

    def __init__(self):
        super().__init__()
        self.setUpNomejaWindow()

    def nomeja(self):
        c = self.cursor()

    def setUpNomejaWindow(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("Puser App - Masukkan Nomor Meja Anda")
        self.setUpWidgets()
    
    def setUpWidgets(self):
        # Set warna background
        self.setStyleSheet('background-color: #28293D') 

        # Label untuk logo
        logo = QLabel(self)
        logoImg = QPixmap('client/img/Puser.png')
        logo.setPixmap(logoImg)
        logo.move(560, 45)

        # Label untuk teks di bawah logo
        logoText = QLabel(self)
        logoText.setText("Punten Meser")
        logoText.setStyleSheet('color: #68FCD6')
        logoText.move(579, 143)
        logoText.setFont(client.fonts.inter16)

        # Label Pertanyaan makan dimana
        nomejaText = QLabel(self)
        nomejaText.setText("Masukkan Nomor Meja Anda")  
        nomejaText.setStyleSheet('''
        color: rgba(255, 255, 255, 80%);
        background-color:  #28293D 
        ''')
        nomejaText.move(475, 250)
        nomejaText.setFont(client.fonts.inter24)

        #Input No Meja
        self.nomeja = QLineEdit(self)
        self.nomeja.setPlaceholderText("Nomor Meja")
        self.nomeja.setFixedSize(200, 100)
        self.nomeja.move(520, 350)
        self.nomeja.setStyleSheet('''
        padding: 11px 30px 11px 30px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        color: rgba(255, 255, 255, 0.8);
        background-color: #3E405B
        ''')
        self.nomeja.setFont(client.fonts.inter16)
        
        onlyInt = QIntValidator()
        onlyInt.setRange(0, 10)
        
        self.nomeja.setValidator(onlyInt)

        # button selanjutnya 
        self.selanjutnyaButton = QPushButton(self)
        self.selanjutnyaButton.setText("Selanjutnya")
        self.selanjutnyaButton.setFixedSize(150, 75)
        self.selanjutnyaButton.move(650, 500)
        self.selanjutnyaButton.setStyleSheet('''
        QPushButton {
            color: #ffffff;
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #5561ff, stop:1 #3643fc);
            border: none;
            border-radius: 12px;
        }
        QPushButton:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #6b75ff, stop:1 #535fff);
        }
        ''')
        self.selanjutnyaButton.setFont(client.fonts.inter24)
        self.selanjutnyaButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.selanjutnyaButton.clicked.connect(self.menu)
        # self.menuwindowdialog = MenuWindow()

        # button kembali
        self.kembaliButton = QPushButton(self)
        self.kembaliButton.setText("Kembali")
        self.kembaliButton.setFixedSize(150, 75)
        self.kembaliButton.move(450, 500)
        self.kembaliButton.setStyleSheet('''
        QPushButton {
            color: #ffffff;
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #f55951, stop:1 #f55951);
            border: none;
            border-radius: 12px;
        }
        QPushButton:hover {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #ff0c00, stop:1 #ff0c00);
        }
        ''')
        self.kembaliButton.setFont(client.fonts.inter24)
        self.kembaliButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kembaliButton.clicked.connect(self.dita)

    def menu(self):
        global nomorMeja
        # nomorMeja = int(self.nomeja.text())
        # self.switch.emit("menu",{})
        if (self.nomeja.text() == ''):
            self.switch.emit("nomeja",{})
        else:
            nomorMeja = (self.nomeja.text())
            nomorMeja = int(nomorMeja)
            self.switch.emit("menu",{})
        
    def dita(self):
        self.switch.emit("dita",{})
        
    def resetnomeja(self):
        self.nomeja.clear()

    # def on_pushkembaliButton_clicked(self):
    #     self.ditawindowdialog.show()
    #     self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = nomejaWindow()
    window.show()
    sys.exit(app.exec())