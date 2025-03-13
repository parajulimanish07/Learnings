# PyQT 5 introduction

import sys #this allow us to use the system specific modules 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super() calls the constructor of the parent class and __init__() is called of the child class 
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("manish.JPG"))
def main():
    app = QApplication(sys.argv) #this allows pyqt to process any command line arguments 
    window = MainWindow() #default behaviour is to hide 
    window.show()
    sys.exit(app.exec_())

if __name__  == "__main__":
    main()
