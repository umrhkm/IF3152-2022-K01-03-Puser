# Form implementation generated from reading ui file 'aneh.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

BG_COLOR = '#FFFFFF'
DARK_MODE_BG = '#383a59'
PRIMARY_BLACK = '#000000'
PRIMARY_WHITE = '#FFFFFF'
PRIMARY_BUTTON = '#5561FF'
PRIMARY_GREEN = '#04FFA5'
SECONDARY_GREEN = '#70FFCC'
PURPLE = '#28293D'
BTN_COLOR = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #5561ff, stop:1 #3643fc);'
BTN_COLOR_HOVER = 'qlineargradient(x1:0, y1:0, x2:1, y2: 1, stop:0 #6b75ff, stop:1 #535fff)'

import requests
import json
import sys
import fonts
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal, QRect
from PyQt6.QtGui import QCursor, QFont, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget)
from custom_widgets import ClickableLabel

# # Kalo program udah jadi, buka aja comment ini
response = requests.get("http://localhost:5000/api/menus/")
jsonresponse = response.json()
makanan = [x for x in jsonresponse if x['kategori'] == 'makanan']
minuman = [x for x in jsonresponse if x['kategori'] == 'minuman']

# Buat ngetes, biar ga request-request dulu
# makanan = [{'fotoUrl': 'https://w7.pngwing.com/pngs/201/77/png-transparent-hamburger-veggie-burger-take-out-fast-food-kebab-delicious-beef-burger-burger-with-lettuce-tomato-and-cheese-food-beef-recipe.png', 'harga': 25000, 'id': 1, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Original Burger'}, {'fotoUrl': None, 'harga': 22000, 'id': 2, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Chicken Burger'}, {'fotoUrl': None, 'harga': 40000, 'id': 3, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Beef Burger'}, {'fotoUrl': None, 'harga': 20000, 'id': 4, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Cheese Burger'}]

# minuman = [{'fotoUrl': None, 'harga': 8000, 'id': 8, 'jumlahStok': 2, 'kategori': 'minuman', 'nama': 'Coca Cola'}, {'fotoUrl': None, 'harga': 8000, 'id': 7, 'jumlahStok': 2, 'kategori': 'minuman', 'nama': 'Fanta'}, {'fotoUrl': None, 'harga': 8000, 'id': 6, 'jumlahStok': 0, 'kategori': 'minuman', 'nama': 'Sprite'}, {'fotoUrl': None, 'harga': 5000, 'id': 5, 'jumlahStok': 0, 'kategori': 'minuman', 'nama': 'Air Mineral'}]

