
import sys
from PySide6.QtWidgets import QApplication , QMainWindow 
from ui_line_break import Ui_MainWindow

class MainWindow ( QMainWindow ) :

    def __init__( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)
        self.ui.remove.clicked.connect (self.remove)
        self.output = ""

    def remove ( self ) :
        text = self.ui.input.text ()
        list = text.split ("\n")
        for part in list :
            self.output += part
        
        self.ui.output.setText (self.output)

app = QApplication ( sys.argv )
window = MainWindow ()
window.show ()
app.exec ()