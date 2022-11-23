# Form implementation generated from reading ui file 'aneh.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


# importing libraries
# from PyQt5.QtWidgets import *
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from custom_widgets import ClickableLabel
import qrcode
import sys
import fonts

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

# # Kalo program udah jadi, buka aja comment ini
# response = requests.get("http://localhost:5000/api/menus/")
# jsonresponse = response.json()
# makanan = [x for x in jsonresponse if x['kategori'] == 'makanan']
# minuman = [x for x in jsonresponse if x['kategori'] == 'minuman']

# Buat ngetes, biar ga request-request dulu
makanan = [{'fotoUrl': 'https://w7.pngwing.com/pngs/201/77/png-transparent-hamburger-veggie-burger-take-out-fast-food-kebab-delicious-beef-burger-burger-with-lettuce-tomato-and-cheese-food-beef-recipe.png', 'harga': 25000, 'id': 1, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Original Burger'}, {'fotoUrl': None, 'harga': 22000, 'id': 2, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Chicken Burger'}, {'fotoUrl': None, 'harga': 40000, 'id': 3, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Beef Burger'}, {'fotoUrl': None, 'harga': 20000, 'id': 4, 'jumlahStok': 0, 'kategori': 'makanan', 'nama': 'Cheese Burger'}]

minuman = [{'fotoUrl': None, 'harga': 8000, 'id': 8, 'jumlahStok': 2, 'kategori': 'minuman', 'nama': 'Coca Cola'}, {'fotoUrl': None, 'harga': 8000, 'id': 7, 'jumlahStok': 2, 'kategori': 'minuman', 'nama': 'Fanta'}, {'fotoUrl': None, 'harga': 8000, 'id': 6, 'jumlahStok': 0, 'kategori': 'minuman', 'nama': 'Sprite'}, {'fotoUrl': None, 'harga': 5000, 'id': 5, 'jumlahStok': 0, 'kategori': 'minuman', 'nama': 'Air Mineral'}]

# Image class for QR code
class Image(qrcode.image.base.BaseImage):
 
    # constructor
    def __init__(self, border, width, box_size):
 
        # assigning border
        self.border = border
 
        # assigning  width
        self.width = width
 
        # assigning box size
        self.box_size = box_size
 
        # creating size
        size = (width + border * 2) * box_size
 
        # image
        self._image = QImage(size, size, QImage.Format.Format_RGB16)
 
        # initial image as white
        self._image.fill(Qt.GlobalColor.white)
 
 
    # pixmap method
    def pixmap(self):
 
        # returns image
        return QPixmap.fromImage(self._image)
 
    # drawrect method for drawing rectangle
    def drawrect(self, row, col):
 
        # creating painter object
        painter = QPainter(self._image)
 
        # drawing rectangle
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,
            QtCore.Qt.GlobalColor.black)
 
 
# Main Window class
class QRWindow(QMainWindow):
 
    # constructor
    def __init__(self):
        QMainWindow.__init__(self)
 
        # setting window title
        self.setFixedSize(1280, 720)
        self.setWindowTitle("QR Code")
        self.setContentsMargins(100,100,100,200)
        # setting geometry
        #self.setGeometry(100, 100, 300, 300)
        self.setStyleSheet(f'background-color: {DARK_MODE_BG}')

        # Label untuk logo
        logo = QLabel(self)
        logoImg = QPixmap("img/Puser.png")
        logo.setPixmap(logoImg)
        logo.move(572, 20)

        # Label untuk teks di bawah logo
        silakanText = QLabel(self)
        silakanText.setText("Silakan scan untuk pembayaran")
        silakanText.setStyleSheet(f'color: {PRIMARY_WHITE}')
        silakanText.move(480, 90)
        silakanText.setFont(fonts.inter24)
        # silakanText.setAlignment(Qt.AlignmentFlag.AlignTop)
        # silakanText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # creating a label to show the qr code
        qRCode = QLabel(self)
         
        # get the text
        text = "testing"
 
        # creating a pix map of qr code
        qr_image = qrcode.make(text, image_factory = Image).pixmap()
 
        # set image to the label
        qRCode.setPixmap(qr_image)
        # qRCode.move(180,180)
        # qRCode.setAlignment(Qt.AlignmentFlag.AlignCenter)
 
        # creating a vertical layout
        layout = QGridLayout(self)
        # layout.columnCount() = 16
        # layout.rowCount() = 16

        # adding label to the layout
        layout.addWidget(QPushButton('Log In'),0,0, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(QLabel(''),0,3, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(silakanText,0,1, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(qRCode,1,1,alignment=Qt.AlignmentFlag.AlignHCenter)
 
        # creating a QWidget object
        widget = QWidget()
 
        # setting layout to the widget
        widget.setLayout(layout)
 
        # setting widget as central widget to the main window
        self.setCentralWidget(widget)
 
 
    # # method called by the line edit
    # def handleTextEntered(self):
 
    #     # get the text
    #     text = "Aku juga"
 
    #     # creating a pix map of qr code
    #     qr_image = qrcode.make(text, image_factory = Image).pixmap()
 
    #     # set image to the label
    #     self.label.setPixmap(qr_image)
 
 
 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRWindow()
    window.show()
    sys.exit(app.exec())