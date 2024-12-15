import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

finviz_ind = ["ROE", "Profit Margin", "Beta", "Market Cap", "P/E"]

class Ticker:
    def __init__(self, ticker, dep, ar):
        self.ticker = ticker
        self.dep = datetime.strptime(dep, '%Y/%m/%d').strftime('%Y-%m-%d')
        self.ar = datetime.strptime(ar, '%Y/%m/%d').strftime('%Y-%m-%d')
        self.data = self.__obtenir_infos()
        self.finviz_data = self.__get_finviz_info()
    
    def __obtenir_infos(self):
        tick = yf.Ticker(self.ticker)
        donnees = tick.history(start = self.dep, end = self.ar, interval = "1d")
        if donnees.empty :
            return None
        donnees.index = donnees.index.tz_localize(None).normalize().strftime("%Y-%m-%d")
        donnees = pd.DataFrame({"Date": donnees.index,"Close": donnees["Close"].squeeze()}).reset_index(drop = True)
        
        deb = donnees["Close"].iloc[0]
        fin = donnees["Close"].iloc[-1]
        rendement = round(((fin - deb)/deb)*100, 2)

        returns = donnees["Close"].pct_change().dropna()
        volatility = round(np.std(returns) * (252**0.5) * 100, 2)

        per = tick.info.get("trailingPE")
        beta = tick.info.get("beta")

        return {"data" : donnees, "rendement" : rendement, "volatilite" : volatility, "per" : per, "beta" : beta}
    
    def __get_finviz_info(self):
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
        }

        url = "https://finviz.com/quote.ashx?t="+ self.ticker +"&p=d"

        response = requests.get(url, headers = headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find("table", class_="snapshot-table2")  
            rows = table.find_all("tr")
            liste = []
            for row in rows:
                cols = row.find_all("td")
                for col in cols:
                    liste.append(col.text)
            fin_dic = {}
            for index, value in enumerate(liste):
                if value in finviz_ind:
                    fin_dic[value] = liste[index + 1]
            return fin_dic
        else:
            return {i : "Information non disponible !" for i in finviz_ind}