# PyQt5 QLabels

import sys #this allow us to use the system specific modules 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget ,QHBoxLayout , QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super() calls the constructor of the parent class and __init__() is called of the child class 
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")


        self.setStyleSheet(""" 
             QPushButton {
                 font-size: 30px;
                 font-family: Arial;
                 padding: 15px 75px;
                 margin: 25px;
                 border: 3px solid;
                 border-radius: 15px;
              }

             QPushButton#button1 {
                 background-color: hsl(0, 100%, 60%);          
                            }
             QPushButton#button2 {
                 background-color: hsl(122,100%,64%);          
                            }
             QPushButton#button3 {
                 background-color: hsl(204,100%,64%);          
                            }
             QPushButton#button1:hover {
                 background-color: hsl(0, 100%, 80%);          
                            }
             QPushButton#button2:hover{
                 background-color: hsl(122,100%,84%);          
                            }
             QPushButton#button3:hover {
                 background-color: hsl(204,100%,84%);          
                            }
             """)

if __name__  == "__main__":
    app = QApplication(sys.argv) #this allows pyqt to process any command line arguments 
    window = MainWindow() #default behaviour is to hide  #window will be a parent parent widget
    window.show()
    sys.exit(app.exec_())
