import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

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


