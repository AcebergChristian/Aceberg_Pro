import random
import sys
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    
    window = MainWindow()

    window.resize(1060,680)
    window.show()
    
    
    sys.exit(app.exec())