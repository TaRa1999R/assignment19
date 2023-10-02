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
        MainWindow.resize(371, 337)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.translate = QPushButton(self.centralwidget)
        self.translate.setObjectName(u"translate")
        self.translate.setGeometry(QRect(210, 120, 141, 51))
        font = QFont()
        font.setPointSize(13)
        self.translate.setFont(font)
        self.translate.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"")
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(20, 20, 331, 81))
        self.input.setFont(font)
        self.input.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"")
        self.input.setAlignment(Qt.AlignCenter)
        self.output = QLineEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(20, 190, 331, 81))
        self.output.setFont(font)
        self.output.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"")
        self.output.setAlignment(Qt.AlignCenter)
        self.EtoP = QRadioButton(self.centralwidget)
        self.EtoP.setObjectName(u"EtoP")
        self.EtoP.setGeometry(QRect(30, 110, 131, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.EtoP.setFont(font1)
        self.EtoP.setStyleSheet(u"color: rgb(0, 136, 66);")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(30, 150, 131, 20))
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setStyleSheet(u"color: rgb(0, 136, 66);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 371, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.translate.setText(QCoreApplication.translate("MainWindow", u"translate", None))
        self.input.setInputMask("")
        self.input.setText("")
        self.output.setText("")
        self.EtoP.setText(QCoreApplication.translate("MainWindow", u"English to Persian", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Persian to English", None))
    # retranslateUi

