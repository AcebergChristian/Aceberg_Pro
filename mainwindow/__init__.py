import random
import sys
from PySide6.QtWidgets import *
from PySide6 import *
from PySide6.QtCore import *
from leftmenu import Leftmenu
from rightcontent import Rightcontent
import mainwindow.data as static


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        

        self.setWindowTitle(static.data["mainwindow"]["TITLE"])
        self.setMinimumSize(748,480)
        #样式
        self.setStyleSheet("background:{};border-radius:10px;".format(static.data["mainwindow"]["bg"]))
        #无边框
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        
        #设置变量  实例化 菜单和右侧内容
        self.getleftmenu = Leftmenu()
        self.getright = Rightcontent()
        
        #初始化组件 布局
        self.initmainwindow()
        
        #连接改变navtop的label的信号
        self.connect_leftmenu_navtop_label_signal()


    def initmainwindow(self):
        #主布局的bg Qframe
        self.main_bgQH = QHBoxLayout()
        self.main_bg = QFrame()
        self.main_bg.setStyleSheet("background:red")
        
        #主布局,把import进来的每个组件或布局的group放进来，再放到QMainWindow的中心控件
        self.main_layout = QHBoxLayout()
        #添加左侧菜单栏
        self.main_layout.addWidget(self.getleftmenu.leftmenu_group)
        #添加右侧布局
        self.main_layout.addLayout(self.getright.rightcontent_layout)
        self.main_layout.setContentsMargins(5,5,5,5)

        
        self.setLayout(self.main_layout)
        

    #执行leftmenu的信号方法点击不同的menu 发送数据
    def connect_leftmenu_navtop_label_signal(self):
        self.getleftmenu.tomsg.connect(self.getright.topnav_group.getlabel)
        self.getleftmenu.tomsg.connect(self.getright.getmenuindex)
        
