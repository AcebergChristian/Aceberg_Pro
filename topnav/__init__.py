import random
import sys
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import topnav.data as static
 
class Topnav(QWidget):
    def __init__(self):
        super().__init__()
        
        
        #顶部导航栏
        self.topnav_group = Movegroupbox()     
        self.topnav_group.setStyleSheet("background-color:{};border-radius:4px;".format(static.data["topnav"]["bg"]))
        #self.topnav_group.setFixedWidth(900)
        self.topnav_group.setFixedHeight(52)
        self.topnav_layout = QHBoxLayout()


        #导航栏标签
        self.currentpagelabel = QLabel(static.data["currentpagelabel"]["label"])
        self.currentpagelabel.setContentsMargins(40,0,0,0)
        self.currentpagelabel.setStyleSheet("color:{};background-color:rgba(48,55,100,0);".format(static.data["currentpagelabel"]["color"]))
        self.topnav_layout.addWidget(self.currentpagelabel)
        self.topnav_layout.addStretch()
        
        
        #导航栏右侧 最小化
        self.topnav_tomin = miniQlabel("_")
        self.topnav_layout.addWidget(self.topnav_tomin)
        
        #导航栏右侧 全屏
        self.topnav_fullscreen = fullWinQlabel("❒")
        self.topnav_layout.addWidget(self.topnav_fullscreen)
        
        #导航栏右侧 关闭窗口
        self.topnav_close = closeQlabel("✕")
        self.topnav_layout.addWidget(self.topnav_close)
        
        
        self.topnav_group.setLayout(self.topnav_layout)
            
        
    #接受leftmenu发出的信号方法
    @Slot(dict)
    def getlabel(self, msg):
        self.currentpagelabel.setText( msg["label"] )

 
class miniQlabel(QLabel):
    def __init__(self,arg):
        super().__init__()
        self.setText(arg)
        self.setStyleSheet("color:#ffffff;font-size:14px")
        self.setFixedSize(static.data["to_btn"]["width"],static.data["to_btn"]["height"])
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def enterEvent(self, event):
        self.setStyleSheet("font-size:14px;color:#ffffff;background-color: {};border-radius:4px;".format(static.data["to_btn"]["focusbackground"]))
    
    def leaveEvent(self, event):
        self.setStyleSheet("font-size:14px;color:#ffffff;background-color: {};border-radius:4px;".format(static.data["to_btn"]["nobackground"]))
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent().parent().showMinimized()


class fullWinQlabel(QLabel):
    def __init__(self,arg):
        super().__init__()
        self.setText(arg)
        self.setStyleSheet("color:#ffffff;font-size:14px")
        self.setFixedSize(static.data["to_btn"]["width"],static.data["to_btn"]["height"])
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        #判断当前是全屏还是一般状态
        self.flag = False

    def enterEvent(self, event):
        self.setStyleSheet("font-size:14px;color:#ffffff;background-color: {};border-radius:4px;".format(static.data["to_btn"]["focusbackground"]))
    
    def leaveEvent(self, event):
        self.setStyleSheet("font-size:14px;color:#ffffff;background-color: {};border-radius:4px;".format(static.data["to_btn"]["nobackground"]))
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.flag == False:
                self.flag = True
                self.parent().parent().setWindowState(Qt.WindowFullScreen)
            else:
                self.flag = False
                self.parent().parent().setWindowState(Qt.WindowNoState)

class closeQlabel(QLabel):
    def __init__(self,arg):
        super().__init__()
        self.setText(arg)
        self.setStyleSheet("color:#ffffff;font-size:14px")
        self.setFixedSize(static.data["to_btn"]["width"],static.data["to_btn"]["height"])
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def enterEvent(self, event):
        self.setStyleSheet("font-size:14px;color:#ffffff;background-color: {};border-radius:4px;".format(static.data["to_btn"]["focusbackground"]))
    
    def leaveEvent(self, event):
        self.setStyleSheet("font-size:14px;color:#ffffff;background-color: {};border-radius:4px;".format(static.data["to_btn"]["nobackground"]))
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent().parent().close()
            

#重写navtop 里的Qgroupbox 实现拖拽移动窗口
class Movegroupbox(QGroupBox):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pressflag = False
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressflag = True
            self.Window = self.parent()
            self.mouse_start = self.mapToGlobal(event.pos())
            self.window_start = self.parent().pos()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressflag = False
    
    def mouseMoveEvent(self, event):
        if self.pressflag == True:
            distance = self.mapToGlobal(event.pos()) - self.mouse_start
            new_position = self.window_start + distance
            self.parent().move(new_position)