# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qrcode
import sys
 
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
        self._image = QImage(size, size, QImage.Format_RGB16)
 
        # initial image as white
        self._image.fill(Qt.white)
 
 
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
            QtCore.Qt.black)
 
 
# Main Window class
class Window(QMainWindow):
 
    # constructor
    def __init__(self):
        QMainWindow.__init__(self)
 
        # setting window title
        self.setWindowTitle("QR Code")
 
        # setting geometry
        self.setGeometry(100, 100, 300, 300)
 
        # creating a label to show the qr code
        self.label = QLabel(self)
 
        # adding action when entered is pressed
        self.handleTextEntered
 
        # creating a vertical layout
        layout = QVBoxLayout(self)
 
        # adding label to the layout
        layout.addWidget(self.label)
 
        # creating a QWidget object
        widget = QWidget()
 
        # setting layout to the widget
        widget.setLayout(layout)
 
        # setting widget as central widget to the main window
        self.setCentralWidget(widget)
 
 
    # method called by the line edit
    def handleTextEntered(self):
 
        # get the text
        text = 'youtube.com'
 
        # creating a pix map of qr code
        qr_image = qrcode.make(text, image_factory = Image).pixmap()
 
        # set image to the label
        self.label.setPixmap(qr_image)
 
 
 
 
# create PyQt5
# app
app = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# showing window
window.show()
 
# start the app
sys.exit(app.exec())
