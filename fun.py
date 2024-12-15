import subprocess
import pandas as pd

def remake_file():
    yah = ["pyside6-uic", "yahoo.ui", "-o", "yahoo.py"]
    tab = ["pyside6-uic", "table.ui", "-o", "table.py"]
    subprocess.run(yah, check=True)
    subprocess.run(tab, check=True)

def get_ratio(text_1, data_1, text_2, data_2):
    ratio_data = pd.merge(left = data_1, right = data_2, on = "Date", suffixes = (f"_{text_1}", f"_{text_2}"))
    ratio_data["Close"] = ratio_data[f"Close_{text_1}"] / ratio_data[f"Close_{text_2}"] 
    return ratio_data[["Date", "Close"]]
