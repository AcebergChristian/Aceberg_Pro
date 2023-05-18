import random
import sys
import os
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

 
class Widgetview(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout_QV_group = QGroupBox()
        self.layout_QV = QVBoxLayout()
        
        self.layout_QV_group.setLayout(self.layout_QV)
        
        #创建布局
        self.creategrid(self.getwidgets())
        

    def creategrid(self,arg):
        widgets_pic_len  = len(arg)
        layout_grid = QGridLayout()
        for i in range(0, widgets_pic_len, 4):
            for j in range(i, min(i + 4, widgets_pic_len)):
                layout_grid.addWidget(self.createwid(arg[j]),int(i/4),j%4,1,1)
        self.layout_QV.addLayout(layout_grid)
        
    
    def getwidgets(self):
        widgets_pic_path = r"widgetview/widgets_pic"
        widgets_pics = os.listdir(widgets_pic_path)
        res = []
        for widgets_pic in widgets_pics:
            if "png" in widgets_pic:
                res.append("widgetview/widgets_pic/"+widgets_pic)
        return res
    

    def createwid(self,arg):
        widbg = QFrame()
        widbg.setStyleSheet("background:rgb(54,64,95);border-radius:4px;")
        widbg_QV = QVBoxLayout()
        wid_pic = QLabel()
        pic = QImage(arg)
        pixmap = QPixmap.fromImage(pic)
        scaled_image = pixmap.scaled(pixmap.width()*0.1, pixmap.height()*0.1, Qt.KeepAspectRatio)
        wid_pic.setPixmap(scaled_image)
        #wid_pic.setAlignment(Qt.AlignCenter)
        wid_desc = QLabel(arg.split("/")[2])
        wid_desc.setAlignment(Qt.AlignCenter)
        wid_desc.setStyleSheet("color:#ffffff;")
        widbg_QV.addWidget(wid_pic)
        widbg_QV.addWidget(wid_desc)
        widbg.setLayout(widbg_QV)
        
        return widbg
