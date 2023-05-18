import random
import sys
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
 
 
class Bottombar(QWidget):
    def __init__(self):
        super().__init__()
        
        
        #顶部导航栏
        self.bottombar_group = QGroupBox("")
        self.bottombar_group.setFixedHeight(50)
        self.bottombar_group.setStyleSheet("background-color:rgb(54,64,95);border-radius:4px;")
        self.bottombar_layout = QHBoxLayout()


        #导航栏标签
        self.bottombardesc = bottombardesc("By Aceberg(Wangjiahao)")
        self.bottombar_layout.addWidget(self.bottombardesc)
        self.bottombar_layout.addStretch()

        #导航栏右侧用户设置
        self.bottombarversion = bottombardesc("Version 1.0.0")
        self.bottombar_layout.addWidget(self.bottombarversion)
        
        
        self.bottombar_group.setLayout(self.bottombar_layout)


class bottombardesc(QLabel):
    def __init__(self,arg):
        super().__init__()
        self.setText(arg)
        self.setStyleSheet("color:rgb(255,255,255);")