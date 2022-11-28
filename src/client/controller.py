import os.path
import sys
from tkinter import E
from PyQt6.QtWidgets import QApplication

from client.dita_window import ditaWindow
from client.nomeja_window import nomejaWindow
from client.loading import SplashScreen
from client.menu_window import MenuWindow
from client.QRGenerator import QRWindow

class Controller:
    
    def __init__(self):
        # self.loading = SplashScreen()
        self.ditaWindow = ditaWindow()
        self.ditaWindow.switch.connect(self.fromDita)
        self.nomejaWindow = nomejaWindow()
        self.nomejaWindow.switch.connect(self.fromNomeja)
        self.MenuWindow = MenuWindow()
        self.MenuWindow.switch.connect(self.fromMenu)
        self.QRWindow = QRWindow()
        self.QRWindow.switch.connect(self.fromQR)

    def start(self):
        # self.loading.show()
        self.ditaWindow.show()
    
    def fromDita(self, page):
        self.ditaWindow.close()
        if page == "nomeja":
            self.nomejaWindow.show()
        elif page=="menu":
            self.MenuWindow.show()

    def fromNomeja(self,page):
        self.nomejaWindow.close()
        if page == "dita":
            self.ditaWindow.show()
        elif page=="menu":
            self.MenuWindow.show()

    def fromMenu(self,page):
        self.MenuWindow.close()
        if page == "qr":
            self.QRWindow.show()
        elif page == "dita":
            self.ditaWindow.show()

    def fromQR(self,page):
        self.QRWindow.close()
        if page == "dita":
            self.ditaWindow.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     controller = Controller()
#     controller.start()
#     sys.exit(app.exec())