import random
import sys
from turtle import left
from PySide6.QtWidgets import *
from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import leftmenu.data as static


class Leftmenu(QWidget):
    
    #改变topnav 的label
    tomsg = Signal(dict)
    
    def __init__(self):
        super().__init__()

        self.menudata = [{
            "name": "工作台",
            "type":"workbench"
        }, {
            "name": "数据管理",
            "type":"datamana"
        }, {
            "name": "组件预览",
            "type":"widgetview"
        }, {
            "name": "后台管理",
            "type":"management"
        }]

        # 初始化组件
        self.flag = True
        self.initleftmenu()
        
    # 初始化左侧菜单
    def initleftmenu(self):
        
        self.leftmenu_group = QGroupBox()
        self.leftmenu_group.setStyleSheet("background-color:{};border-radius:4px;".format(static.data["leftmenu"]["bg"]))
        self.leftmenu_group.setFixedWidth(static.data["leftmenu"]["width"])
        self.leftmenu_QVlayout = QVBoxLayout()

        self.initmenu()

    # 初始化渲染动态list菜单栏
    def initmenu(self):
        
        self.menus_QVlayout = QVBoxLayout()
        
        logo_QHlayout = QHBoxLayout()
        self.leftmenu_menu_logo = QFrame()
        self.leftmenu_menu_logo.setFixedSize(static.data["leftmenu_menu_logo"]["width"],static.data["leftmenu_menu_logo"]["height"])
        self.leftmenu_menu_logo.setStyleSheet("background:url({}) no-repeat center center;".format(static.data["leftmenu_menu_logo"]["picpath"]))
        logo_QHlayout.addWidget(self.leftmenu_menu_logo)
        self.leftmenu_QVlayout.addLayout(logo_QHlayout)
        
        
        for index, item in enumerate(self.menudata):
            self.leftmenu_menu_bg = menuframe()
            self.leftmenu_menu_bg.mousePressEvent = lambda event, index=index: self.clicksetmenuframebg(event, index)
            self.leftmenu_menu_bg.setFixedSize(static.data["leftmenu_menu_bg"]["width"],static.data["leftmenu_menu_bg"]["height"])
            self.leftmenu_menu_bg.setContentsMargins(2, 0, 2, 0)
            self.leftmenu_menu_QH = QHBoxLayout()
            self.leftmenu_menu_icon = QFrame()
            self.leftmenu_menu_icon.setStyleSheet(
                "background:url({}) no-repeat center center;".format(static.data["leftmenu_menu_icon"][item["type"]]))
            self.leftmenu_menu_label = menuframelabel(item["name"])
            self.leftmenu_menu_label.setStyleSheet("color: #ffffff;".format(static.data["leftmenu_menu_label"]["color"]))
            self.leftmenu_menu_label.mousePressEvent = lambda event, index=index: self.clicksetmenuframebg(event, index)

            self.leftmenu_menu_QH.addWidget(self.leftmenu_menu_icon)
            self.leftmenu_menu_QH.addWidget(self.leftmenu_menu_label)
            self.leftmenu_menu_bg.setLayout(self.leftmenu_menu_QH)
            
            self.menus_QVlayout.addWidget(self.leftmenu_menu_bg)

        self.menus_QVlayout.setSpacing(20)
        
        self.leftmenu_QVlayout.setContentsMargins(0, 20, 0, 0)
        
        #使之水平居中的布局
        menus_QHlayout = QHBoxLayout()
        menus_QHlayout.addLayout(self.menus_QVlayout)
        self.leftmenu_QVlayout.addLayout(menus_QHlayout)
        self.leftmenu_QVlayout.addStretch()
        
        # 判断leftmenu 收起还是展开button
        self.setleftmenu_group_width_btn = QLabel(static.data["setleftmenu_group_width_btn"]["closetext"])
        self.setleftmenu_group_width_btn.setAlignment(Qt.AlignCenter)
        self.setleftmenu_group_width_btn.setStyleSheet(
            "background-color: transparent;color:{};font-size:{}; ".format(static.data["setleftmenu_group_width_btn"]["color"],static.data["setleftmenu_group_width_btn"]["font"]))
        self.setleftmenu_group_width_btn.mousePressEvent = self.toggleleftmenu_width
        self.leftmenu_QVlayout.addWidget(self.setleftmenu_group_width_btn)
        
        self.leftmenu_group.setLayout(self.leftmenu_QVlayout)


    # 点击展开收起 重新渲染菜单栏
    def clickchangemenu(self):
        if self.flag == True:
            
            #改变logo
            self.leftmenu_menu_logo.setStyleSheet("background:url({}) no-repeat center center;".format(static.data["leftmenu_menu_logo"]["picpathm"]))
            self.leftmenu_menu_logo.setFixedSize(56,56)
            self.leftmenu_menu_logo.setContentsMargins(0,0,0,30)
            
            for i in range(self.menus_QVlayout.count()):
                self.menus_QVlayout.itemAt(i).widget().setFixedSize(50,40)
                #self.menus_QVlayout.itemAt(i).widget().layout().itemAt(0).widget().setStyleSheet("background:url({}) no-repeat center center;".format(static.data["leftmenu_menu_icon"]["picpath"]))
                self.menus_QVlayout.itemAt(i).widget().findChildren(QLabel)[0].setVisible(False)

        elif self.flag == False:
            
            #改变logo
            self.leftmenu_menu_logo.setStyleSheet("background:url({}) no-repeat center center;".format(static.data["leftmenu_menu_logo"]["picpath"]))
            self.leftmenu_menu_logo.setFixedSize(160,60)
            
            for i in range(self.menus_QVlayout.count()):
                self.menus_QVlayout.itemAt(i).widget().setFixedSize(170,40)
                #self.menus_QVlayout.itemAt(i).widget().layout().itemAt(0).widget().setStyleSheet("background:url({}) no-repeat center center;".format(static.data["leftmenu_menu_icon"]["picpath"]))
                self.menus_QVlayout.itemAt(i).widget().findChildren(QLabel)[0].setVisible(True)

    #点击展开收起事件
    def toggleleftmenu_width(self, event):

        if event.button() == Qt.LeftButton:
            if self.flag == True:
                self.setleftmenu_group_width_btn.setText(static.data["setleftmenu_group_width_btn"]["opentext"])
                self.leftmenu_group.setFixedWidth(60)
                self.clickchangemenu()
                self.flag = False

            elif self.flag == False:
                self.setleftmenu_group_width_btn.setText(static.data["setleftmenu_group_width_btn"]["closetext"])
                self.leftmenu_group.setFixedWidth(200)
                self.clickchangemenu()
                self.flag = True

    #点击改变背景颜色
    def clicksetmenuframebg(self, event, index):
        for i in range(self.menus_QVlayout.count()):
            if i == index:
                self.menus_QVlayout.itemAt(i).widget().flag = True   
                self.menus_QVlayout.itemAt(i).widget().setStyleSheet("background-color: {};border-radius:4px;".format(static.data["leftmenu_menu_bg"]["focusbackground"])  )

                
                #更新label 方法
                dictdata = {"label":self.menus_QVlayout.itemAt(i).widget().layout().itemAt(1).widget().text(),"index":index}

                self.changelabel(dictdata)
                
                
            elif i != index:
                self.menus_QVlayout.itemAt(i).widget().flag = False
                self.menus_QVlayout.itemAt(i).widget().setStyleSheet("background-color:{}".format(static.data["leftmenu_menu_bg"]["nobackground"]))
                
    
    #更新label 方法
    def changelabel(self,arg):
        self.tomsg.emit(arg)


#改写frame方法 使其实例化leftmenu_bg， 鼠标滑过hover效果
class menuframe(QFrame):
     
    def __init__(self):
        super().__init__()
        self.flag = False
        self.setStyleSheet("background-color:rgba(54,64,95,0)")
                                                        
    def enterEvent(self, event):
        self.setStyleSheet("background-color: {};border-radius:4px;".format(static.data["leftmenu_menu_bg"]["focusbackground"]))

    def leaveEvent(self, event):
        if self.flag != True:
            self.setStyleSheet("background-color:{}".format(static.data["leftmenu_menu_bg"]["nobackground"]))


#改写frame方法 使其实例化leftmenu_label 点击改变文字
class menuframelabel(QLabel):
    def __init__(self,arg):
        super().__init__()
        self.setText(arg)
    
 