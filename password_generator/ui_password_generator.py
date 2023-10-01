# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_generator.ui'
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
        MainWindow.resize(390, 476)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(121, 121, 121);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.easy = QRadioButton(self.centralwidget)
        self.easy.setObjectName(u"easy")
        self.easy.setGeometry(QRect(70, 90, 251, 31))
        font = QFont()
        font.setPointSize(13)
        self.easy.setFont(font)
        self.easy.setStyleSheet(u"background-color: rgb(0, 255, 127);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.medium = QRadioButton(self.centralwidget)
        self.medium.setObjectName(u"medium")
        self.medium.setGeometry(QRect(70, 150, 251, 31))
        self.medium.setFont(font)
        self.medium.setStyleSheet(u"background-color: rgb(255, 160, 112);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.hard = QRadioButton(self.centralwidget)
        self.hard.setObjectName(u"hard")
        self.hard.setGeometry(QRect(70, 210, 251, 31))
        self.hard.setFont(font)
        self.hard.setStyleSheet(u"background-color: rgb(255, 61, 103);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(100, 20, 191, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.about.setFont(font1)
        self.about.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(100, 270, 191, 51))
        self.generate.setFont(font1)
        self.generate.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 350, 331, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.password.setFont(font2)
        self.password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(8, 8, 8);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.password.setMaxLength(20)
        self.password.setAlignment(Qt.AlignCenter)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generatore", None))
        self.easy.setText(QCoreApplication.translate("MainWindow", u"Standard Password", None))
        self.medium.setText(QCoreApplication.translate("MainWindow", u"Extra Strong Password", None))
        self.hard.setText(QCoreApplication.translate("MainWindow", u"Super Strong Password", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"generate", None))
        self.password.setText("")
    # retranslateUi

