import pandas as pd
from data_reader import data_reader


class Charter:
    data_frame: pd.DataFrame
    symbol: str

    def __init__(self, symbol):
        self.symbol = symbol
        dr = data_reader.DataReader()
        self.data_frame = dr.get_dataframe("GOOGL")

    def get_plot(self, ax):
        self.data_frame["close"].plot(ax=ax)
