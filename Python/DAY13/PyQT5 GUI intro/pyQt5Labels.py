# PyQt5 QLabels

import sys #this allow us to use the system specific modules 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super() calls the constructor of the parent class and __init__() is called of the child class 
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 0))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color:blue;"
                            "background-color: red;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration:underlined;") #css style sheet for the label
        # label.setAlignment(Qt.AlignTop) # vertically top
        # label.setAlignment(Qt.AlignBottom) #vertically bottom
        # label.setAlignment(Qt.AlignVCenter) #Vertically center the label
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignCenter)
        # label.setAlignment(Qt.AlignLeft)

        # label.setAlignment(Qt.AlignHCenter | Qt.AligntOP) # CENTER AND BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER AND BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER AND CENTER
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv) #this allows pyqt to process any command line arguments 
    window = MainWindow() #default behaviour is to hide  #window will be a parent parent widget
    window.show()
    sys.exit(app.exec_())

if __name__  == "__main__":
    main()
