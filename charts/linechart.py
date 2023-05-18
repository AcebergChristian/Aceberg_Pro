import enum
import random
import sys
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtCharts import *
import charts.data as static
 

class Linechart(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout_group = QGroupBox()
        self.layout_QH = QHBoxLayout()
        self.layout_QH.setContentsMargins(0,0,0,0)

        self.create_line()
        
    def createaxis_x(self):
        axis_xarr = []
        for item in static.linechart_data["linechart"]["axis_x"]:
            axis_xarr.append(item)

        # 创建坐标轴
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(axis_xarr)
        self.axis_x.setTitleText("日期")
        axis_x_font = QFont()
        axis_x_font.setPointSize(8)
        self.axis_x.setLabelsFont(axis_x_font)
        
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
    
    def createaxis_y(self):
        axis_yarr1 = []
        for item in static.linechart_data["linechart"]["cj1"]:
            axis_yarr1.append(item)
        
        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, max(axis_yarr1)+30  )
        self.axis_y.setTitleText("Y Axis")
        axis_y_font = QFont()
        axis_y_font.setPointSize(10)
        self.axis_y.setLabelsFont(axis_y_font)
        
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        

    def create_line(self):
        self.chart = QChart()
        self.legend = self.chart.legend()
        
        # 创建X坐标轴
        self.createaxis_x()
        # 创建Y坐标轴
        self.createaxis_y()

        
        series_arr = static.linechart_data["linechart"]["legend"]
        for item in series_arr:
            series_cj = QLineSeries()
            series_cj_scatter = QScatterSeries()
            series_cj_scatter.setMarkerSize(5)
            series_cj.setName(item[0])
        
            for index,val in enumerate(static.linechart_data["linechart"][item[0]]):
                series_cj.append(index, val)
                series_cj_scatter.append(index, val)
            
            self.chart.addSeries(series_cj)
            self.chart.addSeries(series_cj_scatter)

            series_cj.attachAxis(self.axis_x)
            series_cj_scatter.attachAxis(self.axis_x)
            
            series_cj.attachAxis(self.axis_y)
            series_cj_scatter.attachAxis(self.axis_y)

            # 设置线条颜色和宽度
            pen = QPen()
            pen.setWidth(2)
            series_cj.setPen(QColor(item[1]))
            
        # 将散点系列从图例中移除
        markers = self.legend.markers()
        for marker in markers:
            #判断每一个图例是否属于QScatterSeries类
            if isinstance(marker.series(), QScatterSeries):
                marker.setVisible(False)

        
        
        # 创建视图和场景
        self.view = QChartView(self.chart)

        # 设置图表标题
        self.chart.setTitle("7日数据图")
        
        # 将折线图添加到图表展示窗口中
        self.chartView = QChartView(self.chart)
        self.chartView.setStyleSheet("background:rgb(53,64,95);padding:0,0,0,0;")
        
        self.layout_QH.addWidget(self.chartView)
        self.layout_group.setLayout(self.layout_QH)