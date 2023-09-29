# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rock_paper_scissors.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(462, 558)
        mainWindow.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"border-top-right-radius:5px;\n"
"border-top-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"border-bottom-left-radius:5px")

        self.gridLayout.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.computer = QLineEdit(self.centralwidget)
        self.computer.setObjectName(u"computer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.computer.sizePolicy().hasHeightForWidth())
        self.computer.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Emoji"])
        font1.setPointSize(19)
        self.computer.setFont(font1)
        self.computer.setStyleSheet(u"border-top-right-radius:60px;\n"
"border-top-left-radius:60px;\n"
"border-bottom-right-radius:60px;\n"
"border-bottom-left-radius:60px")

        self.gridLayout.addWidget(self.computer, 1, 1, 1, 1)

        self.win = QLineEdit(self.centralwidget)
        self.win.setObjectName(u"win")
        sizePolicy.setHeightForWidth(self.win.sizePolicy().hasHeightForWidth())
        self.win.setSizePolicy(sizePolicy)
        self.win.setFont(font)
        self.win.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-top-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px")

        self.gridLayout.addWidget(self.win, 2, 0, 1, 3)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(u"color: rgb(0, 85, 0);border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.player = QLineEdit(self.centralwidget)
        self.player.setObjectName(u"player")
        sizePolicy1.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy1)
        self.player.setFont(font1)
        self.player.setStyleSheet(u"border-top-right-radius:60px;\n"
"border-top-left-radius:60px;\n"
"border-bottom-right-radius:60px;\n"
"border-bottom-left-radius:60px")

        self.gridLayout.addWidget(self.player, 4, 1, 1, 1)

        self.score = QLineEdit(self.centralwidget)
        self.score.setObjectName(u"score")
        sizePolicy.setHeightForWidth(self.score.sizePolicy().hasHeightForWidth())
        self.score.setSizePolicy(sizePolicy)
        self.score.setFont(font)
        self.score.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.gridLayout.addWidget(self.score, 5, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(19)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px")

        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(20)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px")

        self.gridLayout.addWidget(self.pushButton_3, 6, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px")

        self.gridLayout.addWidget(self.pushButton_2, 6, 2, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 462, 22))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Rock Paper Scissors", None))
        self.lineEdit_5.setInputMask(QCoreApplication.translate("mainWindow", u"             Computer", None))
        self.win.setInputMask("")
        self.lineEdit_4.setInputMask(QCoreApplication.translate("mainWindow", u"                 player", None))
        self.lineEdit_4.setText(QCoreApplication.translate("mainWindow", u"                 player", None))
        self.player.setInputMask("")
        self.score.setInputMask("")
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u270b\ud83c\udffb\n"
"papre", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"\u270a\ud83c\udffb\n"
"rock", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"\u270c\ud83c\udffb\n"
"scissors", None))
    # retranslateUi

