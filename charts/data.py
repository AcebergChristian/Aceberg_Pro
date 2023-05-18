
#指标图数据
indicator_data = {
        "indicator": {
            "data": [
                {"yesterdaycn_title": "产能",
                "yesterdaycn_val": "188.88",
                "yesterdaycn_rate": "+ 120.18%",
                "iconcolor": "background:rgb(66,70,126)"},
                {"yesterdaycn_title": "产能达成率",
                "yesterdaycn_val": "105.78%",
                "yesterdaycn_rate": "+ 110%",
                "iconcolor": "background:rgb(253,67,116)"},
                {"yesterdaycn_title": "正常任务占比",
                "yesterdaycn_val": "67.48%",
                "yesterdaycn_rate": "- 20.68%",
                "iconcolor": "background:rgb(59,213,149)"},
                {"yesterdaycn_title": "正常工时占比",
                "yesterdaycn_val": "92.26%",
                "yesterdaycn_rate": "+ 180.07%",
                "iconcolor": "background:rgb(246,109,98)"}
        ]
        }
}

#柱状图数据
barchart_data = {
        "barchart": {
            "axis_x": ["工序1","工序2","工序3","工序4"],
            "val": [80.8,46.3,123,78.3]
        }
}


#折线图数据
linechart_data = {
        "linechart": {
            "legend":[ ["cj1","#4c81ff"],["cj2","#f94a47"],["cj3","#21ce6b"] ],
            "axis_x": ["04/10","04/11","04/12","04/13","04/14","04/15","04/16"],
            "cj1": [80.8,46.3,123,78.3,71.8,46.3,138.9],
            "cj2": [60.8,66.3,73,67.6,79.8,98.3,98.9],
            "cj3": [46.8,122.3,78,79.3,46.8,138.3,80.9]
        }
}
