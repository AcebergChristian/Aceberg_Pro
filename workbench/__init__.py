import random
import sys
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from charts.barchart import Barchart
from charts.linechart import Linechart
from charts.indicator import Indicator
 
class Workbench(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout_QV_group = QGroupBox()
        self.layout_QH = QGridLayout()

        
        self.layout_QH.addWidget(Indicator(0).layout_group,0,0,1,2) 
        self.layout_QH.addWidget(Indicator(1).layout_group,0,2,1,2)
        self.layout_QH.addWidget(Indicator(2).layout_group,0,4,1,2) 
        self.layout_QH.addWidget(Indicator(3).layout_group,0,6,1,2)
        
        self.layout_QH.addWidget(Barchart().layout_group,1,0,1,4)
        self.layout_QH.addWidget(Linechart().layout_group,1,4,1,4)
        
        
        self.layout_QV_group.setLayout(self.layout_QH)