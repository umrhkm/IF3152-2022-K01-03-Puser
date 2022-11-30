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
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal, QRect
from PyQt6.QtGui import QCursor, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton, QWidget, QCompleter, QMessageBox)
import client.fonts

# Kalo program udah jadi, buka aja comment ini
response = requests.get("http://localhost:5000/api/menus/")

jsonresponse = response.json()
makanan = [x for x in jsonresponse if x['kategori'] == 'makanan']
minuman = [x for x in jsonresponse if x['kategori'] == 'minuman']

modelmakanan = [sub['nama'] for sub in makanan]
modelminuman = [sub['nama'] for sub in minuman]
model = modelmakanan+modelminuman
            
# Buat ngetes, biar ga request-request dulu

# makanan = [{'fotoUrl': 'https://w7.pngwing.com/pngs/201/77/png-transparent-hamburger-veggie-burger-take-out-fast-food-kebab-delicious-beef-burger-burger-with-lettuce-tomato-and-cheese-food-beef-recipe.png', 'harga': 25000, 'id': 1, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Original Burger'}, {'fotoUrl': None, 'harga': 22000, 'id': 2, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Chicken Burger'}, {'fotoUrl': None, 'harga': 40000, 'id': 3, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Beef Burger'}, {'fotoUrl': None, 'harga': 20000, 'id': 4, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Cheese Burger'}]
# minuman = [{'fotoUrl': None, 'harga': 8000, 'id': 8, 'jumlahStok': 2, 'kategori': 'minuman', 'nama': 'Coca Cola'}, {'fotoUrl': None, 'harga': 8000, 'id': 7, 'jumlahStok': 2, 'kategori': 'minuman', 'nama': 'Fanta'}, {'fotoUrl': None, 'harga': 8000, 'id': 6, 'jumlahStok': 0, 'kategori': 'minuman', 'nama': 'Sprite'}, {'fotoUrl': None, 'harga': 5000, 'id': 5, 'jumlahStok': 0, 'kategori': 'minuman', 'nama': 'Air Mineral'}]
# modelmakanan = [sub['nama'] for sub in makanan]
# modelminuman = [sub['nama'] for sub in minuman]
# model = modelmakanan+modelminuman

from PyQt6.QtGui import QFont 

