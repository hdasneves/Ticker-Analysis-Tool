from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6 import QtCharts
from PySide6.QtCore import Qt
import fun
import sys
from yahoo import Ui_MainWindow

fun.remake_file()

class analyse(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(analyse, self).__init__()
        self.setupUi(self)

        self.bouton_confirm.clicked.connect(self.confirmation_ticker) 

    def confirmation_ticker(self):
        infos = fun.obtenir_infos(self.ticker.text(), self.depart.text(), self.fin.text()) 

        self.linegraph_one_ticker(data = infos["data"]) 

        self.rendement.setText(str(infos["rendement"])+"%")
        self.vol.setText(str(infos["volatilite"])+"%")

    def linegraph_one_ticker(self, data):
        chart = QtCharts.QChart()
        chart.setTitle(f"Evolution du cours de {self.ticker.text()} entre le {self.depart.text()} et le {self.fin.text()}")
        series_data = QtCharts.QLineSeries()
        series_data.setName("Close Value")

        for i in range(len(data)):
            series_data.append(i, data["Close"].iloc[i])
        chart.addSeries(series_data)

        axis_x = QtCharts.QValueAxis()
        axis_x.setRange(1, len(data))
        axis_x.setTitleText("Date (in days from start date)")
        axis_x.setTickCount(10)
        chart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis() 
        axis_y.setRange(min(data["Close"]) - 10, max(data["Close"]) + 10)
        axis_y.setTitleText("Close Value")
        chart.addAxis(axis_y, Qt.AlignLeft)

        series_data.attachAxis(axis_x)
        series_data.attachAxis(axis_y)

        self.graph.setChart(chart)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = analyse()
    window.show()
    app.exec_()