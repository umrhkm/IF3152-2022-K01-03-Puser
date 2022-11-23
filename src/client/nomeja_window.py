import sys
import fonts
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor, QFont, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget)
from menu_window import MenuWindow

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

        # Label No Meja Anda
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
        self.nomeja.setFixedSize(200, 100)
        self.nomeja.move(520, 350)
        self.nomeja.setStyleSheet('''
        padding: 11px 30px 11px 30px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        color: rgba(255, 255, 255, 0.8);
        background-color: #3E405B
        ''')
        self.nomeja.setFont(inter16)
        self.nomeja.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        # button Selanjutnya
        self.nextButton = QPushButton(self)
        self.nextButton.setText("Selanjutnya")
        self.nextButton.setFixedSize(150,75)
        self.nextButton.move(540, 500)
        self.nextButton.setStyleSheet('''
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
        self.nextButton.setFont(fonts.inter18bold)
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.clicked.connect(self.on_pushednextButton_clicked)
        self.menuwindowdialog = MenuWindow()

        # button Kembali
        kembaliText = QPushButton(self)
        kembaliText.setText("Kembali")
        kembaliText.move(30, 20)
        kembaliText.setStyleSheet(f"color: #000000; background-color: #DA6676")
        kembaliText.setFont(fonts.inter18bold)

    def on_pushednextButton_clicked(self):
        self.menuwindowdialog.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = nomejaWindow()
    window.show()
    sys.exit(app.exec())