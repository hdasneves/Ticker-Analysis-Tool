import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import os
import subprocess

def remake_file(): 
    ui_file = "yahoo.ui"
    py_file = "yahoo.py"
    subprocess.run(['pyside6-uic', ui_file, '-o', py_file], check=True)

def import_données(ticker, dep, ar):
    dep = datetime.strptime(dep, '%Y/%m/%d').strftime('%Y-%m-%d')
    ar = datetime.strptime(ar, '%Y/%m/%d').strftime('%Y-%m-%d')
    donnees = yf.Ticker(ticker).history(start = dep, end = ar, interval = "1d")
    return pd.DataFrame({"Date": donnees.index,"Close": donnees["Close"].squeeze()}).reset_index(drop = True)

def obtenir_rendement(donnees):
    deb = donnees["Close"][0]
    fin = donnees["Close"][len(donnees["Close"])-1]
    rendement = (fin - deb)/deb
    return round(rendement*100, 2)

def obtenir_volatilite(donnees):
    return round(np.std(donnees["Close"]), 2)