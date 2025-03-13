# PyQt5 QLabels

import sys #this allow us to use the system specific modules 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super() calls the constructor of the parent class and __init__() is called of the child class 
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)\
        
        label1 = QLabel("#1" , self)
        label2 = QLabel("#2" , self)
        label3 = QLabel("#3" , self)
        label4 = QLabel("#4" , self)
        label5 = QLabel("#5" , self)        

        label1.setStyleSheet("background-color : red;")
        label2.setStyleSheet("background-color : blue;")
        label3.setStyleSheet("background-color : green;")
        label4.setStyleSheet("background-color : yellow;")
        label5.setStyleSheet("background-color : orange;")

        grid = QGridLayout() #calling the constructor
        
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1,1)
        grid.addWidget(label5, 2,2)
    
        central_widget.setLayout(grid) #set layout for the central widget
    
    
def main():
    app = QApplication(sys.argv) #this allows pyqt to process any command line arguments 
    window = MainWindow() #default behaviour is to hide  #window will be a parent parent widget
    window.show()
    sys.exit(app.exec_())

if __name__  == "__main__":
    main()
