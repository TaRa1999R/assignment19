
import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow , QMessageBox
from ui_puzzle_15 import Ui_MainWindow

class MainWindow ( QMainWindow ) :

    def __init__ ( self , num_list ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi ( self )
        self.buttons = [[ self.ui.one , self.ui.two , self.ui.three , self.ui.four ] ,
                        [ self.ui.five , self.ui.six , self.ui.seven , self.ui.eight ] ,
                        [self.ui.nine , self.ui.ten , self.ui.eleven , self.ui.tewelve ] ,
                        [ self.ui.thirteen , self.ui.fourteen , self.ui.fifteen , self.ui.sixteen ] ]
        
        
number_list = []
used_number = []
for i in range (4) :
    number = []
    while len(number) < 4 :
        x = random.randint ( 1 , 16 )
        if x not in used_number :
            number.append (x)
            used_number.append (x)
    
    number_list.append (number)

app = QApplication ( sys.argv )
window = MainWindow ( number_list )
window.show ()
app.exec ()