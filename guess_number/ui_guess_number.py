# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guess_number.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(349, 290)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.guess = QLineEdit(self.centralwidget)
        self.guess.setObjectName(u"guess")
        self.guess.setGeometry(QRect(50, 20, 251, 61))
        font = QFont()
        font.setPointSize(25)
        font.setBold(False)
        self.guess.setFont(font)
        self.guess.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 170);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")
        self.guess.setAlignment(Qt.AlignCenter)
        self.state = QLineEdit(self.centralwidget)
        self.state.setObjectName(u"state")
        self.state.setGeometry(QRect(30, 190, 291, 41))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.state.setFont(font1)
        self.state.setStyleSheet(u"background-color: rgb(194, 164, 255);\n"
"color: rgb(117, 0, 175);\n"
"border-top-right-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.state.setAlignment(Qt.AlignCenter)
        self.check = QPushButton(self.centralwidget)
        self.check.setObjectName(u"check")
        self.check.setGeometry(QRect(40, 110, 121, 51))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.check.setFont(font2)
        self.check.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"border-top-right-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(190, 110, 121, 51))
        self.about.setFont(font2)
        self.about.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"border-top-right-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 349, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Guess Number", None))
        self.guess.setText("")
        self.state.setText("")
        self.check.setText(QCoreApplication.translate("MainWindow", u"check", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

