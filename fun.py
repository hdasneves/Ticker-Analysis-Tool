import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import subprocess

def obtenir_infos(ticker, dep, ar):
    dep = datetime.strptime(dep, '%Y/%m/%d').strftime('%Y-%m-%d')
    ar = datetime.strptime(ar, '%Y/%m/%d').strftime('%Y-%m-%d')
    donnees = yf.Ticker(ticker).history(start = dep, end = ar, interval = "1d")

    if donnees.empty :
        return None

    donnees.index = donnees.index.tz_localize(None).normalize().strftime("%Y-%m-%d")
    donnees = pd.DataFrame({"Date": donnees.index,"Close": donnees["Close"].squeeze()}).reset_index(drop = True)

    deb = donnees["Close"].iloc[0]
    fin = donnees["Close"].iloc[-1]
    rendement = round(((fin - deb)/deb)*100, 2)

    moyenne = np.mean(donnees["Close"])
    ecart_type = np.var(donnees["Close"])**0.5
    volatilite = round(ecart_type, 2)

    per = yf.Ticker(ticker).info.get("trailingPE")
    beta = yf.Ticker(ticker).info.get("beta")

    return {"data" : donnees, "rendement" : rendement, "volatilite" : volatilite, "per" : per, "beta" : beta}

def get_ratio(text_1, data_1, text_2, data_2):
    ratio_data = pd.merge(left = data_1, right = data_2, on = "Date", suffixes = (f"_{text_1}", f"_{text_2}"))
    ratio_data["Close"] = ratio_data[f"Close_{text_1}"] / ratio_data[f"Close_{text_2}"] #Utilisation de close au lieu de ratio pour réutiliser la fonction linegraph
    return ratio_data[["Date", "Close"]]


