import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor, QFont, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget)
from client.nomeja_window import nomejaWindow
from client.menu_window import MenuWindow

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
        logoImg = QPixmap('client/img/Puser.png')
        logo.setPixmap(logoImg)
        logo.move(560, 45)

        # Label untuk teks di bawah logo
        logoText = QLabel(self)
        logoText.setText("Punten Meser")
        logoText.setStyleSheet('color: #68FCD6')
        logoText.move(579, 143)
        logoText.setFont(inter16)

        # Label Pertanyaan makan dimana
        ditaText = QLabel(self)
        ditaText.setText("Mau Makan di Mana?")
        ditaText.setStyleSheet('''
        color: rgba(255, 255, 255, 80%);
        background-color:  #28293D 
        ''')
        ditaText.move(512, 227)
        ditaText.setFont(inter24)

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
        self.dineinButton.setFont(inter24)
        self.dineinButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dineinButton.clicked.connect(self.on_pushdineinButton_clicked)
        self.nomejadialog = nomejaWindow()

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
        self.takeawayButton.setFont(inter24)
        self.takeawayButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeawayButton.clicked.connect(self.on_pushtakeawayButton_clicked)
        self.menuwindowdialog = MenuWindow()

    def on_pushtakeawayButton_clicked(self):
        self.menuwindowdialog.show()
        self.close()
    def on_pushdineinButton_clicked(self):
        self.nomejadialog.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ditaWindow()
    window.show()
    sys.exit(app.exec())