class MenuWindow(QWidget):
    switch = pyqtSignal(str, dict)

    def __init__(self):
        super().__init__()

        self.pageMakanan = 0
        self.pageMinuman = 0
        
        self.fetchMakanan()
        self.fetchMinuman()
        self.setUpMenuWindow()
        
    def setUpMenuWindow(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("Puser - Pilih Menu")
        self.setUpWidgets()
      
    def updateDisplayMakanan(self):
        self.fetchMakanan()
        self.setUpDisplayMakanan()
        
    def updateDisplayMinuman(self):
        self.fetchMinuman()
        self.setUpDisplayMinuman()
        
    def setUpWidgets(self):
        # Set warna background
        self.setStyleSheet(f'background-color: {DARK_MODE_BG}')

        # Label untuk logo
        logo = QLabel(self)
        logoImg = QPixmap("img/Puser.png")
        logo.setPixmap(logoImg)
        logo.move(572, 20)

        # Label untuk teks di bawah logo
        silakanText = QLabel(self)
        silakanText.setText("Silakan Pilih Menu Makanan / Minuman Anda")
        silakanText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        silakanText.move(400, 60)
        silakanText.setFont(fonts.inter24)
        
        makananText = QLabel(self)
        makananText.setText("Makanan")
        makananText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        makananText.move(50, 100)
        makananText.setFont(fonts.inter18bold)
        
        minumanText = QLabel(self)
        minumanText.setText("Minuman")
        minumanText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        minumanText.move(50, 365)
        minumanText.setFont(fonts.inter18bold)
        
        # Set up previous / next button
        self.rightMakananButton = QPushButton(self)
        self.rightMakananButton.setGeometry(QRect(1215, 207, 48, 48))
        self.rightMakananButton.setStyleSheet("background-image: url(img/right-btn.png);")
        self.rightMakananButton.clicked.connect(self.rightMakananButtonClicked)
        self.rightMakananButton.hide()
        self.rightMakananButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftMakananButton = QPushButton(self)
        self.leftMakananButton.setGeometry(QRect(20, 207, 48, 48))
        self.leftMakananButton.setStyleSheet("background-image: url(img/left-btn.png);")
        self.leftMakananButton.clicked.connect(self.leftMakananButtonClicked)
        self.leftMakananButton.hide()
        self.leftMakananButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.rightMinumanButton = QPushButton(self)
        self.rightMinumanButton.setGeometry(QRect(1215, 470, 48, 48))
        self.rightMinumanButton.setStyleSheet("background-image: url(img/right-btn.png);")
        self.rightMinumanButton.clicked.connect(self.rightMinumanButtonClicked)
        self.rightMinumanButton.hide()

        self.leftMinumanButton = QPushButton(self)
        self.leftMinumanButton.setGeometry(QRect(20, 470, 48, 48))
        self.leftMinumanButton.setStyleSheet("background-image: url(img/left-btn.png);")
        self.leftMinumanButton.clicked.connect(self.leftMinumanButtonClicked)
        self.leftMinumanButton.hide()
        
        # Set up menu cards from cards
        self.initializeMenu()
        self.setUpDisplayMakanan()
        self.setUpDisplayMinuman()

        self.searchbar = QLineEdit(self)
        self.searchbar.setPlaceholderText("Cari Makanan/Minuman")
        self.searchbar.setFixedSize(1260, 42)
        self.searchbar.move(970, 81)
        self.searchbar.setGeometry(QRect(10, 10, 48, 48))
        self.searchbar.setStyleSheet(
            """QLineEdit { background-color: #04FFA5; color: black; border-radius: 10px }""")
        self.searchbar.setFont(fonts.inter14)
        
    def initializeMenu(self):
        # Set up empty menu cards
        self.makananCards = []
        for i in range(5):
            self.makananCards.append({})
            self.makananCards[i]["card"] = QLabel(self)
            self.makananCards[i]["card"].setGeometry(QRect(80 + (i * 230), 130, 200, 200))
            self.makananCards[i]["card"].setStyleSheet(f"background-color: {DARK_MODE_BG}")
            self.makananCards[i]["card"].setPixmap(QPixmap("img/card-template.png"))
            
            self.makananCards[i]["cardIllustration"] = QLabel(self)
            self.makananCards[i]["cardIllustration"].setGeometry(QRect(120 + (i*230), 142, 120, 95))
            self.makananCards[i]["cardIllustration"].setStyleSheet(f"background-color: {PRIMARY_GREEN}")
            self.makananCards[i]["cardIllustration"].setPixmap(QPixmap("img/push-up.png"))

            self.makananCards[i]["cardTitle"] = QLabel(self)
            self.makananCards[i]["cardTitle"].setGeometry(QRect(90 + (i*230), 260, 120, 20))
            self.makananCards[i]["cardTitle"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
            self.makananCards[i]["cardTitle"].setText("Title")
            self.makananCards[i]["cardTitle"].setFont(fonts.inter16bold)

            self.makananCards[i]["cardPrice"] = QLabel(self)
            self.makananCards[i]["cardPrice"].setText("Price")
            self.makananCards[i]["cardPrice"].setGeometry(QRect(92 + (i*230), 300, 80, 14))
            self.makananCards[i]["cardPrice"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
            self.makananCards[i]["cardPrice"].setFont(fonts.inter12)
            
            self.makananCards[i]["Spinbox"] = QtWidgets.QSpinBox(self)
            self.makananCards[i]["Spinbox"].setGeometry(QRect(230 + (i*230), 270, 42, 22))
            self.makananCards[i]["Spinbox"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
            self.makananCards[i]["Spinbox"].setObjectName("SpinBox")
            
        self.minumanCards = []
        for i in range(5):
            self.minumanCards.append({})
            self.minumanCards[i]["card"] = QLabel(self)
            self.minumanCards[i]["card"].setGeometry(QRect(80 + (i * 230), 150 + 245, 200, 200))
            self.minumanCards[i]["card"].setStyleSheet(f"background-color: {DARK_MODE_BG}")
            self.minumanCards[i]["card"].setPixmap(QPixmap("img/card-template.png"))
            
            self.minumanCards[i]["cardIllustration"] = QLabel(self)
            self.minumanCards[i]["cardIllustration"].setGeometry(QRect(120 + (i*230), 162 + 245, 120, 95))
            self.minumanCards[i]["cardIllustration"].setStyleSheet(f"background-color: {PRIMARY_GREEN}")
            self.minumanCards[i]["cardIllustration"].setPixmap(QPixmap("img/push-up.png"))

            self.minumanCards[i]["cardTitle"] = QLabel(self)
            self.minumanCards[i]["cardTitle"].setGeometry(QRect(90 + (i*230), 280 + 245, 120, 20))
            self.minumanCards[i]["cardTitle"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
            self.minumanCards[i]["cardTitle"].setText("Title")
            self.minumanCards[i]["cardTitle"].setFont(fonts.inter16bold)

            self.minumanCards[i]["cardPrice"] = QLabel(self)
            self.minumanCards[i]["cardPrice"].setText("Price")
            self.minumanCards[i]["cardPrice"].setGeometry(QRect(92 + (i*230), 320 + 245, 80, 14))
            self.minumanCards[i]["cardPrice"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
            self.minumanCards[i]["cardPrice"].setFont(fonts.inter12)
            
            self.minumanCards[i]["Spinbox"] = QtWidgets.QSpinBox(self)
            self.minumanCards[i]["Spinbox"].setGeometry(QRect(230 + (i*230), 290 + 245, 42, 22))
            self.minumanCards[i]["Spinbox"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
            self.minumanCards[i]["Spinbox"].setObjectName("SpinBox")

    def setUpDisplayMakanan(self):
        listMakanan = self.makanan
        print(type(listMakanan))
        start = self.pageMakanan*3
        for i in range(5):
            if start+i < len(listMakanan):
                self.makananCards[i]["cardTitle"].setText(listMakanan[start+i]["name"])
                ## INI MASI ERROR
                # if (listMakanan[start+i]["linkIllustration"][:4] == "http"):
                #     pixmap = QPixmap()
                #     request = requests.get(listMakanan[start+i]["linkIllustration"])
                #     pixmap.loadFromData(request.content)
                #     pixmap.scaledToHeight(120)
                #     self.makananCards[i]["cardIllustration"].setPixmap(pixmap.scaledToHeight(120))
                # else:
                #     self.makananCards[i]["cardIllustration"].setPixmap(QPixmap(listMakanan[start+i]["linkIllustration"]))
                rp_harga = "Rp " + str(listMakanan[start+i]["price"])
                self.makananCards[i]["cardPrice"].setText(rp_harga)
                
                self.makananCards[i]["card"].show()
                self.makananCards[i]["cardIllustration"].show()
                self.makananCards[i]["cardTitle"].show()
                self.makananCards[i]["cardPrice"].show()
                self.makananCards[i]["Spinbox"].show()
            else:
                self.makananCards[i]["card"].hide()
                self.makananCards[i]["cardIllustration"].hide()
                self.makananCards[i]["cardTitle"].hide()
                self.makananCards[i]["cardPrice"].hide()
                self.makananCards[i]["Spinbox"].hide()

        if self.pageMakanan == 0:
            self.leftMakananButton.hide()
        else:
            self.leftMakananButton.show()

        if start + 5 < len(listMakanan):
            self.rightMakananButton.show()
        else:
            self.rightMakananButton.hide()
            
    def setUpDisplayMinuman(self):
        listMinuman = self.minuman
        start = self.pageMinuman*3
        for i in range(5):
            if start+i < len(listMinuman):
                self.minumanCards[i]["cardTitle"].setText(listMinuman[start+i]["name"])
                
                ## INI MASI ERROR
                # if (listMinuman[start+i]["linkIllustration"][:4] == "http"):
                #     pixmap = QPixmap()
                #     request = requests.get(listMinuman[start+i]["linkIllustration"])
                #     pixmap.loadFromData(request.content)
                #     pixmap.scaledToHeight(120)
                #     self.minumanCards[i]["cardIllustration"].setPixmap(pixmap.scaledToHeight(120))
                # else:
                #     self.minumanCards[i]["cardIllustration"].setPixmap(QPixmap(listMinuman[start+i]["linkIllustration"]))
                rp_harga = "Rp " + str(listMinuman[start+i]["price"])
                self.minumanCards[i]["cardPrice"].setText(rp_harga)
                self.minumanCards[i]["card"].show()
                self.minumanCards[i]["cardIllustration"].show()
                self.minumanCards[i]["cardTitle"].show()
                self.minumanCards[i]["cardPrice"].show()
                self.minumanCards[i]["Spinbox"].show()
            else:
                self.minumanCards[i]["card"].hide()
                self.minumanCards[i]["cardIllustration"].hide()
                self.minumanCards[i]["cardTitle"].hide()
                self.minumanCards[i]["cardPrice"].hide()
                self.minumanCards[i]["Spinbox"].hide()

        if self.pageMinuman == 0:
            self.leftMinumanButton.hide()
        else:
            self.leftMinumanButton.show()

        if start + 5 < len(listMinuman):
            self.rightMinumanButton.show()
        else:
            self.rightMinumanButton.hide()
      
    def rightMakananButtonClicked(self):
        if self.pageMakanan < (len(self.makanan)-1)//3:
            self.pageMakanan += 1
            self.setUpDisplayMakanan()
      
    def leftMakananButtonClicked(self):
        if self.pageMakanan > 0:
            self.pageMakanan -= 1
            self.setUpDisplayMakanan()

    def rightMinumanButtonClicked(self):
        if self.pageMinuman + 1 < (len(self.minuman)//3):
            self.pageMinuman += 1
            self.setUpDisplayMinuman()

    def leftMinumanButtonClicked(self):
        if self.pageMinuman > 0:
            self.pageMinuman -= 1
            self.setUpDisplayMinuman()

    def fetchMakanan(self):
        dataMakanan = []
        for i in range(len(makanan)):
              dataMakanan.append({
                "id": makanan[i]["id"],
                "name": makanan[i]["nama"],
                "price": makanan[i]["harga"],
                #"stock": makanan[i]["jumlahStok"],
                "linkIllustration": makanan[i]["fotoUrl"]
            })
        self.makanan = dataMakanan
        
    def fetchMinuman(self):
        dataMinuman = []
        for i in range(len(minuman)):
              dataMinuman.append({
                "id": minuman[i]["id"],
                "name": minuman[i]["nama"],
                "price": minuman[i]["harga"],
                # "stock": minuman[i]["jumlahStok"],
                "linkIllustration": minuman[i]["fotoUrl"],
            })
        self.minuman = dataMinuman
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec())