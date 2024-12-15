import subprocess
import pandas as pd

def get_ratio(text_1, data_1, text_2, data_2):
    ratio_data = pd.merge(left = data_1, right = data_2, on = "Date", suffixes = (f"_{text_1}", f"_{text_2}"))
    ratio_data["Close"] = ratio_data[f"Close_{text_1}"] / ratio_data[f"Close_{text_2}"] 
    return ratio_data[["Date", "Close"]]
