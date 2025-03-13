# PyQt5 QLabels

import sys #this allow us to use the system specific modules 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super() calls the constructor of the parent class and __init__() is called of the child class 
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("manish.JPG")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                         ( self.height() - label.height()) // 2,
                          label.width(), label.height())

def main():
    app = QApplication(sys.argv) #this allows pyqt to process any command line arguments 
    window = MainWindow() #default behaviour is to hide  #window will be a parent parent widget
    window.show()
    sys.exit(app.exec_())

if __name__  == "__main__":
    main()