class MenuWindow(QWidget):
    switch = pyqtSignal(str, dict)
    totalHarga = 0
    
    def __init__(self):
        super().__init__()

        self.startIndeksMakanan = 0
        self.startIndeksMinuman = 0
        self.startIndeksSearchMakanan = 0
        self.startIndeksSearchMinuman = 0
        self.pageMakanan = 0
        self.pageMinuman = 0
        self.pageMakananSearch = 0
        self.pageMinumanSearch = 0
        self.dataSearchMakanan = []
        self.dataSearchMinuman = []
        
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
        logoImg = QPixmap("client/img/Puser.png")
        logo.setPixmap(logoImg)
        logo.move(572, 20)

        # Label untuk teks di bawah logo
        silakanText = QLabel(self)
        silakanText.setText("Silakan Pilih Menu Makanan / Minuman Anda")
        silakanText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        silakanText.move(400, 60)
        silakanText.setFont(client.fonts.inter24)
        
        makananText = QLabel(self)
        makananText.setText("Makanan")
        makananText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        makananText.move(50, 100)
        makananText.setFont(client.fonts.inter18bold)
        
        minumanText = QLabel(self)
        minumanText.setText("Minuman")
        minumanText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        minumanText.move(50, 380)
        minumanText.setFont(client.fonts.inter18bold)
        
        # Set up previous / next button
        self.rightMakananButton = QPushButton(self)
        self.rightMakananButton.setGeometry(QRect(1215, 217, 48, 48))
        self.rightMakananButton.setStyleSheet("background-image: url(client/img/right-btn.png);")
        self.rightMakananButton.clicked.connect(self.rightMakananButtonClicked)
        self.rightMakananButton.hide()
        self.rightMakananButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftMakananButton = QPushButton(self)
        self.leftMakananButton.setGeometry(QRect(20, 217, 48, 48))
        self.leftMakananButton.setStyleSheet("background-image: url(client/img/left-btn.png);")
        self.leftMakananButton.clicked.connect(self.leftMakananButtonClicked)
        self.leftMakananButton.hide()
        self.leftMakananButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.rightMinumanButton = QPushButton(self)
        self.rightMinumanButton.setGeometry(QRect(1215, 480, 48, 48))
        self.rightMinumanButton.setStyleSheet("background-image: url(client/img/right-btn.png);")
        self.rightMinumanButton.clicked.connect(self.rightMinumanButtonClicked)
        self.rightMinumanButton.hide()
        self.rightMinumanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftMinumanButton = QPushButton(self)
        self.leftMinumanButton.setGeometry(QRect(20, 480, 48, 48))
        self.leftMinumanButton.setStyleSheet("background-image: url(client/img/left-btn.png);")
        self.leftMinumanButton.clicked.connect(self.leftMinumanButtonClicked)
        self.leftMinumanButton.hide()
        self.leftMinumanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.rightSearchMakananButton = QPushButton(self)
        self.rightSearchMakananButton.setGeometry(QRect(1215, 217, 48, 48))
        self.rightSearchMakananButton.setStyleSheet("background-image: url(client/img/right-btn.png);")
        self.rightSearchMakananButton.clicked.connect(self.rightSearchMakananButtonClicked)
        self.rightSearchMakananButton.hide()
        self.rightSearchMakananButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftSearchMakananButton = QPushButton(self)
        self.leftSearchMakananButton.setGeometry(QRect(20, 217, 48, 48))
        self.leftSearchMakananButton.setStyleSheet("background-image: url(client/img/left-btn.png);")
        self.leftSearchMakananButton.clicked.connect(self.leftSearchMakananButtonClicked)
        self.leftSearchMakananButton.hide()
        self.leftSearchMakananButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.rightSearchMinumanButton = QPushButton(self)
        self.rightSearchMinumanButton.setGeometry(QRect(1215, 480, 48, 48))
        self.rightSearchMinumanButton.setStyleSheet("background-image: url(client/img/right-btn.png);")
        self.rightSearchMinumanButton.clicked.connect(self.rightSearchMinumanButtonClicked)
        self.rightSearchMinumanButton.hide()
        self.rightSearchMinumanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.leftSearchMinumanButton = QPushButton(self)
        self.leftSearchMinumanButton.setGeometry(QRect(20, 480, 48, 48))
        self.leftSearchMinumanButton.setStyleSheet("background-image: url(client/img/left-btn.png);")
        self.leftSearchMinumanButton.clicked.connect(self.leftSearchMinumanButtonClicked)
        self.leftSearchMinumanButton.hide()
        self.leftSearchMinumanButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
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
        self.searchbar.setFont(client.fonts.inter14)
        self.searchbar.returnPressed.connect(self.search)

        self.completer = QCompleter(model)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)
        
        self.totalPriceText = QLabel(self)
        self.totalPriceText.setText("Rp 0000000000000" + str(self.totalHarga))
        self.totalPriceText.setStyleSheet(f'color: {DARK_MODE_BG}')
        self.totalPriceText.move(50, 665)
        self.totalPriceText.setFont(client.fonts.inter24bold)
        
        self.totalHargaText = QLabel(self)
        self.totalHargaText.setText("Total Harga")
        self.totalHargaText.setStyleSheet(f'color: {DARK_MODE_BG}')
        self.totalHargaText.move(50, 645)
        self.totalHargaText.setFont(client.fonts.inter14bold)
        
        self.checkOutText = QPushButton(self)
        self.checkOutText.setText("Check Out")
        self.checkOutText.move(550, 650)
        self.checkOutText.setFixedSize(180, 50)
        self.checkOutText.setStyleSheet(f"color: {PRIMARY_WHITE}; background-color: {'#696969'}; border-color: {'#696969'}; border-radius: 12px")
        self.checkOutText.setFont(client.fonts.inter24bold)
        self.checkOutText.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkOutText.clicked.connect(self.on_checkoutButton_clicked)
        self.checkOutText.setEnabled(False)
        # self.qrdialog = QRWindow()

        # button kembali
        self.kembaliButton = QPushButton(self)
        self.kembaliButton.setText("Kembali")
        self.kembaliButton.setFixedSize(180, 42)
        self.kembaliButton.move(50, 50)
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
        self.kembaliButton.setFont(client.fonts.inter18)
        self.kembaliButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kembaliButton.clicked.connect(self.dita)
    
    def dita(self):
        self.switch.emit("dita",{})

    def on_checkoutButton_clicked(self):
        from client.controller import status, tableNumber            
        flag = True
        for i in range(len(makanan)):
            if (makanan[i]["jumlahStok"]) < self.makananCards[i]["Spinbox"].value():
                flag = False
        for i in range(len(minuman)):
            if (minuman[i]["jumlahStok"]) < self.minumanCards[i]["Spinbox"].value():
                flag = False
        if flag:
            # Add to detail pesanan
            responsecounter = requests.get("http://localhost:5000/api/detail-pesanan/")
            counterdetail = responsecounter.json()
            counter = len(counterdetail) + 1
            dita_status = True
            
            if status == 'Take away':
                dita_status = False
            if dita_status:
                requests.post("http://localhost:5000/api/detail-pesanan/add", json={"dine_in_status": True})
                requests.put(f"http://localhost:5000/api/detail-pesanan/update/nomor-meja/{counter}", json={"nomor_meja": tableNumber})
            else:
                requests.post("http://localhost:5000/api/detail-pesanan/add", json={"dine_in_status": False})
            
            # Add detail menu to pesanan
            # Makanan
            for i in range(len(makanan)):
                if self.makananCards[i]["Spinbox"].value() != 0:
                    id = makanan[i]['id']
                    kuantitasMakanan = makanan[i]["jumlahStok"]
                    kuantitas = self.makananCards[i]["Spinbox"].value()
                    catatan = self.makananCards[i]["Notes"].text()
                    print("stok", kuantitasMakanan-kuantitas)
                    requests.post("http://localhost:5000/api/pesanan/add", json={"id_pesanan":counter, "id_menu":id, "kuantitas": kuantitas})
                    requests.put(f"http://localhost:5000/api/pesanan/update/catatan/{counter}/{id}", json={"catatan": str(catatan)})
                    requests.put(f"http://localhost:5000/api/menus/update/jumlah-stok/{id}", json={"jumlahStok":kuantitasMakanan-kuantitas})
            # Minuman
            for i in range(len(minuman)):
                if self.minumanCards[i]["Spinbox"].value() != 0:
                    id = minuman[i]['id']
                    kuantitasMinuman = minuman[i]["jumlahStok"]
                    kuantitas = self.minumanCards[i]["Spinbox"].value()
                    catatan = self.minumanCards[i]["Notes"].text()
                    print("stok", kuantitasMinuman-kuantitas)
                    requests.post("http://localhost:5000/api/pesanan/add", json={"id_pesanan":counter, "id_menu":id, "kuantitas": kuantitas})
                    requests.put(f"http://localhost:5000/api/pesanan/update/catatan/{counter}/{id}", json={"catatan": str(catatan)})
                    requests.put(f"http://localhost:5000/api/menus/update/jumlah-stok/{id}", json={"jumlahStok":kuantitasMinuman-kuantitas})
            self.switch.emit("qr",{})
            
        else:
            self.pesananNotValid()
    
    def cardMakananPositioning(self, flag, i):
        self.makananCards[flag]["card"].setGeometry(QRect(80 + (i * 230), 130, 200, 220))
        self.makananCards[flag]["cardIllustration"].setGeometry(QRect(136 + (i*230), 142, 120, 95))
        self.makananCards[flag]["cardTitle"].setGeometry(QRect(90 + (i*230), 255, 120, 20))
        self.makananCards[flag]["cardPrice"].setGeometry(QRect(90 + (i*230), 277, 80, 14))
        self.makananCards[flag]["cardStock"].setGeometry(QRect(90 + (i*230), 293, 80, 14))
        self.makananCards[flag]["Spinbox"].setGeometry(QRect(230 + (i*230), 280, 42, 22))
        self.makananCards[flag]["Notes"].setGeometry(QRect(90 + (i*230), 315, 50, 10))
        
    def cardMinumanPositioning(self, flagMinuman, i):
        self.minumanCards[flagMinuman]["card"].setGeometry(QRect(80 + (i * 230), 165 + 245, 200, 220))
        self.minumanCards[flagMinuman]["cardIllustration"].setGeometry(QRect(136 + (i*230), 182 + 245, 95, 95))
        self.minumanCards[flagMinuman]["cardTitle"].setGeometry(QRect(90 + (i*230), 290 + 245, 120, 20))
        self.minumanCards[flagMinuman]["cardPrice"].setGeometry(QRect(90 + (i*230), 312 + 245, 80, 14))
        self.minumanCards[flagMinuman]["cardStock"].setGeometry(QRect(90 + (i*230), 328 + 245, 80, 14))
        self.minumanCards[flagMinuman]["Spinbox"].setGeometry(QRect(230 + (i*230), 315 + 245, 42, 22))
        self.minumanCards[flagMinuman]["Notes"].setGeometry(QRect(90 + (i*230), 280+ 315, 50, 10))
        
    def initializeMenu(self):
        # Set up empty menu cards
        self.makananCards = []
        flag = 0
        while flag < len(makanan):
            for i in range(5):
                self.makananCards.append({})
                self.makananCards[flag]["card"] = QLabel(self)
                self.makananCards[flag]["card"].setStyleSheet(f"background-color: {DARK_MODE_BG}")
                self.makananCards[flag]["card"].setPixmap(QPixmap("client/img/card-template-new.png"))
                
                self.makananCards[flag]["cardIllustration"] = QLabel(self)
                self.makananCards[flag]["cardIllustration"].setStyleSheet(f"background-color: {PRIMARY_GREEN}")
                self.makananCards[flag]["cardIllustration"].setPixmap(QPixmap("client/img/default-icon.png"))

                self.makananCards[flag]["cardTitle"] = QLabel(self)
                self.makananCards[flag]["cardTitle"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.makananCards[flag]["cardTitle"].setText("Title")
                self.makananCards[flag]["cardTitle"].setFont(client.fonts.inter15bold)

                self.makananCards[flag]["cardPrice"] = QLabel(self)
                self.makananCards[flag]["cardPrice"].setText("Price")
                self.makananCards[flag]["cardPrice"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.makananCards[flag]["cardPrice"].setFont(client.fonts.inter12)
                
                self.makananCards[flag]["cardStock"] = QLabel(self)
                self.makananCards[flag]["cardStock"].setText("Stock")
                self.makananCards[flag]["cardStock"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.makananCards[flag]["cardStock"].setFont(client.fonts.inter12)

                self.makananCards[flag]["Spinbox"] = QtWidgets.QSpinBox(self)
                self.makananCards[flag]["Spinbox"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.makananCards[flag]["Spinbox"].setObjectName("SpinBox")
                self.makananCards[flag]["Spinbox"].valueChanged.connect(lambda x, i=flag: self.spinboxMakananClicked(i))
                
                self.makananCards[flag]["Notes"] = QtWidgets.QLineEdit(self)
                self.makananCards[flag]["Notes"].setFixedSize(125,20)
                self.makananCards[flag]["Notes"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {PRIMARY_WHITE}")
                self.makananCards[flag]["Notes"].setPlaceholderText("tambah catatan")
                self.makananCards[flag]["Notes"].setFont(client.fonts.inter11)
                
                self.cardMakananPositioning(flag, i)
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
                self.minumanCards[flagMinuman]["card"].setStyleSheet(f"background-color: {DARK_MODE_BG}")
                self.minumanCards[flagMinuman]["card"].setPixmap(QPixmap("client/img/card-template-new.png"))
                
                self.minumanCards[flagMinuman]["cardIllustration"] = QLabel(self)
                self.minumanCards[flagMinuman]["cardIllustration"].setStyleSheet(f"background-color: {PRIMARY_GREEN}")
                self.minumanCards[flagMinuman]["cardIllustration"].setPixmap(QPixmap("client/img/default-icon.png"))

                self.minumanCards[flagMinuman]["cardTitle"] = QLabel(self)
                self.minumanCards[flagMinuman]["cardTitle"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.minumanCards[flagMinuman]["cardTitle"].setText("Title")
                self.minumanCards[flagMinuman]["cardTitle"].setFont(client.fonts.inter15bold)

                self.minumanCards[flagMinuman]["cardPrice"] = QLabel(self)
                self.minumanCards[flagMinuman]["cardPrice"].setText("Price")
                self.minumanCards[flagMinuman]["cardPrice"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.minumanCards[flagMinuman]["cardPrice"].setFont(client.fonts.inter12)
                
                self.minumanCards[flagMinuman]["cardStock"] = QLabel(self)
                self.minumanCards[flagMinuman]["cardStock"].setText("Stock")
                self.minumanCards[flagMinuman]["cardStock"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.minumanCards[flagMinuman]["cardStock"].setFont(client.fonts.inter12)
                
                self.minumanCards[flagMinuman]["Spinbox"] = QtWidgets.QSpinBox(self)
                self.minumanCards[flagMinuman]["Spinbox"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {SECONDARY_GREEN}")
                self.minumanCards[flagMinuman]["Spinbox"].setObjectName("SpinBox")
                self.minumanCards[flagMinuman]["Spinbox"].valueChanged.connect(lambda x, i=flagMinuman: self.spinboxMinumanClicked(i))

                self.minumanCards[flagMinuman]["Notes"] = QtWidgets.QLineEdit(self)
                self.minumanCards[flagMinuman]["Notes"].setFixedSize(125,20)
                self.minumanCards[flagMinuman]["Notes"].setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {PRIMARY_WHITE}")
                self.minumanCards[flagMinuman]["Notes"].setPlaceholderText("tambah catatan")
                self.minumanCards[flagMinuman]["Notes"].setFont(client.fonts.inter11)
                
                self.cardMinumanPositioning(flagMinuman, i)
                self.hideMinuman(flagMinuman)

                if flagMinuman == len(minuman):
                    break
                else:
                    flagMinuman += 1

    def setUpDisplayMakanan(self):
        listMakanan = self.makanan
        start = 0
        i = 0
        while start < len(makanan):
            self.makananCards[start]["cardTitle"].setText(listMakanan[start]["name"])
            # buat ilustrasi
            self.makananCards[start]["cardIllustration"].setPixmap(QPixmap(f"client/img/makanan-{start}.png"))
            rp_harga = "Rp " + str(listMakanan[start]["price"])
            self.makananCards[start]["cardPrice"].setText(rp_harga)
            stock =  "Stok: " + str(listMakanan[start]["stock"])
            self.makananCards[start]["cardStock"].setText(stock)
            self.cardMakananPositioning(start, i)
            if (i==4):
                i = 0
            else:
                i += 1
            start += 1
            
        self.showDisplayMakanan(self.startIndeksMakanan, len(makanan))
        
        if self.pageMakanan == 0:
            self.leftMakananButton.hide()
        else:
            self.leftMakananButton.show()

        if self.startIndeksMakanan + 5 < len(makanan):
            self.rightMakananButton.show()
        else:
            self.rightMakananButton.hide()
            
    def setUpDisplaySearchMakanan(self):
        position = 0
        start = 0
        while start < len(self.dataSearchMakanan):
            self.cardMakananPositioning(self.dataSearchMakanan[start], position)
            if position == 4:
                position = 0
            else:
                position += 1
            start += 1
        validIdx = []
        for i in range(5):
            validIdx.append(i+self.startIndeksSearchMakanan)
        
        for i in range(len(self.dataSearchMakanan)):
            if i not in validIdx:
                self.hideMakanan(self.dataSearchMakanan[i])
            else:
                self.showMakanan(self.dataSearchMakanan[i])
                if (self.makananCards[self.dataSearchMakanan[i]]["Spinbox"].value() != 0):
                    self.makananCards[self.dataSearchMakanan[i]]["Notes"].show()
                else:
                    self.makananCards[self.dataSearchMakanan[i]]["Notes"].hide()
                    
        if self.pageMakananSearch == 0:
            self.leftSearchMakananButton.hide()
        else:
            self.leftSearchMakananButton.show()

        if self.startIndeksSearchMakanan + 5 < len(self.dataSearchMakanan):
            self.rightSearchMakananButton.show()
        else:
            self.rightSearchMakananButton.hide()
            
    def showDisplayMakanan(self, startIndeksMakanan, lenMakanan):
        validIdx = []
        for i in range(5):
            validIdx.append(i+startIndeksMakanan)
        for i in range(lenMakanan):
            if i not in validIdx:
                self.hideMakanan(i)
            else:
                self.showMakanan(i)
                if (self.makananCards[i]["Spinbox"].value() != 0):
                    self.makananCards[i]["Notes"].show()
                else:
                    self.makananCards[i]["Notes"].hide()
                
    def setUpDisplayMinuman(self):
        listMinuman = self.minuman
        start = 0
        i = 0
        while start < len(minuman):
            self.minumanCards[start]["cardTitle"].setText(listMinuman[start]["name"])
            # buat ilustrasi
            self.minumanCards[start]["cardIllustration"].setPixmap(QPixmap(f"client/img/minuman-{start}.png"))
            rp_harga = "Rp " + str(listMinuman[start]["price"])
            self.minumanCards[start]["cardPrice"].setText(rp_harga)
            stock =  "Stok: " + str(listMinuman[start]["stock"])
            self.minumanCards[start]["cardStock"].setText(stock)
            self.cardMinumanPositioning(start, i)
            if (i == 4):
                i = 0
            else:
                i += 1
            start += 1
            
        self.showDisplayMinuman(self.startIndeksMinuman, len(minuman))
            
        if self.pageMinuman == 0:
            self.leftMinumanButton.hide()
        else:
            self.leftMinumanButton.show()

        if self.startIndeksMinuman + 5 < len(listMinuman):
            self.rightMinumanButton.show()
        else:
            self.rightMinumanButton.hide()
            
    def setUpDisplaySearchMinuman(self):
        position = 0
        start = 0
        while start < len(self.dataSearchMinuman):
            self.cardMinumanPositioning(self.dataSearchMinuman[start], position)
            if position == 4:
                position = 0
            else:
                position += 1
            start += 1
        validIdx = []
        for i in range(5):
            validIdx.append(i+self.startIndeksSearchMinuman)
        
        for i in range(len(self.dataSearchMinuman)):
            if i not in validIdx:
                self.hideMinuman(self.dataSearchMinuman[i])
            else:
                self.showMinuman(self.dataSearchMinuman[i])
                if (self.minumanCards[self.dataSearchMinuman[i]]["Spinbox"].value() != 0):
                    self.minumanCards[self.dataSearchMinuman[i]]["Notes"].show()
                else:
                    self.minumanCards[self.dataSearchMinuman[i]]["Notes"].hide()
                    
        if self.pageMinumanSearch == 0:
            self.leftSearchMinumanButton.hide()
        else:
            self.leftSearchMinumanButton.show()

        if self.startIndeksSearchMinuman + 5 < len(self.dataSearchMinuman):
            self.rightSearchMinumanButton.show()
        else:
            self.rightSearchMinumanButton.hide()

    def showDisplayMinuman(self, startIndeksMinuman, lenMinuman):
        validIdx = []
        for i in range(5):
            validIdx.append(i+startIndeksMinuman)
        for i in range(lenMinuman):
            if i not in validIdx:
                self.hideMinuman(i)
            else:
                self.showMinuman(i)
                if (self.minumanCards[i]["Spinbox"].value() != 0):
                    self.minumanCards[i]["Notes"].show()
                else:
                    self.minumanCards[i]["Notes"].hide()

    def showMakanan(self, i):
        self.makananCards[i]["card"].show()
        self.makananCards[i]["cardIllustration"].show()
        self.makananCards[i]["cardTitle"].show()
        self.makananCards[i]["cardPrice"].show()
        self.makananCards[i]["cardStock"].show()
        self.makananCards[i]["Spinbox"].show()
    
    def hideMakanan(self, i):
        self.makananCards[i]["card"].hide()
        self.makananCards[i]["cardIllustration"].hide()
        self.makananCards[i]["cardTitle"].hide()
        self.makananCards[i]["cardPrice"].hide()
        self.makananCards[i]["cardStock"].hide()
        self.makananCards[i]["Spinbox"].hide()
        self.makananCards[i]["Notes"].hide()

    def showMinuman(self, i):
        self.minumanCards[i]["card"].show()
        self.minumanCards[i]["cardIllustration"].show()
        self.minumanCards[i]["cardTitle"].show()
        self.minumanCards[i]["cardPrice"].show()
        self.minumanCards[i]["cardStock"].show()
        self.minumanCards[i]["Spinbox"].show()

    def hideMinuman(self, i):
        self.minumanCards[i]["card"].hide()
        self.minumanCards[i]["cardIllustration"].hide()
        self.minumanCards[i]["cardTitle"].hide()
        self.minumanCards[i]["cardPrice"].hide()
        self.minumanCards[i]["cardStock"].hide()
        self.minumanCards[i]["Spinbox"].hide()
        self.minumanCards[i]["Notes"].hide()

    def pesananNotValid(self):
        self.msgBox = QMessageBox()
        self.msgBox.setText("Tidak dapat membuat pesanan \nStock tidak cukup!")
        self.msgBox.setWindowTitle("Pesanan gagal")
        self.msgBox.setIcon(QMessageBox.Icon.Warning)
        self.msgBox.setStyleSheet(f"Background-color: {PRIMARY_WHITE}")
        self.msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msgBox.exec()

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
        if self.pageMinuman < (len(self.minuman)//5):
            self.pageMinuman += 1
            self.startIndeksMinuman += 5
            self.setUpDisplayMinuman()

    def leftMinumanButtonClicked(self):
        if self.pageMinuman > 0:
            self.pageMinuman -= 1
            self.startIndeksMinuman -= 5
            self.setUpDisplayMinuman()
            
    def rightSearchMakananButtonClicked(self):
        if self.pageMakananSearch < (len(self.dataSearchMakanan)//5):
            self.pageMakananSearch += 1
            self.startIndeksSearchMakanan += 5
            self.setUpDisplaySearchMakanan()
            
    def leftSearchMakananButtonClicked(self):
        if self.pageMakananSearch > 0:
            self.pageMakananSearch -= 1
            self.startIndeksSearchMakanan -= 5
            self.setUpDisplaySearchMakanan()

    def rightSearchMinumanButtonClicked(self):
        if self.pageMinumanSearch < (len(self.dataSearchMinuman)//5):
            self.pageMinumanSearch += 1
            self.startIndeksSearchMinuman += 5
            self.setUpDisplaySearchMinuman()

    def leftSearchMinumanButtonClicked(self):
        if self.pageMinumanSearch > 0:
            self.pageMinumanSearch -= 1
            self.startIndeksSearchMinuman -= 5
            self.setUpDisplaySearchMinuman()

    def showMakananNotes(self, i):
        if (self.makananCards[i]["Spinbox"].value() != 0):
            self.makananCards[i]["Notes"].show()
        else:
            self.makananCards[i]["Notes"].hide()
    
    def showMinumanNotes(self, i):
        if (self.minumanCards[i]["Spinbox"].value() != 0):
            self.minumanCards[i]["Notes"].show()
        else:
            self.minumanCards[i]["Notes"].hide()
            
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
        if self.totalHarga == 0:
            self.checkOutText.setEnabled(False)
            self.checkOutText.setStyleSheet(f"color: {PRIMARY_WHITE}; background-color: {'#696969'}; border-color: {'#696969'}; border-radius: 12px")
        else:
            self.checkOutText.setEnabled(True)
            self.checkOutText.setStyleSheet(f"color: {PRIMARY_BLACK}; background-color: {PRIMARY_GREEN}; border-color: {PRIMARY_BLACK}; border-radius: 12px")
    
    def fetchMakanan(self):
        dataMakanan = []
        for i in range(len(makanan)):
            dataMakanan.append({
                "id": makanan[i]["id"],
                "name": makanan[i]["nama"],
                "price": makanan[i]["harga"],
                "stock": makanan[i]["jumlahStok"]
            })
        self.makanan = dataMakanan
        
    def fetchMinuman(self):
        dataMinuman = []
        for i in range(len(minuman)):
            dataMinuman.append({
                "id": minuman[i]["id"],
                "name": minuman[i]["nama"],
                "price": minuman[i]["harga"],
                "stock": minuman[i]["jumlahStok"]
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
    
    def resetCondition(self):
        self.rightSearchMakananButton.hide()
        self.leftSearchMakananButton.hide()
        self.rightSearchMinumanButton.hide()
        self.leftSearchMinumanButton.hide()
        self.rightMakananButton.hide()
        self.leftMakananButton.hide()
        self.rightMinumanButton.hide()
        self.leftMinumanButton.hide()
        self.startIndeksMakanan = 0
        self.startIndeksMinuman = 0
        self.startIndeksSearchMakanan = 0
        self.startIndeksSearchMinuman = 0
        self.pageMakanan = 0
        self.pageMinuman = 0
        self.pageMakananSearch = 0
        self.pageMinumanSearch = 0
        
    def search(self):
        # hide all button
        self.resetCondition()
        self.dataSearchMakanan.clear()
        self.dataSearchMinuman.clear()
        searchmenu = self.searchbar.text()
        
        # hide all cards
        for i in range(len(makanan)):
            self.hideMakanan(i)
        for i in range(len(minuman)):
            self.hideMinuman(i)
        
        # searching
        for i in range(len(makanan)):
            if (searchmenu.lower() in makanan[i]["nama"].lower()):
                self.dataSearchMakanan.append(i)
        for i in range(len(minuman)):
            if (searchmenu.lower() in minuman[i]["nama"].lower()):
                self.dataSearchMinuman.append(i)

        #if searchbar is clear
        if (searchmenu == ''):
            self.resetCondition()
            self.setUpDisplayMakanan()
            self.setUpDisplayMinuman()

        #if found in makanan
        elif (len(self.dataSearchMakanan) != 0):
            self.setUpDisplaySearchMakanan()
            # if also found in minuman
            if (len(self.dataSearchMinuman) != 0):
                self.setUpDisplaySearchMinuman()
            
        #if found in only minuman
        elif (len(self.dataSearchMinuman) != 0):
            self.setUpDisplaySearchMinuman()
        
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MenuWindow()
#     window.show()
#     sys.exit(app.exec())