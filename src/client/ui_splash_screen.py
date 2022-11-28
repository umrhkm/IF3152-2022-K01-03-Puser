# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenYjSmgx.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(687, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 170, 661, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 270, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.506, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(50, 300, 561, 21))
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 120, 151, 51))
        self.label.setPixmap(QPixmap(u"client/img/Puser.png"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" color:#b1b1b1;\">Aplikasi Pemesanan Makanan</span></p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#b1b1b1;\">loading...</span></p></body></html>", None))
        self.label.setText("")
    # retranslateUi

