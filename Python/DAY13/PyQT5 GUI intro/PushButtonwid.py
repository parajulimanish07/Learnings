# PyQt5 QLabels

import sys #this allow us to use the system specific modules 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super() calls the constructor of the parent class and __init__() is called of the child class 
        self.setGeometry(700, 300, 500, 500)
        self.label = QLabel("Hello", self)
        self.initUI()
    
    def initUI(self):
        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size:50px;")

    def on_click(self):
        self.label.setText("Goodbye")

if __name__  == "__main__":
    app = QApplication(sys.argv) #this allows pyqt to process any command line arguments 
    window = MainWindow() #default behaviour is to hide  #window will be a parent parent widget
    window.show()
    sys.exit(app.exec_())
