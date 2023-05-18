from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtCharts import *
import charts.data as static

class Indicator(QWidget):
    def __init__(self, arg):
        super().__init__()

        self.arg = arg

        # 不同数据
        self.data = static.indicator_data["indicator"]["data"]

        self.layout_group = QGroupBox()
        self.layout_group.setStyleSheet(
            "background:rgb(54,64,95);border-radius:2px;")
        self.layout_group.setFixedHeight(60)
        self.layout_QH = QHBoxLayout()

        self.create_indexnum()

    # 生成图表
    def create_indexnum(self):

        #icon
        indicator_icon = QFrame()
        indicator_icon.setFixedSize(30, 30)
        indicator_icon.setStyleSheet(
            "background:url(charts/pic/indicator.svg) no-repeat center center;")
        indicator_icon_bg = QFrame()
        indicator_icon_bg_QH = QHBoxLayout()
        indicator_icon_bg.setFixedSize(30, 30)
        indicator_icon_bg.setStyleSheet(self.data[self.arg]["iconcolor"]+";border-radius:15px")
        indicator_icon_bg_QH.setContentsMargins(0, 0, 0, 0)
        indicator_icon_bg_QH.addWidget(indicator_icon)
        indicator_icon_bg.setLayout(indicator_icon_bg_QH)

        #标题和值
        indicator_label_QV = QVBoxLayout()
        indicator_label1 = QLabel(self.data[self.arg]["yesterdaycn_title"])
        indicator_label1.setStyleSheet("color:#ffffff;font-size:10px;")
        indicator_label2 = QLabel(self.data[self.arg]["yesterdaycn_val"])
        indicator_label2.setStyleSheet("color:#ffffff;font-size:14px;")
        indicator_label_QV.addWidget(indicator_label1)
        indicator_label_QV.addWidget(indicator_label2)

        #涨幅率
        indicator_updown_QV = QVBoxLayout()
        indicator_updown = QLabel(self.data[self.arg]["yesterdaycn_rate"])
        judgeupdown = lambda x:"color:rgb(50,167,139);font-size:10px;" if "+" in x else "color:rgb(243,65,69);font-size:10px;"
        indicator_updown.setStyleSheet( judgeupdown(self.data[self.arg]["yesterdaycn_rate"]) )
        indicator_updown_QV.addWidget(indicator_updown)
        indicator_updown_QV.addStretch()

        #以上三个组件放到布局里
        self.layout_QH.addWidget(indicator_icon_bg)
        self.layout_QH.addLayout(indicator_label_QV)
        self.layout_QH.addLayout(indicator_updown_QV)

        self.layout_group.setLayout(self.layout_QH)

