from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QHeaderView, QInputDialog, QFileDialog
from PySide6 import QtCharts
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
import sys
from table import Ui_MainWindow
import pandas as pd
import subprocess

class afficheur(QMainWindow, Ui_MainWindow):
    def __init__(self, text_1, data_1, text_2 = None, data_2 = None):
        super(afficheur, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Editeur de données")

        if data_2 is not None :
            overall_data = pd.merge(left = data_1["data"], right = data_2["data"], on = "Date", suffixes = (f"_{text_1}", f"_{text_2}"))
        else :
            overall_data = data_1["data"]

        self.afficher_données(dataframe = overall_data)
        self.ajout_colonne.clicked.connect(self.nouvelle_colonne)
        self.suppr.clicked.connect(self.supprimer_colonne)
        self.sauv.clicked.connect(self.exporter_en_csv )

    def afficher_données(self, dataframe):
        self.model = QStandardItemModel(dataframe.shape[0], dataframe.shape[1], self)
        self.model.setHorizontalHeaderLabels(dataframe.columns.tolist())

        for row in range(dataframe.shape[0]):
            for col in range(dataframe.shape[1]):
                item = QStandardItem(str(dataframe.iat[row, col]))
                self.model.setItem(row, col, item)
        
        self.classeur.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.classeur.setModel(self.model)

    def nouvelle_colonne(self):
        nom_colonne, ok = QInputDialog.getText(self, "Ajouter une colonne", "Nom de la nouvelle colonne :")

        if ok :
            self.model.insertColumn(self.model.columnCount())
            self.model.setHorizontalHeaderItem(self.model.columnCount() - 1, QStandardItem(nom_colonne))

    def supprimer_colonne(self):
        noms_colonnes = [self.model.headerData(col, Qt.Horizontal, Qt.DisplayRole) for col in range(self.model.columnCount())]
        nom_colonne, ok = QInputDialog.getItem(self, "Supprimer une colonne", "Choisissez une colonne à supprimer :", noms_colonnes, editable = False)
        
        if ok :
            self.model.removeColumn(noms_colonnes.index(nom_colonne))
    
    def exporter_en_csv(self):
        options = QFileDialog.Options()
        chemin_fichier, _ = QFileDialog.getSaveFileName(self, "Exporter les données", "", "Fichiers CSV (*.csv);;Fichiers Excel (*.xlsx);;Tous les fichiers (*)", options = options)
        
        if not chemin_fichier:
            return
        
        model = self.classeur.model()
        data = [[model.data(model.index(row, col)) for col in range(model.columnCount())] for row in range(model.rowCount())]
        headers = [model.headerData(col, Qt.Horizontal, Qt.DisplayRole) for col in range(model.columnCount())]
        df = pd.DataFrame(data, columns=headers)

        if chemin_fichier.endswith(".xlsx"):
            df = df.to_excel(chemin_fichier, index = False)
        if chemin_fichier.endswith(".csv"):
            df = df.to_csv(chemin_fichier, index = False)

