
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
        if self.ui.output.text () != "" :
            message = QMessageBox (windowTitle = "Erorr" , text = " you must write your input in blue box ")
            message.exec_ ()
            self.ui.output.setText ("")

        if self.mode == "E_to_P" :
            english = self.ui.input.text ()
            english_word = english.split (" ")
            persian = ""

            for word in english_word :
                for existence in self.Words_bank :
                    if word == existence["en"] :
                        persian += existence["fa"] + " "
                        break

                else :
                    persian += word + " "
            
            self.ui.output.setText (persian)

        elif self.mode == "P_to_E" :
            persian = self.ui.input.text ()
            persian_word = persian.split (" ")
            english = ""

            for word in persian_word :
                for existence in self.Words_bank :
                    if word == existence["fa"] :
                        english += existence["en"] + " "
                        break

                else :
                    english += word + " "
            
            self.ui.output.setText (english)


    def statement ( self , state ) :
        self.mode = state

app = QApplication ( sys.argv )
window = MainWindow ()
window.show ()
app.exec ()