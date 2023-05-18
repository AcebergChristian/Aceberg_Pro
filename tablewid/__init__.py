import random
import sys
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import tablewid.data as static

class Tablewid(QWidget):
    def __init__(self):
        super().__init__()

        # 堆叠布局之表格主体
        # 右侧filter，buttonbar，table 在righttable_layout 布局里
        self.tablewid_group = QGroupBox()
        self.tablewid_layout = QVBoxLayout()
        # 导入的筛选条件
        self.filter_group = Filter()
        self.tablewid_layout.addWidget(self.filter_group.filter_group)
        # 导入的表格按钮栏
        self.tablebtn_group = Tablebtnbar()
        self.tablewid_layout.addWidget(self.tablebtn_group.tablebtn_group)
        # 导入的表格
        self.contenttable_group = Contenttable()
        self.tablewid_layout.addWidget(
            self.contenttable_group.contenttable_group)

        self.tablewid_group.setLayout(self.tablewid_layout)


class Filter(QWidget):
    def __init__(self):
        super().__init__()

        self.columndata = static.data["tablewid"]["columndata"]
        
        self.filter_group = QGroupBox()
        self.filter_group.setStyleSheet(
            "background-color:rgb(54,64,95);border-radius:4px;color:#ffffff")
        self.filter_group.setFixedHeight(120)
        
        self.filter_layoutQH = QHBoxLayout()
        
        self.filter_group.setLayout(self.filter_layoutQH)

        # 初始化组件
        self.creategrid(self.columndata)
        
        self.filter_layoutQH.setSpacing(30)
        
        self.filter_confirm = filterbtn("查询")
        self.filter_reset = filterbtn("重置")
        self.filter_layoutQH.addWidget(self.filter_confirm)
        self.filter_layoutQH.addWidget(self.filter_reset)

    def creategrid(self,arg):
        widgets_pic_len  = len(arg)
        layout_grid = QGridLayout()
        for i in range(0, widgets_pic_len, 3):
            for j in range(i, min(i + 3, widgets_pic_len)):
                layout_grid.addLayout(self.createfiled(arg[j]),int(i/3),j%3,1,1)
                print(arg[j])
            
        self.filter_layoutQH.addLayout(layout_grid)
        
        
        
    def createfiled(self, arg):
        filter_layoutForm = QFormLayout()

        QLine = QLineEdit()
        QLine.setFixedSize(150, 22)
        QLine.setStyleSheet("background:#ffffff;color:#333333")
        filter_layoutForm.addRow(arg, QLine)

        return filter_layoutForm


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


class Tablebtnbar(QWidget):
    def __init__(self):
        super().__init__()

        # 右侧 按钮bar
        self.tablebtn_group = QGroupBox("")
        self.tablebtn_group.setStyleSheet(
            "background-color:rgb(54,64,95);border-radius:4px;color:#ffffff")
        self.tablebtn_group.setFixedHeight(52)

        self.tablebtn_layout = QHBoxLayout()

        self.tablebtn_addone = filterbtn("新增")
        self.tablebtn_putout = filterbtn("导出")
        self.tablebtn_update = filterbtn("刷新")

        self.tablebtn_layout.addWidget(self.tablebtn_addone)
        self.tablebtn_layout.addWidget(self.tablebtn_putout)
        self.tablebtn_layout.addWidget(self.tablebtn_update)
        self.tablebtn_layout.addStretch()

        self.tablebtn_group.setLayout(self.tablebtn_layout)


