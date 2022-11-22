import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor, QFont, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget)

class nomejaWindow(QWidget):
    switch = pyqtSignal(str,dict)

    def __init__(self):
        super().__init__()
        self.setUpNomejaWindow()

    def nomeja(self):
        c = self.conn.cursor()

    def setUpNomejaWindow(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("Puser App - Masukkan Nomor Meja Anda")
        self.setUpWidgets()
    
    def setUpWidgets(self):
        # Set warna background
        self.setStyleSheet('background-color: #28293D') 

    # Set up font
        inter14 = QFont()
        inter14.setFamily("Inter")
        inter14.setPixelSize(14)

        inter16 = QFont()
        inter16.setFamily("Inter")
        inter16.setPixelSize(16)

        inter24 = QFont()
        inter24.setFamily("Inter")
        inter24.setPixelSize(24)

        # Label untuk logo
        logo = QLabel(self)
        logoImg = QPixmap('../img/Puser.png')
        logo.setPixmap(logoImg)
        logo.move(495, 45)

        # Label untuk teks di bawah logo
        logoText = QLabel(self)
        logoText.setText("Punten Meser")
        logoText.setStyleSheet('color: #68FCD6')
        logoText.move(579, 143)
        logoText.setFont(inter16)

        # Label Pertanyaan makan dimana
        nomejaText = QLabel(self)
        nomejaText.setText("Masukkan Nomor Meja Anda")  
        nomejaText.setStyleSheet('''
        color: rgba(255, 255, 255, 80%);
        background-color:  #28293D 
        ''')
        nomejaText.move(475, 250)
        nomejaText.setFont(inter24)

        #Input No Meja
        self.nomeja = QLineEdit(self)
        self.nomeja.setPlaceholderText("Nomor Meja")
        self.nomeja.setFixedSize(200, 150)
        self.nomeja.move(520, 350)
        self.nomeja.setStyleSheet('''
        padding: 11px 30px 11px 30px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        color: rgba(255, 255, 255, 0.8);
        background-color: #3E405B
        ''')
        self.nomeja.setFont(inter16)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = nomejaWindow()
    window.show()
    sys.exit(app.exec())