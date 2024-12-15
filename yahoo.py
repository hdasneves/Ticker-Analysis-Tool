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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.onglets = QTabWidget(self.widget_4)
        self.onglets.setObjectName(u"onglets")
        self.onglets.setTabShape(QTabWidget.Triangular)
        self.onglets.setUsesScrollButtons(True)
        self.onglets.setTabBarAutoHide(False)
        self.choix_period = QWidget()
        self.choix_period.setObjectName(u"choix_period")
        self.horizontalLayout_4 = QHBoxLayout(self.choix_period)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_6 = QWidget(self.choix_period)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_ticker = QLabel(self.widget_6)
        self.label_ticker.setObjectName(u"label_ticker")

        self.verticalLayout_2.addWidget(self.label_ticker, 0, Qt.AlignHCenter)

        self.ticker = QLineEdit(self.widget_6)
        self.ticker.setObjectName(u"ticker")

        self.verticalLayout_2.addWidget(self.ticker)


        self.horizontalLayout_4.addWidget(self.widget_6)

        self.line_3 = QFrame(self.choix_period)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.widget_7 = QWidget(self.choix_period)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(6)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_date = QLabel(self.widget_7)
        self.label_date.setObjectName(u"label_date")

        self.verticalLayout_3.addWidget(self.label_date, 0, Qt.AlignHCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.depart = QDateEdit(self.widget_7)
        self.depart.setObjectName(u"depart")
        self.depart.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(1, 0, 0)))
        self.depart.setTime(QTime(1, 0, 0))
        self.depart.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_5.addWidget(self.depart)

        self.fin = QDateEdit(self.widget_7)
        self.fin.setObjectName(u"fin")
        self.fin.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(1, 0, 0)))
        self.fin.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_5.addWidget(self.fin)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.horizontalLayout_4.addWidget(self.widget_7)

        self.line_4 = QFrame(self.choix_period)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.widget_8 = QWidget(self.choix_period)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy2.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.afficher_1 = QPushButton(self.widget_8)
        self.afficher_1.setObjectName(u"afficher_1")

        self.verticalLayout_5.addWidget(self.afficher_1)

        self.bouton_confirm = QPushButton(self.widget_8)
        self.bouton_confirm.setObjectName(u"bouton_confirm")

        self.verticalLayout_5.addWidget(self.bouton_confirm)


        self.horizontalLayout_4.addWidget(self.widget_8, 0, Qt.AlignBottom)

        self.onglets.addTab(self.choix_period, "")
        self.comparaison = QWidget()
        self.comparaison.setObjectName(u"comparaison")
        self.horizontalLayout_14 = QHBoxLayout(self.comparaison)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_13 = QWidget(self.comparaison)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(4)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy4)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_ticker_comparaison = QLabel(self.widget_13)
        self.label_ticker_comparaison.setObjectName(u"label_ticker_comparaison")

        self.verticalLayout_6.addWidget(self.label_ticker_comparaison, 0, Qt.AlignHCenter)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.actif_a = QLineEdit(self.widget_13)
        self.actif_a.setObjectName(u"actif_a")

        self.horizontalLayout_15.addWidget(self.actif_a)

        self.actif_b = QLineEdit(self.widget_13)
        self.actif_b.setObjectName(u"actif_b")

        self.horizontalLayout_15.addWidget(self.actif_b)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_16.addLayout(self.verticalLayout_6)


        self.horizontalLayout_14.addWidget(self.widget_13)

        self.line_6 = QFrame(self.comparaison)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_6)

        self.widget_14 = QWidget(self.comparaison)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy3.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy3)
        self.horizontalLayout_18 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_date_comparaison = QLabel(self.widget_14)
        self.label_date_comparaison.setObjectName(u"label_date_comparaison")

        self.verticalLayout_7.addWidget(self.label_date_comparaison, 0, Qt.AlignHCenter)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.depart_comparaison = QDateEdit(self.widget_14)
        self.depart_comparaison.setObjectName(u"depart_comparaison")
        self.depart_comparaison.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(1, 0, 0)))
        self.depart_comparaison.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_17.addWidget(self.depart_comparaison)

        self.fin_comparaison = QDateEdit(self.widget_14)
        self.fin_comparaison.setObjectName(u"fin_comparaison")
        self.fin_comparaison.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(1, 0, 0)))
        self.fin_comparaison.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_17.addWidget(self.fin_comparaison)


        self.verticalLayout_7.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_18.addLayout(self.verticalLayout_7)


        self.horizontalLayout_14.addWidget(self.widget_14)

        self.line_7 = QFrame(self.comparaison)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_7)

        self.widget_15 = QWidget(self.comparaison)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy2.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy2)
        self.verticalLayout_8 = QVBoxLayout(self.widget_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.afficher_2 = QPushButton(self.widget_15)
        self.afficher_2.setObjectName(u"afficher_2")

        self.verticalLayout_8.addWidget(self.afficher_2)

        self.bouton_confirm_comparaison = QPushButton(self.widget_15)
        self.bouton_confirm_comparaison.setObjectName(u"bouton_confirm_comparaison")

        self.verticalLayout_8.addWidget(self.bouton_confirm_comparaison, 0, Qt.AlignBottom)


        self.horizontalLayout_14.addWidget(self.widget_15)

        self.onglets.addTab(self.comparaison, "")

        self.horizontalLayout_3.addWidget(self.onglets)


        self.verticalLayout.addWidget(self.widget_4)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.partie_graph = QWidget(self.widget)
        self.partie_graph.setObjectName(u"partie_graph")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(8)
        sizePolicy5.setHeightForWidth(self.partie_graph.sizePolicy().hasHeightForWidth())
        self.partie_graph.setSizePolicy(sizePolicy5)
        self.horizontalLayout_7 = QHBoxLayout(self.partie_graph)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.choix_graph = QStackedWidget(self.partie_graph)
        self.choix_graph.setObjectName(u"choix_graph")
        self.un_ticker_ = QWidget()
        self.un_ticker_.setObjectName(u"un_ticker_")
        self.horizontalLayout_30 = QHBoxLayout(self.un_ticker_)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.graph_ticker = QChartView(self.un_ticker_)
        self.graph_ticker.setObjectName(u"graph_ticker")

        self.horizontalLayout_30.addWidget(self.graph_ticker)

        self.choix_graph.addWidget(self.un_ticker_)
        self.deux_tickers_ = QWidget()
        self.deux_tickers_.setObjectName(u"deux_tickers_")
        self.horizontalLayout_27 = QHBoxLayout(self.deux_tickers_)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.choix_graph_deux_tickers = QTabWidget(self.deux_tickers_)
        self.choix_graph_deux_tickers.setObjectName(u"choix_graph_deux_tickers")
        self.evo = QWidget()
        self.evo.setObjectName(u"evo")
        self.horizontalLayout_28 = QHBoxLayout(self.evo)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.graph_evo_tickers = QChartView(self.evo)
        self.graph_evo_tickers.setObjectName(u"graph_evo_tickers")

        self.horizontalLayout_28.addWidget(self.graph_evo_tickers)

        self.choix_graph_deux_tickers.addTab(self.evo, "")
        self.ratio = QWidget()
        self.ratio.setObjectName(u"ratio")
        self.horizontalLayout_29 = QHBoxLayout(self.ratio)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.graph_ratio_ticker = QChartView(self.ratio)
        self.graph_ratio_ticker.setObjectName(u"graph_ratio_ticker")

        self.horizontalLayout_29.addWidget(self.graph_ratio_ticker)

        self.choix_graph_deux_tickers.addTab(self.ratio, "")

        self.horizontalLayout_27.addWidget(self.choix_graph_deux_tickers)

        self.choix_graph.addWidget(self.deux_tickers_)

        self.horizontalLayout_7.addWidget(self.choix_graph)


        self.verticalLayout.addWidget(self.partie_graph)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(5)
        sizePolicy6.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy6)
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.retours = QStackedWidget(self.widget_3)
        self.retours.setObjectName(u"retours")
        self.deux_tickers = QWidget()
        self.deux_tickers.setObjectName(u"deux_tickers")
        self.verticalLayout_11 = QVBoxLayout(self.deux_tickers)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_16 = QWidget(self.deux_tickers)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_19 = QWidget(self.widget_16)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_r_a = QLabel(self.widget_19)
        self.label_r_a.setObjectName(u"label_r_a")

        self.horizontalLayout_12.addWidget(self.label_r_a)

        self.r_a = QLabel(self.widget_19)
        self.r_a.setObjectName(u"r_a")

        self.horizontalLayout_12.addWidget(self.r_a)


        self.horizontalLayout_11.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_16)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_r_b = QLabel(self.widget_20)
        self.label_r_b.setObjectName(u"label_r_b")

        self.horizontalLayout_22.addWidget(self.label_r_b)

        self.r_b = QLabel(self.widget_20)
        self.r_b.setObjectName(u"r_b")

        self.horizontalLayout_22.addWidget(self.r_b)


        self.horizontalLayout_11.addWidget(self.widget_20)


        self.verticalLayout_11.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.deux_tickers)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_22 = QWidget(self.widget_17)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_v_a = QLabel(self.widget_22)
        self.label_v_a.setObjectName(u"label_v_a")

        self.horizontalLayout_21.addWidget(self.label_v_a)

        self.v_a = QLabel(self.widget_22)
        self.v_a.setObjectName(u"v_a")

        self.horizontalLayout_21.addWidget(self.v_a)


        self.horizontalLayout_13.addWidget(self.widget_22)

        self.widget_21 = QWidget(self.widget_17)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_v_b = QLabel(self.widget_21)
        self.label_v_b.setObjectName(u"label_v_b")

        self.horizontalLayout_23.addWidget(self.label_v_b)

        self.v_b = QLabel(self.widget_21)
        self.v_b.setObjectName(u"v_b")

        self.horizontalLayout_23.addWidget(self.v_b)


        self.horizontalLayout_13.addWidget(self.widget_21)


        self.verticalLayout_11.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.deux_tickers)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_23 = QWidget(self.widget_18)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_diff_r = QLabel(self.widget_23)
        self.label_diff_r.setObjectName(u"label_diff_r")

        self.horizontalLayout_20.addWidget(self.label_diff_r)

        self.r_diff = QLabel(self.widget_23)
        self.r_diff.setObjectName(u"r_diff")

        self.horizontalLayout_20.addWidget(self.r_diff)


        self.horizontalLayout_19.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_18)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_diff_v = QLabel(self.widget_24)
        self.label_diff_v.setObjectName(u"label_diff_v")

        self.horizontalLayout_24.addWidget(self.label_diff_v)

        self.v_diff = QLabel(self.widget_24)
        self.v_diff.setObjectName(u"v_diff")

        self.horizontalLayout_24.addWidget(self.v_diff)


        self.horizontalLayout_19.addWidget(self.widget_24)


        self.verticalLayout_11.addWidget(self.widget_18)

        self.retours.addWidget(self.deux_tickers)
        self.un_ticker = QWidget()
        self.un_ticker.setObjectName(u"un_ticker")
        self.horizontalLayout_8 = QHBoxLayout(self.un_ticker)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.one_ticker_choice = QTabWidget(self.un_ticker)
        self.one_ticker_choice.setObjectName(u"one_ticker_choice")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_2 = QWidget(self.tab_7)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_12 = QVBoxLayout(self.widget_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_25 = QWidget(self.widget_2)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_rendement = QLabel(self.widget_25)
        self.label_rendement.setObjectName(u"label_rendement")

        self.horizontalLayout_25.addWidget(self.label_rendement)

        self.rendement = QLabel(self.widget_25)
        self.rendement.setObjectName(u"rendement")

        self.horizontalLayout_25.addWidget(self.rendement)


        self.verticalLayout_12.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.widget_2)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_vol = QLabel(self.widget_26)
        self.label_vol.setObjectName(u"label_vol")

        self.horizontalLayout_26.addWidget(self.label_vol)

        self.vol = QLabel(self.widget_26)
        self.vol.setObjectName(u"vol")

        self.horizontalLayout_26.addWidget(self.vol)


        self.verticalLayout_12.addWidget(self.widget_26)


        self.horizontalLayout_9.addWidget(self.widget_2)

        self.widget_5 = QWidget(self.tab_7)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_13 = QVBoxLayout(self.widget_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_27 = QWidget(self.widget_5)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_per = QLabel(self.widget_27)
        self.label_per.setObjectName(u"label_per")

        self.horizontalLayout_31.addWidget(self.label_per)

        self.per = QLabel(self.widget_27)
        self.per.setObjectName(u"per")

        self.horizontalLayout_31.addWidget(self.per)


        self.verticalLayout_13.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_5)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_beta = QLabel(self.widget_28)
        self.label_beta.setObjectName(u"label_beta")

        self.horizontalLayout_32.addWidget(self.label_beta)

        self.beta = QLabel(self.widget_28)
        self.beta.setObjectName(u"beta")

        self.horizontalLayout_32.addWidget(self.beta)


        self.verticalLayout_13.addWidget(self.widget_28)


        self.horizontalLayout_9.addWidget(self.widget_5)

        self.one_ticker_choice.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_9 = QVBoxLayout(self.tab_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.finviz_selector = QComboBox(self.tab_8)
        self.finviz_selector.setObjectName(u"finviz_selector")

        self.verticalLayout_9.addWidget(self.finviz_selector)

        self.finviz_info = QLabel(self.tab_8)
        self.finviz_info.setObjectName(u"finviz_info")

        self.verticalLayout_9.addWidget(self.finviz_info)

        self.one_ticker_choice.addTab(self.tab_8, "")

        self.horizontalLayout_8.addWidget(self.one_ticker_choice)

        self.retours.addWidget(self.un_ticker)

        self.verticalLayout_4.addWidget(self.retours)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.onglets.setCurrentIndex(0)
        self.choix_graph.setCurrentIndex(0)
        self.choix_graph_deux_tickers.setCurrentIndex(0)
        self.retours.setCurrentIndex(1)
        self.one_ticker_choice.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_en_tete.setText(QCoreApplication.translate("MainWindow", u"Outil d'analyse de tickers sur une p\u00e9riode souhait\u00e9e ", None))
        self.label_ticker.setText(QCoreApplication.translate("MainWindow", u"Choix du ticker", None))
        self.ticker.setText(QCoreApplication.translate("MainWindow", u"AMZN", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Choix de la p\u00e9riode", None))
        self.depart.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.fin.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.afficher_1.setText(QCoreApplication.translate("MainWindow", u"Afficher CSV", None))
        self.bouton_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirmer", None))
        self.onglets.setTabText(self.onglets.indexOf(self.choix_period), QCoreApplication.translate("MainWindow", u"Analyse d'un ticker donn\u00e9", None))
        self.label_ticker_comparaison.setText(QCoreApplication.translate("MainWindow", u"Choix de l'actif A et B", None))
        self.actif_a.setText(QCoreApplication.translate("MainWindow", u"AMZN", None))
        self.actif_b.setText(QCoreApplication.translate("MainWindow", u"AAPL", None))
        self.label_date_comparaison.setText(QCoreApplication.translate("MainWindow", u"Choix de la p\u00e9riode", None))
        self.depart_comparaison.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.fin_comparaison.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.afficher_2.setText(QCoreApplication.translate("MainWindow", u"Afficher CSV", None))
        self.bouton_confirm_comparaison.setText(QCoreApplication.translate("MainWindow", u"Confirmer", None))
        self.onglets.setTabText(self.onglets.indexOf(self.comparaison), QCoreApplication.translate("MainWindow", u"Comparaison entre deux tickers", None))
        self.choix_graph_deux_tickers.setTabText(self.choix_graph_deux_tickers.indexOf(self.evo), QCoreApplication.translate("MainWindow", u"Evolution des cours", None))
        self.choix_graph_deux_tickers.setTabText(self.choix_graph_deux_tickers.indexOf(self.ratio), QCoreApplication.translate("MainWindow", u"Ratio entre les deux cours", None))
        self.label_r_a.setText("")
        self.r_a.setText("")
        self.label_r_b.setText("")
        self.r_b.setText("")
        self.label_v_a.setText("")
        self.v_a.setText("")
        self.label_v_b.setText("")
        self.v_b.setText("")
        self.label_diff_r.setText("")
        self.r_diff.setText("")
        self.label_diff_v.setText("")
        self.v_diff.setText("")
        self.label_rendement.setText("")
        self.rendement.setText("")
        self.label_vol.setText("")
        self.vol.setText("")
        self.label_per.setText("")
        self.per.setText("")
        self.label_beta.setText("")
        self.beta.setText("")
        self.one_ticker_choice.setTabText(self.one_ticker_choice.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Informations li\u00e9es aux donn\u00e9es", None))
        self.finviz_info.setText("")
        self.one_ticker_choice.setTabText(self.one_ticker_choice.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Informations obtenues sur Finviz", None))
    # retranslateUi

