import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import os
import subprocess

def remake_file(): 
    ui_file = "test.ui"
    py_file = "yahoo.py"
    subprocess.run(['pyside6-uic', ui_file, '-o', py_file], check=True)

def log_data(data):
    return np.log(data)
    

def obtenir_infos(ticker, dep, ar):
    dep = datetime.strptime(dep, '%Y/%m/%d').strftime('%Y-%m-%d')
    ar = datetime.strptime(ar, '%Y/%m/%d').strftime('%Y-%m-%d')
    donnees = yf.Ticker(ticker).history(start = dep, end = ar, interval = "1d")
    donnees = pd.DataFrame({"Date": donnees.index,"Close": donnees["Close"].squeeze()}).reset_index(drop = True)

    deb = donnees["Close"].iloc[0]
    fin = donnees["Close"].iloc[-1]
    rendement = round(((fin - deb)/deb)*100, 2)

    moyenne = np.mean(donnees["Close"])
    ecart_type = np.var(donnees["Close"])**0.5
    volatilite = np.round((ecart_type / moyenne) * 100, 2)

    return {"data" : donnees, "rendement" : rendement, "volatilite" : volatilite}