class Contenttable(QWidget):
    def __init__(self):
        super().__init__()

        self.contenttable_group = QGroupBox("")
        self.contenttable_group.setStyleSheet(
            "background:rgb(54,64,95);border-radius:4px;")
        self.contenttable_group.setFixedHeight(320)
        self.contenttable_layout = QVBoxLayout()

        self.contenttable_group.setLayout(self.contenttable_layout)

        # 列
        self.columndata = static.data["tablewid"]["columndata"]
        
        # 假数据
        self.fakedata = static.data["tablewid"]["fakedata"]
        
        
        self.createtable()
        self.createdata(self.circulpagedata(1))

        self.createtablepagebar()

        self.update()

    def createtable(self):
        self.tableWidget = QTableWidget(10, 8)

        self.tableWidget.setStyleSheet(
            "QTableWidget::item { color:#e1e1e1;font-size:8px;border:0px solid rgba(255,255,11,0.4)}  QTableView::item:selected { background-color: rgb(81,93,128); color: white; }")
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section { color:#ffffff;font-weight:500;font-size:12px; }")
        self.tableWidget.verticalHeader().setStyleSheet(
            "QHeaderView::section { color:#ffffff;font-weight:500;font-size:12px; }")
        self.tableWidget.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical { border: none; background: rgb(86,100,154); width: 10px; margin: 1px 0 1px 0; } QScrollBar::handle:vertical { border-radius:4px;background: rgb(48,55,100); min-height: 20px; } QScrollBar::sub-line:vertical {background: rgba(0,0,0,0);} QScrollBar::add-line:vertical { background: rgba(0,0,0,0);}")

        self.tableWidget.setHorizontalHeaderLabels(self.columndata)

        self.contenttable_layout.addWidget(self.tableWidget)

    def createdata(self, arg):
        for index, item in enumerate(arg):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(item["id"]))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(item["name"]))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(item["age"]))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(item["class"]))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(item["loc"]))


    # 动态生成槽函数
    def btnclickfunc_decorator(self, index):
        def btnclickfunc():
            self.createdata(self.circulpagedata(index))
        return btnclickfunc

    def createtablepagebar(self):

        datalen = int(len(self.fakedata) / 10)
        self.pagebar = QHBoxLayout()

        firstpbtn = pagebtn("首页")
        self.btnclick_funcnfir = self.btnclickfunc_decorator(1)
        firstpbtn.clicked.connect(self.btnclick_funcnfir)

        lastpbtn = pagebtn("尾页")
        self.btnclick_funcnlst = self.btnclickfunc_decorator(datalen)
        lastpbtn.clicked.connect(self.btnclick_funcnlst)

        if datalen <= 5:
            self.pagebar.addStretch()
            self.pagebar.addWidget(firstpbtn)

            # 生成字典
            for i in range(1, datalen+1):
                button = pagebtn(f'{i}')
                self.btnclick_func = self.btnclickfunc_decorator(i)
                button.clicked.connect(self.btnclick_func)

                self.pagebar.addWidget(button)
            self.pagebar.addWidget(lastpbtn)

        else:
            pbtn1 = pagebtn("1")
            self.btnclick_func1 = self.btnclickfunc_decorator(1)
            pbtn1.clicked.connect(self.btnclick_func1)

            pbtn2 = pagebtn("2")
            self.btnclick_func2 = self.btnclickfunc_decorator(2)
            pbtn2.clicked.connect(self.btnclick_func2)

            pbtn3 = pagebtn("3")
            self.btnclick_func3 = self.btnclickfunc_decorator(3)
            pbtn3.clicked.connect(self.btnclick_func3)

            shenglue = QLabel("...")
            shenglue.setStyleSheet("color:#ffffff")

            pbtnn = pagebtn(str(datalen))
            self.btnclick_funcn = self.btnclickfunc_decorator(datalen)
            pbtnn.clicked.connect(self.btnclick_funcn)

            self.pagebar.addStretch()
            self.pagebar.addWidget(firstpbtn)
            self.pagebar.addWidget(pbtn1)
            self.pagebar.addWidget(pbtn2)
            self.pagebar.addWidget(pbtn3)
            self.pagebar.addWidget(shenglue)
            self.pagebar.addWidget(pbtnn)
            self.pagebar.addWidget(lastpbtn)

        self.contenttable_layout.addLayout(self.pagebar)

    # 根据点击的数字，展示某一页数据
    def circulpagedata(self, arg):
        res = []
        for index, item in enumerate(self.fakedata):
            if 10*arg-10 < index <= 10*arg:
                res.append(item)
        return res


# 分页按钮的类
class pagebtn(QPushButton):
    def __init__(self, arg):
        super().__init__()

        self.setText(arg)
        self.setFixedSize(26, 26)
        self.setStyleSheet(
            "font-size:10px;background-color:rgb(86,100,154);color:#ffffff;border-radius:2px;")

    def enterEvent(self, event):
        self.setStyleSheet(
            "font-size:10px;background-color:rgba(86,100,154,0.6);color:#ffffff;border-radius:2px;")

    def leaveEvent(self, event):
        self.setStyleSheet(
            "font-size:10px;background-color:rgba(86,100,154,1);color:#ffffff;border-radius:2px;")

