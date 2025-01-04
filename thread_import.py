from PySide6.QtCore import QThread, Signal
import class_ticker
import pandas as pd

def get_ratio(text_1, data_1, text_2, data_2):
    ratio_data = pd.merge(left = data_1, right = data_2, on = "Date", suffixes = (f"_{text_1}", f"_{text_2}"))
    ratio_data["Close"] = ratio_data[f"Close_{text_1}"] / ratio_data[f"Close_{text_2}"] 
    return ratio_data[["Date", "Close"]]

def get_ratio(text_1, data_1, text_2, data_2):
    ratio_data = pd.merge(left = data_1, right = data_2, on = "Date", suffixes = (f"_{text_1}", f"_{text_2}"))
    ratio_data["Close"] = ratio_data[f"Close_{text_1}"] / ratio_data[f"Close_{text_2}"] 
    return ratio_data[["Date", "Close"]]

class DataFetchWorker(QThread):
    finished = Signal(dict) 
    error = Signal(str) 

    def __init__(self, ticker_1, start_date, end_date, ticker_2 = None, nb_ticker = 1):
        super().__init__()
        self.ticker_1 = ticker_1
        self.ticker_2 = ticker_2
        self.nb_ticker = nb_ticker
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        if self.nb_ticker == 1:   
            infos = class_ticker.Ticker(self.ticker_1, self.start_date, self.end_date)
        
            if infos.data is None:
                self.error.emit("Erreur lors de l'import !")
                return 

            self.finished.emit({"data_1": infos.data, "finviz_data": infos.finviz_data})
        else : 
            actif_a = class_ticker.Ticker(self.ticker_1, self.start_date, self.end_date) 
            actif_b = class_ticker.Ticker(self.ticker_2, self.start_date, self.end_date) 

            if actif_a.data is None or actif_b.data is None : 
                self.error.emit("Erreur lors de l'import d'un des deux fichiers !")
                return
            ratio_data = get_ratio(text_1 = self.ticker_1, data_1 = actif_a.data["data"], text_2 = self.ticker_2, data_2 = actif_b.data["data"])
            self.finished.emit({"data_1": actif_a.data, "data_2": actif_b.data, "ratio" : ratio_data})

