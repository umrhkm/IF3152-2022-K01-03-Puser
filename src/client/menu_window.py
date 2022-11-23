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
import sys
import fonts
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal, QRect
from PyQt6.QtGui import QCursor, QPixmap, QImage
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton, QWidget, QCompleter)
from custom_widgets import ClickableLabel

# Kalo program udah jadi, buka aja comment ini
# response = requests.get("http://localhost:5000/api/menus/")

# jsonresponse = response.json()
# makanan = [x for x in jsonresponse if x['kategori'] == 'makanan']
# minuman = [x for x in jsonresponse if x['kategori'] == 'minuman']

# modelmakanan = [sub['nama'] for sub in makanan]
# modelminuman = [sub['nama'] for sub in minuman]
# model = modelmakanan+modelminuman

# Buat ngetes, biar ga request-request dulu

makanan = [{'fotoUrl': 'https://w7.pngwing.com/pngs/201/77/png-transparent-hamburger-veggie-burger-take-out-fast-food-kebab-delicious-beef-burger-burger-with-lettuce-tomato-and-cheese-food-beef-recipe.png', 'harga': 25000, 'id': 1, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Original Burger'}, {'fotoUrl': None, 'harga': 22000, 'id': 2, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Chicken Burger'}, {'fotoUrl': None, 'harga': 40000, 'id': 3, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Beef Burger'}, {'fotoUrl': None, 'harga': 20000, 'id': 4, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Cheese Burger'}]
minuman = [{'fotoUrl': None, 'harga': 8000, 'id': 8, 'jumlahStok': 2, 'kategori': 'minuman', 'nama': 'Coca Cola'}, {'fotoUrl': None, 'harga': 8000, 'id': 7, 'jumlahStok': 2, 'kategori': 'minuman', 'nama': 'Fanta'}, {'fotoUrl': None, 'harga': 8000, 'id': 6, 'jumlahStok': 0, 'kategori': 'minuman', 'nama': 'Sprite'}, {'fotoUrl': None, 'harga': 5000, 'id': 5, 'jumlahStok': 0, 'kategori': 'minuman', 'nama': 'Air Mineral'}]
modelmakanan = [sub['nama'] for sub in makanan]
modelminuman = [sub['nama'] for sub in minuman]
model = modelmakanan+modelminuman

