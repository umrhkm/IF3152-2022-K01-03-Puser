import fonts
import sys

import bcrypt
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor, QFont, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget)

from custom_widgets import ClickableLabel


class LoginWindow(QWidget):
    switch = pyqtSignal(str, dict)

    def __init__(self):
        super().__init__()
        self.setUpLoginWindow()
        # self.conn = sqlite3.connect("fitpal.db")

    def setUpLoginWindow(self):
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
        logoImg = QPixmap('../img/Puser.png')
        logo.setPixmap(logoImg)
        logo.move(495, 45)

        # Label untuk teks di bawah logo
        logoText = QLabel(self)
        logoText.setText("Punten Meser")
        logoText.setStyleSheet('color: #68FCD6')
        logoText.move(579, 143)
        logoText.setFont(inter16)

        # Label untuk card
        card = QLabel(self)
        cardImg = QPixmap("img/login-card.png")
        card.setPixmap(cardImg)
        card.move(309, 197)

        # Label Pertanyaan makan dimana
        loginText = QLabel(self)
        loginText.setText("Mau Makan di Mana?")  #3E405B
        loginText.setStyleSheet('''
        color: rgba(255, 255, 255, 80%);
        background-color:  #28293D 
        ''')
        loginText.move(512, 227)
        loginText.setFont(inter24)

        # Input username/email
        # self.usernameEdit = QLineEdit(self)
        # self.usernameEdit.setPlaceholderText("Username or Email")
        # self.usernameEdit.setFixedSize(446, 46)
        # self.usernameEdit.move(407, 293)
        # self.usernameEdit.setStyleSheet('''
        # padding: 11px 30px 11px 30px;
        # border: 1px solid rgba(255, 255, 255, 0.8);
        # border-radius: 20px;
        # color: rgba(255, 255, 255, 0.8);
        # background-color: #3E405B
        # ''')
        # self.usernameEdit.setFont(inter16)

        # button Kembali
        self.kembaliText = QPushButton(self)
        self.kembaliText.setText("Kembali")
        self.kembaliText.move(30, 20)
        self.kembaliText.setStyleSheet(f"color: #000000; background-color: #DA6676")
        self.kembaliText.setFont(fonts.inter18bold)

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
        self.dineinButton.clicked.connect(self.login)

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
        self.takeawayButton.clicked.connect(self.login)

        # Input No Meja
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setPlaceholderText("Nomor Meja")
        self.passwordEdit.setFixedSize(155, 46)
        self.passwordEdit.move(550, 500)
        self.passwordEdit.setStyleSheet('''
        padding: 11px 30px 11px 30px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        color: rgba(255, 255, 255, 0.8);
        background-color: #3E405B
        ''')
        self.passwordEdit.setFont(inter16)
        # self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        # Menu push button
        # self.menuButton = QPushButton(self)
        # self.menuButton.setText("Continue to Menu")
        # self.menuButton.setFixedSize(183, 48)
        # self.menuButton.move(535, 550)
        # self.menuButton.setStyleSheet('''
        # QPushButton {
        #     color: #ffffff;
        #     background-color: qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #5561ff, stop:1 #3643fc);
        #     border: none;
        #     border-radius: 12px;
        # }
        # QPushButton:hover {
        #     background-color: qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #6b75ff, stop:1 #535fff);
        # }
        # ''')
        # self.menuButton.setFont(inter16)
        # self.menuButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.menuButton.clicked.connect(self.login)

        # # Don't have an account? label
        # label = QLabel(self)
        # label.setText("Don't have an account?")
        # label.setFont(inter14)
        # label.setStyleSheet(
        #     'color: rgba(255, 255, 255, 0.8); background-color: #3E405B')
        # label.move(561, 508)

        # Register here label
        # registerHere = ClickableLabel(self)
        # registerHere.setText("Register here")
        # registerHere.setFont(inter16)
        # registerHere.setStyleSheet('''
        # QLabel {
        #     color: #3EEBBE; 
        #     text-decoration: underline; 
        #     background-color: #3E405B
        # }
        # QLabel:hover {
        #     color: #68FCD6;
        # }
        # ''')
        # registerHere.move(587, 529)
        # registerHere.clicked.connect(self.showRegisterWindow)
        # registerHere.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # # Eye icon
        # eyeIcon = ClickableLabel(self)
        # eyeIconImg = QPixmap("../img/eye-icon.png")
        # eyeIcon.setPixmap(eyeIconImg)
        # eyeIcon.move(800, 365)
        # eyeIcon.setStyleSheet("background-color: #3E405B")
        # eyeIcon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # # Eye icon click handling
        # self.showPassword = False
        # eyeIcon.clicked.connect(self.toggleShowPassword)

    # def showRegisterWindow(self):
    #     self.switch.emit("register", {})

    # def toggleShowPassword(self):
    #     self.showPassword = not (self.showPassword)
    #     if (self.showPassword):
    #         self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
    #     else:
    #         self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

    # def comparePass(self, password, hashPassword):
    #     return bcrypt.checkpw(password.encode(), hashPassword.encode())

    def login(self):
        c = self.conn.cursor()
        # c.execute(
        #     f"SELECT * FROM user WHERE (username = '{self.usernameEdit.text()}' OR email = '{self.usernameEdit.text()}')")
        # res = c.fetchone()
        # if res != None and not self.comparePass(self.passwordEdit.text(), res[4]):
        #     res = None
        # if res == None:
        #     msgBox = QMessageBox()
        #     msgBox.setText(
        #         "<p>Username/email and password combination not found!</p>")
        #     msgBox.setWindowTitle("Login Failed")
        #     msgBox.setIcon(QMessageBox.Icon.Warning)
        #     msgBox.setStyleSheet("background-color: white")
        #     msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        #     msgBox.exec()
        # else:
        #     msgBox = QMessageBox()
        #     msgBox.setText(f"<p>Hello, {res[1]}!</p>")
        #     msgBox.setWindowTitle("Login Successful")
        #     msgBox.setIcon(QMessageBox.Icon.Information)
        #     msgBox.setStyleSheet("background-color: white")
        #     msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        #     msgBox.exec()
        #     user = {
        #         "id": res[0],
        #         "fullname": res[1],
        #         "username": res[2],
        #         "email": res[3],
        #         "password": res[4],
        #         "type": res[5]
        #     }
        #     if (res[5] == "user"):
        #         self.switch.emit("user_dashboard", user)
        #     else:
        #         self.switch.emit("trainer_dashboard", user)

    def clearForm(self):
        self.passwordEdit.clear()
        self.usernameEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())