# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.classeur = QTableView(self.centralwidget)
        self.classeur.setObjectName(u"classeur")

        self.verticalLayout.addWidget(self.classeur)

        self.ajout_colonne = QPushButton(self.centralwidget)
        self.ajout_colonne.setObjectName(u"ajout_colonne")

        self.verticalLayout.addWidget(self.ajout_colonne)

        self.suppr = QPushButton(self.centralwidget)
        self.suppr.setObjectName(u"suppr")

        self.verticalLayout.addWidget(self.suppr)

        self.sauv = QPushButton(self.centralwidget)
        self.sauv.setObjectName(u"sauv")

        self.verticalLayout.addWidget(self.sauv)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ajout_colonne.setText(QCoreApplication.translate("MainWindow", u"Ajouter colonne", None))
        self.suppr.setText(QCoreApplication.translate("MainWindow", u"Supprimer colonne", None))
        self.sauv.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder les donn\u00e9es", None))
    # retranslateUi

