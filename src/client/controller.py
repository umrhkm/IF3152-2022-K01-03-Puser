import os.path
import sys
from tkinter import E
from PyQt6.QtWidgets import QApplication

from dita_window import ditaWindow
from nomeja_window import nomejaWindow

class Controller:
    def __init__(self):
        self.ditaWindow = ditaWindow()
        self.ditaWindow.switch.connect(self.fromDita)
        self.nomejaWindow = nomejaWindow()
        self.nomejaWindow.switch.connect(self.fromNomeja)

    def start(self):
        self.ditaWindow.show()
    
    def fromDita(self):
        self.ditaWindow.close()
        self.nomejaWindow.show()

    def fromNomeja(self):
        self.nomejaWindow.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.start()
    sys.exit(app.exec())