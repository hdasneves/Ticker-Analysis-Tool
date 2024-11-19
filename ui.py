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
        self.bouton_confirm.clicked.connect(self.confirmation) #Connection du bouton de validation à la fonction confirmation


    def confirmation(self):
        data = fun.import_données(self.ticker.text(), self.depart.text(), self.fin.text()) #Obtention des données basées sur l'input de l'utilisateur

        self.linegraph(data = data) #Ajout données au graphique

        rendement = fun.obtenir_rendement(donnees = data) #Obtention du rendement
        volatilite = fun.obtenir_volatilite(donnees = data)
        self.rendement.setText(str(rendement)+"%")
        self.vol.setText(str(volatilite)+"%")

    def linegraph(self, data):
        chart = QtCharts.QChart()
        series_data = QtCharts.QLineSeries()
        series_data.setName("Close Value")

        for i in range(len(data)):
            series_data.append(i, data["Close"][i])
        chart.addSeries(series_data)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(data["Date"])
        chart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(min(data["Close"]) - 10, max(data["Close"]) + 10)
        chart.addAxis(axis_y, Qt.AlignLeft)

        series_data.attachAxis(axis_x)
        series_data.attachAxis(axis_y)

        self.graph.setChart(chart)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = analyse()
    window.show()
    app.exec_()