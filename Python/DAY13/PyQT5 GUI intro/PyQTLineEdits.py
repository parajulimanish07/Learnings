# PyQt5 QLabels

import sys #this allow us to use the system specific modules 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QRadioButton, QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super() calls the constructor of the parent class and __init__() is called of the child class 
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit (self)
        self.button= QPushButton("Submit", self)
        self.initUI()
    
    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210,10,100,40)
        self.line_edit.setStyleSheet("font-size:25px;"
                                     "font-family:Arial")
        self.button.setStyleSheet("font-size:25px;"
                                     "font-family:Arial")
        self.line_edit.setPlaceholderText("Enter your name")
        self.button.clicked.connect(self.submit)
    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}!")        

if __name__  == "__main__":
    app = QApplication(sys.argv) #this allows pyqt to process any command line arguments 
    window = MainWindow() #default behaviour is to hide  #window will be a parent parent widget
    window.show()
    sys.exit(app.exec_())
    main()
