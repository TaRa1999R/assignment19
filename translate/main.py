
import sys
from functools import partial
from PySide6.QtWidgets import QApplication , QMainWindow , QMessageBox
from ui_translate import Ui_MainWindow

class MainWindow ( QMainWindow ) :

    def __init__( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)
        
        f = open ("translate/translate.txt" , "r" )
        self.Words_bank = []
        file = f.read ()
        word = file.split ("\n")
        for i in range (0 , len (word) , 2) :
            dictionary = {"en" : word [i] , "fa" : word [i + 1] }
            self.Words_bank.append (dictionary)
        f.close ()

        self.ui.EtoP.setChecked (True)
        self.mode = "E_to_P"

        self.ui.EtoP.clicked.connect (partial (self.statement , "E_to_P"))
        self.ui.PtoE.clicked.connect (partial (self.statement , "P_to_E"))
        self.ui.translate.clicked.connect (self.translate)

    def translate ( self ) :
        if self.mode == "E_to_P" :
            print ("HI")

        elif self.mode == "P_to_E" :
            print ("hi")
    
    def statement ( self , state ) :
        self.mode = state

app = QApplication ( sys.argv )
window = MainWindow ()
window.show ()
app.exec ()