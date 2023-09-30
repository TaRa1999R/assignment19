
import random
import sys
from PySide6.QtWidgets import QApplication , QMainWindow , QMessageBox
from ui_guess_number import Ui_MainWindow

class MainWindow ( QMainWindow ) :

    def __init__ ( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)
        self.number = random.randint (1 , 100)
        self.guess_number = 0
        self.ui.about.clicked.connect (self.about)
        self.ui.check.clicked.connect (self.check)

    def about ( self ) :
        message = QMessageBox (WindowTitle = "about" , text = "You must guess a number between 1 to 100. Then type your guess in blue box\
and press 'check' botton to check it 🧐. You will see the result in purple box.")
        message.exec_ ()

    def check ( self ) :
        guess = int (self.ui.guess.text())
        self.ui.guess.setText ("")
        self.guess_number += 1
        if guess > self.number :
            text = f"its lower than {guess}"
            self.ui.state.setText (text)
        
        elif guess < self.number :
            text = f"its higher than {guess}"
            self.ui.state.setText (text)
        
        elif guess == self.number :
            text = f"🎉🎉You Win🎉🎉\nThe number was {self.number}.\nYou win after {self.guess_number} guess."
            self.ui.state.setText ("")
            message =  QMessageBox (WindowTitle = "Congratulation" , text = text)
            message.exec_ ()


app = QApplication ( sys.argv )
window = MainWindow ()
window.show ()
app.exec ()