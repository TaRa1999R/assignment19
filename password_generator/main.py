
import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow , QMessageBox
from ui_password_generator import Ui_MainWindow

class MainWindow ( QMainWindow ) :

    def __init__( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)

app = QApplication ( sys.argv )
window = MainWindow ()
window.show ()
app.exec ()