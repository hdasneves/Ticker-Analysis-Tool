# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yahoo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1039, 764)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.en_tete = QWidget(self.widget)
        self.en_tete.setObjectName(u"en_tete")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.en_tete.sizePolicy().hasHeightForWidth())
        self.en_tete.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.en_tete)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_en_tete = QLabel(self.en_tete)
        self.label_en_tete.setObjectName(u"label_en_tete")

        self.horizontalLayout_2.addWidget(self.label_en_tete, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.en_tete)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_ticker = QLabel(self.widget_6)
        self.label_ticker.setObjectName(u"label_ticker")

        self.verticalLayout_2.addWidget(self.label_ticker, 0, Qt.AlignHCenter)

        self.ticker = QLineEdit(self.widget_6)
        self.ticker.setObjectName(u"ticker")

        self.verticalLayout_2.addWidget(self.ticker)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.line_3 = QFrame(self.widget_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(6)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_date = QLabel(self.widget_7)
        self.label_date.setObjectName(u"label_date")

        self.verticalLayout_3.addWidget(self.label_date, 0, Qt.AlignHCenter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.depart = QDateEdit(self.widget_7)
        self.depart.setObjectName(u"depart")
        self.depart.setDateTime(QDateTime(QDate(2019, 12, 26), QTime(0, 0, 0)))

        self.horizontalLayout_4.addWidget(self.depart)

        self.fin = QDateEdit(self.widget_7)
        self.fin.setObjectName(u"fin")
        self.fin.setDateTime(QDateTime(QDate(2020, 12, 26), QTime(0, 0, 0)))

        self.horizontalLayout_4.addWidget(self.fin)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.line_4 = QFrame(self.widget_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bouton_confirm = QPushButton(self.widget_8)
        self.bouton_confirm.setObjectName(u"bouton_confirm")

        self.horizontalLayout_6.addWidget(self.bouton_confirm, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.widget_4)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.partie_graph = QWidget(self.widget)
        self.partie_graph.setObjectName(u"partie_graph")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(8)
        sizePolicy3.setHeightForWidth(self.partie_graph.sizePolicy().hasHeightForWidth())
        self.partie_graph.setSizePolicy(sizePolicy3)
        self.horizontalLayout_7 = QHBoxLayout(self.partie_graph)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.graph = QChartView(self.partie_graph)
        self.graph.setObjectName(u"graph")

        self.horizontalLayout_7.addWidget(self.graph)


        self.verticalLayout.addWidget(self.partie_graph)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label = QLabel(self.widget_9)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)

        self.rendement = QLabel(self.widget_9)
        self.rendement.setObjectName(u"rendement")

        self.horizontalLayout_10.addWidget(self.rendement)


        self.horizontalLayout_8.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.vol = QLabel(self.widget_10)
        self.vol.setObjectName(u"vol")

        self.horizontalLayout_11.addWidget(self.vol)


        self.horizontalLayout_8.addWidget(self.widget_10)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_3 = QLabel(self.widget_11)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_13.addWidget(self.label_3)

        self.sharpe = QLabel(self.widget_11)
        self.sharpe.setObjectName(u"sharpe")

        self.horizontalLayout_13.addWidget(self.sharpe)


        self.horizontalLayout_9.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.horizontalLayout_9.addWidget(self.widget_12)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_en_tete.setText(QCoreApplication.translate("MainWindow", u"Outil d'analyse d'un ticker donn\u00e9 sur une p\u00e9riode souhait\u00e9e ", None))
        self.label_ticker.setText(QCoreApplication.translate("MainWindow", u"Choix du ticker", None))
        self.ticker.setText(QCoreApplication.translate("MainWindow", u"AMZN", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Choix de la date de d\u00e9part et de fin", None))
        self.depart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.fin.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.bouton_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirmer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rendement global sur la p\u00e9riode", None))
        self.rendement.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Volatilit\u00e9 sur la p\u00e9riode", None))
        self.vol.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ratio de Sharpe sur la p\u00e9riode ", None))
        self.sharpe.setText("")
    # retranslateUi

