import random
import sys
import json
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import management.data as static

class Management(QWidget):
    def __init__(self):
        super().__init__()

        self.layout_QV_group = QGroupBox()
        self.layout_QV = QVBoxLayout()

        self.layout_QV_group.setLayout(self.layout_QV)

        
        self.createfilter(static.data["columndata"])
        self.createtable(static.data)
        self.createtabledata(static.data)
    
    def createfilter(self, arg):

        # 右侧 筛选条件
        self.filter_group = QGroupBox("")
        self.filter_group.setStyleSheet(
            "background-color:rgb(54,64,95);border-radius:4px;color:#ffffff")
        self.filter_group.setFixedHeight(150)

        self.filter_layoutQV = QVBoxLayout()
        
        self.filter_scroll_QH = QHBoxLayout()
        self.filter_scroll_QH.setSpacing(30)
        
        self.filter_scroll = QScrollArea()
        self.filter_scroll_frame = QFrame()
      
        self.btn_layoutQH = QHBoxLayout()
        
        self.filter_scroll_QH.addLayout(self.creategrid(arg))
        self.filter_scroll_frame.setLayout(self.filter_scroll_QH)
        self.filter_scroll.setWidget(self.filter_scroll_frame)
        self.filter_layoutQV.addWidget(self.filter_scroll)
        
        self.filter_confirm = filterbtn("查询")
        self.filter_reset = filterbtn("重置")
        self.btn_layoutQH.addWidget(self.filter_confirm)
        self.btn_layoutQH.addWidget(self.filter_reset)
        self.btn_layoutQH.setContentsMargins(0,10,0,0)

        
        self.filter_layoutQV.addLayout(self.btn_layoutQH)
        self.filter_group.setLayout(self.filter_layoutQV)
        
        self.layout_QV.addWidget(self.filter_group)
        
    def creategrid(self,arg):
        widgets_pic_len  = len(arg)
        layout_grid = QGridLayout()
        for i in range(0, widgets_pic_len, 3):
            for j in range(i, min(i + 3, widgets_pic_len)):
                layout_grid.addLayout(self.createfiled(arg[j]),int(i/3),j%3,1,1)
            
        return layout_grid
        
    def createfiled(self, arg):
        filter_layoutForm = QFormLayout()

        QLine = QLineEdit()
        QLine.setFixedSize(150, 22)
        QLine.setStyleSheet("background:#ffffff;color:#333333")
        filter_layoutForm.addRow(arg, QLine)

        return filter_layoutForm

    #表格主体
    def createtable(self,arg):
        self.contenttable_group = QGroupBox()
        self.contenttable_group.setStyleSheet("background-color:rgb(54,64,95);border-radius:4px;color:#ffffff")
        self.contenttable_layout = QVBoxLayout()
        self.tableWidget = QTableWidget(10, len(arg["columndata"])+2)

        self.tableWidget.setStyleSheet(
            "QTableWidget::item { color:#e1e1e1;font-size:8px;border:0px solid rgba(255,255,11,0.4)}  QTableView::item:selected { background-color: rgb(81,93,128); color: white; }")
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section { color:#ffffff;font-weight:500;font-size:12px; }")
        self.tableWidget.verticalHeader().setStyleSheet(
            "QHeaderView::section { color:#ffffff;font-weight:500;font-size:12px; }")
        self.tableWidget.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical { border: none; background: rgb(86,100,154); width: 10px; margin: 1px 0 1px 0; } QScrollBar::handle:vertical { border-radius:4px;background: rgb(48,55,100); min-height: 20px; } QScrollBar::sub-line:vertical {background: rgba(0,0,0,0);} QScrollBar::add-line:vertical { background: rgba(0,0,0,0);}")
        self.tableWidget.horizontalScrollBar().setStyleSheet(
            "QScrollBar:horizontal { border: none; background: rgb(86,100,154); height: 10px; margin: 0 1px 0 1px; } QScrollBar::handle:horizontal { border-radius:4px;background: rgb(48,55,100); min-width: 20px; } QScrollBar::sub-line:horizontal {background: rgba(0,0,0,0);} QScrollBar::add-line:horizontal { background: rgba(0,0,0,0);}")
        self.tableWidget.setHorizontalHeaderLabels(arg["columndata"])

        self.contenttable_layout.addWidget(self.tableWidget)
        self.contenttable_group.setLayout(self.contenttable_layout)
        self.layout_QV.addWidget(self.contenttable_group)
    
    def createtabledata(self,arg):
        for i,items in enumerate(arg["tabeldata"]):
            for j,item in enumerate(items):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))     

        
# 搜索和btnBar 的按钮的类
class filterbtn(QPushButton):
    def __init__(self, arg):
        super().__init__()

        self.setText(arg)
        self.setFixedSize(52, 26)
        self.setStyleSheet(
            "background-color:rgb(86,100,154);color:#ffffff;border-radius:2px;")

    def enterEvent(self, event):
        self.setStyleSheet(
            "background-color:rgba(86,100,154,0.6);color:#ffffff;border-radius:2px;")

    def leaveEvent(self, event):
        self.setStyleSheet(
            "background-color:rgba(86,100,154,1);color:#ffffff;border-radius:2px;")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pass