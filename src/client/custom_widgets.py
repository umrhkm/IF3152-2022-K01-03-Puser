from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLabel


class ClickableLabel(QLabel):
  clicked = pyqtSignal()
  def __init__(self, parent = None):
    QLabel.__init__(self, parent = parent)
  
  def mousePressEvent(self, event):
    self.clicked.emit()