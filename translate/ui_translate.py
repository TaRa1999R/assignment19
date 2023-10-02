# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translate.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(390, 361)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(30, 20, 331, 81))
        font = QFont()
        font.setPointSize(13)
        self.input.setFont(font)
        self.input.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.output = QLineEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(30, 200, 331, 81))
        self.output.setFont(font)
        self.output.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.EtoP = QRadioButton(self.centralwidget)
        self.EtoP.setObjectName(u"EtoP")
        self.EtoP.setGeometry(QRect(40, 120, 141, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.EtoP.setFont(font1)
        self.EtoP.setStyleSheet(u"color: rgb(0, 144, 70);")
        self.PtoE = QRadioButton(self.centralwidget)
        self.PtoE.setObjectName(u"PtoE")
        self.PtoE.setGeometry(QRect(40, 150, 141, 20))
        self.PtoE.setFont(font1)
        self.PtoE.setStyleSheet(u"color: rgb(0, 144, 70);")
        self.translate = QPushButton(self.centralwidget)
        self.translate.setObjectName(u"translate")
        self.translate.setGeometry(QRect(210, 120, 131, 51))
        self.translate.setFont(font)
        self.translate.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 390, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.input.setText("")
        self.output.setText("")
        self.EtoP.setText(QCoreApplication.translate("MainWindow", u"English to Persian", None))
        self.PtoE.setText(QCoreApplication.translate("MainWindow", u"Persian to English", None))
        self.translate.setText(QCoreApplication.translate("MainWindow", u"translate", None))
    # retranslateUi

