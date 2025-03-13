# PyQt5 QLabels

import sys #this allow us to use the system specific modules 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QCheckBox)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super() calls the constructor of the parent class and __init__() is called of the child class 
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()
    
    def initUI(self):
      self.checkbox.setGeometry(0,0,500,100)
      self.checkbox.setStyleSheet("font-size:30px;"
                                  "font-family: Arial;")
      self.checkbox.setChecked(False)
      self.checkbox.stateChanged.connect(self.checkbox_changed)


    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You don't like food")   

if __name__  == "__main__":
    app = QApplication(sys.argv) #this allows pyqt to process any command line arguments 
    window = MainWindow() #default behaviour is to hide  #window will be a parent parent widget
    window.show()
    sys.exit(app.exec_())
    main()
