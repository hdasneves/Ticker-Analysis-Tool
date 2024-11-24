from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6 import QtCharts
from PySide6.QtCore import Qt
import fun
import sys
import numpy as np

fun.remake_file()

from yahoo import Ui_MainWindow

class analyse(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(analyse, self).__init__()
        self.setupUi(self)
        self.bouton_confirm.clicked.connect(self.confirmation_ticker)
        self.bouton_confirm_comparaison.clicked.connect(self.confirmation_comparaison) 

    def confirmation_ticker(self):
        infos = fun.obtenir_infos(self.ticker.text(), self.depart.text(), self.fin.text()) 
        self.linegraph(self.ticker.text(), data_1 = infos["data"]) 
        self.retours.setCurrentIndex(1)
        self.label_rendement.setText("Rendement")
        self.rendement.setText(str(infos["rendement"])+"%")
        self.label_vol.setText("Volatilité (en %)")
        self.vol.setText(str(infos["volatilite"])+"%")

    def confirmation_comparaison(self):
        actif_a = fun.obtenir_infos(self.actif_a.text(), self.depart_comparaison.text(), self.fin_comparaison.text()) 
        actif_b = fun.obtenir_infos(self.actif_b.text(), self.depart_comparaison.text(), self.fin_comparaison.text()) 
        self.linegraph(self.actif_a.text(), actif_a["data"], self.actif_b.text(), actif_b["data"])

        self.label_r_a.setText(f"Rendement de {self.actif_a.text()}")
        self.r_a.setText(str(actif_a["rendement"])+"%")
        self.label_r_b.setText(f"Rendement de {self.actif_b.text()}")
        self.r_b.setText(str(actif_b["rendement"])+"%")

        self.label_v_a.setText(f"Volatilité de {self.actif_a.text()} (en %)")
        self.v_a.setText(str(actif_a["volatilite"])+"%")
        self.label_v_b.setText(f"Volatilité de {self.actif_b.text()} (en %)")
        self.v_b.setText(str(actif_b["volatilite"])+"%")

        self.label_diff_r.setText(f"Différence de rendement entre les deux")
        self.r_diff.setText(str(np.round(actif_a["rendement"] - actif_b["rendement"]))+"%")
        self.label_diff_v.setText(f"Différence de volatilité entre les deux")
        self.v_diff.setText(str(np.round(actif_a["volatilite"] - actif_b["volatilite"], 2))+"%")

        self.retours.setCurrentIndex(0)

    def linegraph(self, text_1, data_1, text_2 = None, data_2 = None):
        chart = QtCharts.QChart()
        if data_2 is not None:
            chart.setTitle(f"Comparaison de l'évolution du cours de {self.actif_a.text()} et de {self.actif_b.text()} entre le {self.depart_comparaison.text()} et le {self.fin_comparaison.text()} en base log")
        else : 
            chart.setTitle(f"Evolution du cours de {self.ticker.text()} entre le {self.depart.text()} et le {self.fin.text()}")

        series_data_1 = QtCharts.QLineSeries()
        series_data_1.setName(text_1)

        if data_2 is not None:
            series_data_2 = QtCharts.QLineSeries()
            series_data_2.setName(text_2)

            for i in range(len(data_2)):
                series_data_2.append(i, data_2["Close"].iloc[i])
            chart.addSeries(series_data_2)

        for i in range(len(data_1)):
            series_data_1.append(i, data_1["Close"].iloc[i])
        chart.addSeries(series_data_1)

        axis_x = QtCharts.QValueAxis()
        axis_x.setRange(0, len(data_1) - 1)
        axis_x.setTitleText("Date (in days from start date)")
        chart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis() 
        axis_y.setRange(min(data_1["Close"]), max(data_1["Close"]))
        axis_y.setTitleText(f"Close Value {self.actif_a.text()}")
        chart.addAxis(axis_y, Qt.AlignLeft)

        series_data_1.attachAxis(axis_x)
        series_data_1.attachAxis(axis_y)

        if data_2 is not None: 
            axis_z = QtCharts.QValueAxis()
            axis_z.setRange(min(data_2["Close"]), max(data_2["Close"]))
            axis_z.setTitleText(f"Close Value {self.actif_b.text()}")
            chart.addAxis(axis_z, Qt.AlignRight)
            series_data_2.attachAxis(axis_x)
            series_data_2.attachAxis(axis_z)

        self.graph.setChart(chart)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = analyse()
    window.show()
    app.exec_()