class MenuWindow(QWidget):
    switch = pyqtSignal(str, dict)
    totalHarga = 0
    
    def __init__(self):
        super().__init__()

        self.startIndeksMakanan = 0
        self.startIndeksMinuman = 0
        self.pageMakanan = 0
        self.pageMinuman = 0
        
        self.fetchMakanan()
        self.fetchMinuman()
        self.setUpMenuWindow()

    def setUpMenuWindow(self):
        self.setFixedSize(1280, 720)
        self.setWindowTitle("Puser - Pilih Menu")
        self.setUpWidgets()
        
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
        minumanText.move(50, 380)
        minumanText.setFont(fonts.inter18bold)

        kembaliText = QPushButton(self)
        kembaliText.setText("Kembali")
        kembaliText.move(30, 20)
        kembaliText.setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: #DA6676")
        kembaliText.setFont(fonts.inter18bold)

        # Set up previous / next button
        self.rightMakananButton = QPushButton(self)
        self.rightMakananButton.setGeometry(QRect(1215, 217, 48, 48))
        self.rightMakananButton.setStyleSheet("background-image: url(img/right-btn.png);")
        self.rightMakananButton.clicked.connect(self.rightMakananButtonClicked)
        self.rightMakananButton.hide()
        self.rightMakananButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftMakananButton = QPushButton(self)
        self.leftMakananButton.setGeometry(QRect(20, 217, 48, 48))
        self.leftMakananButton.setStyleSheet("background-image: url(img/left-btn.png);")
        self.leftMakananButton.clicked.connect(self.leftMakananButtonClicked)
        self.leftMakananButton.hide()
        self.leftMakananButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.rightMinumanButton = QPushButton(self)
        self.rightMinumanButton.setGeometry(QRect(1215, 480, 48, 48))
        self.rightMinumanButton.setStyleSheet("background-image: url(img/right-btn.png);")
        self.rightMinumanButton.clicked.connect(self.rightMinumanButtonClicked)
        self.rightMinumanButton.hide()
        self.rightMinumanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftMinumanButton = QPushButton(self)
        self.leftMinumanButton.setGeometry(QRect(20, 480, 48, 48))
        self.leftMinumanButton.setStyleSheet("background-image: url(img/left-btn.png);")
        self.leftMinumanButton.clicked.connect(self.leftMinumanButtonClicked)
        self.leftMinumanButton.hide()
        self.leftMinumanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        # Set up menu cards from cards
        self.initializeMenu()
        self.setUpDisplayMakanan()
        self.setUpDisplayMinuman()

        self.searchbar = QLineEdit(self)
        self.searchbar.setPlaceholderText("Cari Makanan/Minuman")
        self.searchbar.setFixedSize(260, 42)
        # self.searchbar.move(970, 81)
        self.searchbar.setGeometry(QRect(1000, 50, 38, 38))
        self.searchbar.setStyleSheet(
            """QLineEdit { background-color: #04FFA5; color: black; border-radius: 10px; font-size:12px}""")
        self.searchbar.setFont(fonts.inter14)
        self.searchbar.returnPressed.connect(self.search)

        self.completer = QCompleter(model)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

        self.totalHargaText = QLabel(self)
        self.totalHargaText.setText("Total Harga")
        self.totalHargaText.setStyleSheet(f'color: {DARK_MODE_BG}')
        self.totalHargaText.move(50, 645)
        self.totalHargaText.setFont(fonts.inter14bold)
        
        self.totalPriceText = QLabel(self)
        self.totalPriceText.setText("Rp 0000000000000" + str(self.totalHarga))
        self.totalPriceText.setStyleSheet(f'color: {DARK_MODE_BG}')
        self.totalPriceText.move(50, 665)
        self.totalPriceText.setFont(fonts.inter24bold)

        self.checkOutText = QPushButton(self)
        self.checkOutText.setText("Check Out")
        self.checkOutText.move(575, 660)
        self.checkOutText.setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {DARK_MODE_BG}")
        self.checkOutText.setFont(fonts.inter24bold)
        self.checkOutText.clicked.connect(self.checkoutClicked)
        
        
    def initializeMenu(self):
        # Set up empty menu cards
        self.makananCards = []
        flag = 0
        while flag < len(makanan):
            for i in range(5):
                self.makananCards.append({})
                self.makananCards[flag]["card"] = QLabel(self)
                self.makananCards[flag]["card"].setGeometry(QRect(80 + (i * 230), 130, 200, 220))
                self.makananCards[flag]["card"].setStyleSheet(f"background-color: {DARK_MODE_BG}")
                self.makananCards[flag]["card"].setPixmap(QPixmap("img/card-template-new.png"))
                
                self.makananCards[flag]["cardIllustration"] = QLabel(self)
                self.makananCards[flag]["cardIllustration"].setGeometry(QRect(136 + (i*230), 142, 120, 95))
                self.makananCards[flag]["cardIllustration"].setStyleSheet(f"background-color: {PRIMARY_GREEN}")
                self.makananCards[flag]["cardIllustration"].setPixmap(QPixmap("img/push-up.png"))

                self.makananCards[flag]["cardTitle"] = QLabel(self)
                self.makananCards[flag]["cardTitle"].setGeometry(QRect(90 + (i*230), 255, 120, 20))
                self.makananCards[flag]["cardTitle"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.makananCards[flag]["cardTitle"].setText("Title")
                self.makananCards[flag]["cardTitle"].setFont(fonts.inter15bold)

                self.makananCards[flag]["cardPrice"] = QLabel(self)
                self.makananCards[flag]["cardPrice"].setText("Price")
                self.makananCards[flag]["cardPrice"].setGeometry(QRect(90 + (i*230), 285, 80, 14))
                self.makananCards[flag]["cardPrice"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.makananCards[flag]["cardPrice"].setFont(fonts.inter13)

                self.makananCards[flag]["Spinbox"] = QtWidgets.QSpinBox(self)
                self.makananCards[flag]["Spinbox"].setGeometry(QRect(230 + (i*230), 280, 42, 22))
                self.makananCards[flag]["Spinbox"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.makananCards[flag]["Spinbox"].setObjectName("SpinBox")
                self.makananCards[flag]["Spinbox"].valueChanged.connect(lambda x, i=flag: self.spinboxMakananClicked(i))
                
                self.makananCards[flag]["Notes"] = QtWidgets.QLineEdit(self)
                self.makananCards[flag]["Notes"].setFixedSize(125,20)
                self.makananCards[flag]["Notes"].setGeometry(QRect(90 + (i*230), 315, 50, 10))
                self.makananCards[flag]["Notes"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {PRIMARY_WHITE}")
                self.makananCards[flag]["Notes"].setPlaceholderText("tambah catatan")
                self.makananCards[flag]["Notes"].setFont(fonts.inter11)
                
                self.hideMakanan(flag)

                if flag == len(makanan):
                    break
                else:
                    flag += 1
                    
        self.minumanCards = []
        flagMinuman = 0
        while flagMinuman < len(minuman):
            for i in range(5):
                self.minumanCards.append({})
                self.minumanCards[flagMinuman]["card"] = QLabel(self)
                self.minumanCards[flagMinuman]["card"].setGeometry(QRect(80 + (i * 230), 165 + 245, 200, 220))
                self.minumanCards[flagMinuman]["card"].setStyleSheet(f"background-color: {DARK_MODE_BG}")
                self.minumanCards[flagMinuman]["card"].setPixmap(QPixmap("img/card-template-new.png"))
                
                self.minumanCards[flagMinuman]["cardIllustration"] = QLabel(self)
                self.minumanCards[flagMinuman]["cardIllustration"].setGeometry(QRect(136 + (i*230), 182 + 245, 95, 95))
                self.minumanCards[flagMinuman]["cardIllustration"].setStyleSheet(f"background-color: {PRIMARY_GREEN}")
                self.minumanCards[flagMinuman]["cardIllustration"].setPixmap(QPixmap("img/push-up.png"))

                self.minumanCards[flagMinuman]["cardTitle"] = QLabel(self)
                self.minumanCards[flagMinuman]["cardTitle"].setGeometry(QRect(90 + (i*230), 290 + 245, 120, 20))
                self.minumanCards[flagMinuman]["cardTitle"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.minumanCards[flagMinuman]["cardTitle"].setText("Title")
                self.minumanCards[flagMinuman]["cardTitle"].setFont(fonts.inter15bold)

                self.minumanCards[flagMinuman]["cardPrice"] = QLabel(self)
                self.minumanCards[flagMinuman]["cardPrice"].setText("Price")
                self.minumanCards[flagMinuman]["cardPrice"].setGeometry(QRect(90 + (i*230), 320 + 245, 80, 14))
                self.minumanCards[flagMinuman]["cardPrice"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.minumanCards[flagMinuman]["cardPrice"].setFont(fonts.inter12)
                
                self.minumanCards[flagMinuman]["Spinbox"] = QtWidgets.QSpinBox(self)
                self.minumanCards[flagMinuman]["Spinbox"].setGeometry(QRect(230 + (i*230), 315 + 245, 42, 22))
                self.minumanCards[flagMinuman]["Spinbox"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.minumanCards[flagMinuman]["Spinbox"].setObjectName("SpinBox")
                self.minumanCards[flagMinuman]["Spinbox"].valueChanged.connect(lambda x, i=flagMinuman: self.spinboxMinumanClicked(i))

                self.minumanCards[flagMinuman]["Notes"] = QtWidgets.QLineEdit(self)
                self.minumanCards[flagMinuman]["Notes"].setFixedSize(125,20)
                self.minumanCards[flagMinuman]["Notes"].setGeometry(QRect(90 + (i*230), 280+ 315, 50, 10))
                self.minumanCards[flagMinuman]["Notes"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {PRIMARY_WHITE}")
                self.minumanCards[flagMinuman]["Notes"].setPlaceholderText("tambah catatan")
                self.minumanCards[flagMinuman]["Notes"].setFont(fonts.inter11)
                
                self.hideMinuman(flagMinuman)
                
                if flagMinuman == len(minuman):
                    break
                else:
                    flagMinuman += 1

    def setUpDisplayMakanan(self):
        listMakanan = self.makanan
        start = 0
        while start < len(makanan):
            self.makananCards[start]["cardTitle"].setText(listMakanan[start]["name"])
            # buat ilustrasi
            self.makananCards[start]["cardIllustration"].setPixmap(QPixmap(f"img/makanan-{start}.png"))
            rp_harga = "Rp " + str(listMakanan[start]["price"])
            self.makananCards[start]["cardPrice"].setText(rp_harga)
            start += 1
            
        self.showDisplayMakanan()
        
        if self.pageMakanan == 0:
            self.leftMakananButton.hide()
        else:
            self.leftMakananButton.show()

        if self.startIndeksMakanan + 5 < len(makanan):
            self.rightMakananButton.show()
        else:
            self.rightMakananButton.hide()

    def showDisplayMakanan(self):
        validIdx = []
        for i in range(5):
            validIdx.append(i+self.startIndeksMakanan)
        for i in range(len(makanan)):
            if i not in validIdx:
                self.hideMakanan(i)
            else:
                self.showMakanan(i)
                    
        
    def setUpDisplayMinuman(self):
        listMinuman = self.minuman
        start = 0
        while start < len(minuman):
            self.minumanCards[start]["cardTitle"].setText(listMinuman[start]["name"])
            # buat ilustrasi
            self.minumanCards[start]["cardIllustration"].setPixmap(QPixmap(f"img/minuman-{start}.png"))
            rp_harga = "Rp " + str(listMinuman[start]["price"])
            self.minumanCards[start]["cardPrice"].setText(rp_harga)
            start += 1
            
        self.showDisplayMinuman()
            
        if self.pageMinuman == 0:
            self.leftMinumanButton.hide()
        else:
            self.leftMinumanButton.show()

        if self.startIndeksMinuman + 5 < len(listMinuman):
            self.rightMinumanButton.show()
        else:
            self.rightMinumanButton.hide()

    def showDisplayMinuman(self):
        validIdx = []
        for i in range(5):
            validIdx.append(i+self.startIndeksMinuman)
        for i in range(len(minuman)):
            if i not in validIdx:
                self.hideMinuman(i)
            else:
                self.showMinuman(i)

    def showMakanan(self, i):
        self.makananCards[i]["card"].show()
        self.makananCards[i]["cardIllustration"].show()
        self.makananCards[i]["cardTitle"].show()
        self.makananCards[i]["cardPrice"].show()
        self.makananCards[i]["Spinbox"].show()
        self.makananCards[i]["Notes"].hide()
        # if self.makananCards[i]["Spinbox"].value() == 0:
        #     self.makananCards[i]["Notes"].hide()
        # else:
        #     self.makananCards[i]["Notes"].show()
    
    def hideMakanan(self, i):
        self.makananCards[i]["card"].hide()
        self.makananCards[i]["cardIllustration"].hide()
        self.makananCards[i]["cardTitle"].hide()
        self.makananCards[i]["cardPrice"].hide()
        self.makananCards[i]["Spinbox"].hide()
        self.makananCards[i]["Notes"].hide()
        
    def showMinuman(self, i):
        self.minumanCards[i]["card"].show()
        self.minumanCards[i]["cardIllustration"].show()
        self.minumanCards[i]["cardTitle"].show()
        self.minumanCards[i]["cardPrice"].show()
        self.minumanCards[i]["Spinbox"].show()
        self.minumanCards[i]["Notes"].hide()
        # if self.minumanCards[i]["Spinbox"].value() == 0:
        #     self.minumanCards[i]["Notes"].hide()
        # else:
        #     self.minumanCards[i]["Notes"].show()
    
    def hideMinuman(self, i):
        self.minumanCards[i]["card"].hide()
        self.minumanCards[i]["cardIllustration"].hide()
        self.minumanCards[i]["cardTitle"].hide()
        self.minumanCards[i]["cardPrice"].hide()
        self.minumanCards[i]["Spinbox"].hide()
        self.minumanCards[i]["Notes"].hide()
                
    def rightMakananButtonClicked(self):
        if self.pageMakanan < (len(self.makanan)//5):
            self.pageMakanan += 1
            self.startIndeksMakanan += 5
            self.setUpDisplayMakanan()
            
    def leftMakananButtonClicked(self):
        if self.pageMakanan > 0:
            self.pageMakanan -= 1
            self.startIndeksMakanan -= 5
            self.setUpDisplayMakanan()

    def rightMinumanButtonClicked(self):
        if self.pageMakanan < (len(self.minuman)//5):
            self.pageMinuman += 1
            self.startIndeksMinuman += 5
            self.setUpDisplayMinuman()

    def leftMinumanButtonClicked(self):
        if self.pageMinuman > 0:
            self.pageMinuman -= 1
            self.startIndeksMinuman -= 5
            self.setUpDisplayMinuman()

    def updateHarga(self):
        dataHargaMakanan = [0] * len(makanan)
        j = 0
        for i in range(len(makanan)):
            total = self.makananCards[i]['Spinbox'].value() * makanan[i]['harga']
            dataHargaMakanan[j] = total
            j += 1
        dataHargaMinuman = [0] * len(minuman)
        k = 0
        for i in range(len(minuman)):
            total = self.minumanCards[i]['Spinbox'].value() * minuman[i]['harga']
            dataHargaMinuman[k] = total
            k += 1
        self.totalHarga = sum(dataHargaMakanan) + sum(dataHargaMinuman)
        self.totalPriceText.setText("Rp " + str(self.totalHarga))
        self.totalHargaText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        self.totalPriceText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        self.checkOutText.setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {PRIMARY_GREEN}")

        if self.totalHarga == 0:
            self.checkOutText.setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {DARK_MODE_BG}")
    
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

    def spinboxMakananClicked(self, idx):
        n = self.makananCards[idx]["Spinbox"].value()
        self.updateHarga()
        if (self.makananCards[idx]["Spinbox"].value() != 0):
            self.makananCards[idx]["Notes"].show()
        else:
            self.makananCards[idx]["Notes"].hide()

    def spinboxMinumanClicked(self, idx):
        n = self.minumanCards[idx]["Spinbox"].value()
        self.updateHarga()
        if (self.minumanCards[idx]["Spinbox"].value() != 0):
            self.minumanCards[idx]["Notes"].show()
        else:
            self.minumanCards[idx]["Notes"].hide()
    
    def search(self):
        try:
            responsesearch = requests.get('http://localhost:5000/api/menus/search-nama/'+self.searchbar.text())
            jsonresponsesearch = responsesearch.json()
            makanan = [x for x in jsonresponsesearch if x['kategori'] == 'makanan']
            minuman = [x for x in jsonresponsesearch if x['kategori'] == 'minuman']

            dataMakananSearch = []
            for i in range(len(makanan)):
                dataMakananSearch.append({
                    "id": makanan[i]["id"],
                    "name": makanan[i]["nama"],
                    "price": makanan[i]["harga"],
                    #"stock": makanan[i]["jumlahStok"],
                    "linkIllustration": makanan[i]["fotoUrl"]
                })
            self.makanan = dataMakananSearch

            listMakanan = self.makanan
            start = self.pageMakanan*5
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
                self.leftMakananButton.hide()
                for i in range(len(makanan)):
                    self.hideMakanan(i)
                start = 0
                while start < len(indexsearchmakanan):
                    self.showMakanan(indexsearchmakanan[start])
                    start += 1

            listMinuman = self.minuman
            start = self.pageMinuman*5
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
                self.leftMinumanButton.hide()
                for i in range(len(minuman)):
                    self.hideMinuman(i)
                start2 = 0
                while start2 < len(indexsearchminuman):
                    self.showMinuman(indexsearchminuman[start2])
                    start2 += 1
        except ValueError as e:
            self.fetchMakanan()
            self.setUpDisplayMakanan()
            self.fetchMinuman()
            self.setUpDisplayMinuman()

    def checkoutClicked(self):
        with open("tes.txt", "w") as f:
            f.write("Dine In\n")
            nomorMeja = 0
            f.write(f"Nomor Meja: {nomorMeja} \n")
            f.write("Pesanan Anda:\n\n")
            urutanMakanan = 1
            f.write("Makanan\n")
            flag = False
            for i in range(len(makanan)):
                if self.makananCards[i]["Spinbox"].value() != 0:
                    nama = self.makananCards[i]["cardTitle"].text()
                    kuantitas = self.makananCards[i]["Spinbox"].value()
                    catatan = self.makananCards[i]["Notes"].text()
                    f.write(f"{urutanMakanan}. {nama}: {kuantitas} buah\n")
                    f.write(f"Catatan tambahan: {catatan}\n")
                    urutanMakanan += 1
                    flag=True
            if not flag:
                f.write("Tidak ada makanan yang Anda pesan\n")
            f.write("\n")
            f.write("Minuman\n")
            urutanMinuman = 1
            flag = False
            for i in range(len(minuman)):
                if self.minumanCards[i]["Spinbox"].value() != 0:
                    nama = self.minumanCards[i]["cardTitle"].text()
                    kuantitas = self.minumanCards[i]["Spinbox"].value()
                    catatan = self.minumanCards[i]["Notes"].text()
                    f.write(f"{urutanMinuman}. {nama}: {kuantitas} buah\n")
                    f.write(f"Catatan tambahan: {catatan}\n")
                    urutanMinuman += 1
                    flag=True
            if not flag:
                f.write("Tidak ada minuman yang Anda pesan\n")
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec())
