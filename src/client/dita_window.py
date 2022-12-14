import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QWidget)
import client.fonts

class ditaWindow(QWidget):
    switch = pyqtSignal(str, dict)

    def __init__(self):
        super().__init__()
        self.setUpDitaWindow()

    def dita(self):
        c = self.cursor()

    def setUpDitaWindow(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("Puser App - Order Here")
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
        ditaText = QLabel(self)
        ditaText.setText("Mau Makan di Mana?")
        ditaText.setStyleSheet('''
        color: rgba(255, 255, 255, 80%);
        background-color:  #28293D 
        ''')
        ditaText.move(512, 227)
        ditaText.setFont(client.fonts.inter24)

        # Dine In Button
        self.dineinButton = QPushButton(self)
        self.dineinButton.setText("Dine in")
        self.dineinButton.setFixedSize(200, 200)
        self.dineinButton.move(400, 275)
        self.dineinButton.setStyleSheet('''
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
        self.dineinButton.setFont(client.fonts.inter24)
        self.dineinButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dineinButton.clicked.connect(self.dineIn)
        # self.nomejadialog = nomejaWindow()

        # Take Away Button
        self.takeawayButton = QPushButton(self)
        self.takeawayButton.setText("Take Away")
        self.takeawayButton.setFixedSize(200, 200)
        self.takeawayButton.move(650, 275)
        self.takeawayButton.setStyleSheet('''
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
        self.takeawayButton.setFont(client.fonts.inter24)
        self.takeawayButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeawayButton.clicked.connect(self.takeAway)
        # self.menuwindowdialog = MenuWindow()

    def takeAway(self):
        self.switch.emit("menu",{})
        # self.close()

    def dineIn(self):
        global status
        status = True
        self.switch.emit("nomeja",{})

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ditaWindow()
    window.show()
    sys.exit(app.exec())