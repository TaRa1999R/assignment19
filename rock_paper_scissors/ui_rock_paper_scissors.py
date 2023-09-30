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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(552, 616)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit, 6, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.lineEdit_6.setFont(font1)
        self.lineEdit_6.setStyleSheet(u"color: rgb(85, 85, 0);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px;")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.win = QLineEdit(self.centralwidget)
        self.win.setObjectName(u"win")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.win.sizePolicy().hasHeightForWidth())
        self.win.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.win.setFont(font2)
        self.win.setLayoutDirection(Qt.LeftToRight)
        self.win.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"border-top-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.win.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.win, 2, 0, 2, 4)

        self.paper = QPushButton(self.centralwidget)
        self.paper.setObjectName(u"paper")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.paper.sizePolicy().hasHeightForWidth())
        self.paper.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Emoji"])
        font3.setPointSize(12)
        self.paper.setFont(font3)
        self.paper.setStyleSheet(u"background-color: rgb(198, 198, 198);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px;")

        self.gridLayout.addWidget(self.paper, 7, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.computer = QLineEdit(self.centralwidget)
        self.computer.setObjectName(u"computer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.computer.sizePolicy().hasHeightForWidth())
        self.computer.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Emoji"])
        font4.setPointSize(15)
        self.computer.setFont(font4)
        self.computer.setStyleSheet(u"border-top-right-radius:50px;\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"border-bottom-left-radius:50px;")
        self.computer.setMaxLength(3)
        self.computer.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.computer, 1, 1, 1, 1)

        self.scissors = QPushButton(self.centralwidget)
        self.scissors.setObjectName(u"scissors")
        sizePolicy2.setHeightForWidth(self.scissors.sizePolicy().hasHeightForWidth())
        self.scissors.setSizePolicy(sizePolicy2)
        self.scissors.setFont(font3)
        self.scissors.setStyleSheet(u"background-color: rgb(198, 198, 198);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px;")

        self.gridLayout.addWidget(self.scissors, 7, 1, 1, 1)

        self.rock = QPushButton(self.centralwidget)
        self.rock.setObjectName(u"rock")
        sizePolicy2.setHeightForWidth(self.rock.sizePolicy().hasHeightForWidth())
        self.rock.setSizePolicy(sizePolicy2)
        self.rock.setFont(font3)
        self.rock.setStyleSheet(u"background-color: rgb(198, 198, 198);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px;")

        self.gridLayout.addWidget(self.rock, 7, 3, 1, 1)

        self.player = QLineEdit(self.centralwidget)
        self.player.setObjectName(u"player")
        sizePolicy3.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy3)
        self.player.setFont(font4)
        self.player.setStyleSheet(u"border-top-right-radius:50px;\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"border-bottom-left-radius:50px;")
        self.player.setMaxLength(3)
        self.player.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.player, 5, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setStyleSheet(u"color: rgb(85, 85, 0);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px;")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 552, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rock Paper Scissors", None))
        MainWindow.setWindowFilePath("")
        self.lineEdit.setText("")
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"Computer", None))
        self.win.setInputMask("")
        self.win.setText("")
        self.paper.setText(QCoreApplication.translate("MainWindow", u"\u270b\ud83c\udffb\n"
"paper", None))
        self.computer.setInputMask("")
        self.scissors.setText(QCoreApplication.translate("MainWindow", u"\u270c\ud83c\udffb\n"
"scissors", None))
        self.rock.setText(QCoreApplication.translate("MainWindow", u"\u270a\ud83c\udffb\n"
"rock", None))
        self.player.setInputMask("")
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Player", None))
    # retranslateUi

