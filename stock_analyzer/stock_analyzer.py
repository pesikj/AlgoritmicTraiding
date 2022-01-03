import numpy as np
import pandas as pd
from ta.trend import ADXIndicator


class StockData:
    symbol: str
    data: pd.DataFrame

    def add_adx_indicator(self):
        df = self.df
        indicator_adx = ADXIndicator(high=df["high"], low=df["low"], close=df["close"])
        df["adx"] = indicator_adx.adx()
        df["di_pos"] = indicator_adx.adx_pos()
        df["di_neg"] = indicator_adx.adx_neg()
        df["di_higher"] = np.where((df["di_pos"] > df["di_neg"]), "pos", "neg")
        df["di_higher_t-1"] = df["di_higher"].shift()

        df["signal_buy"] = np.where(
            (df["adx"] > 20) & (df["di_higher"] == "pos") & (df["di_higher_t-1"] == "neg"),
            True, False)
        df["signal_sell"] = np.where(
            (df["adx"] > 20) & (df["di_higher"] == "neg") & (df["di_higher_t-1"] == "pos"),
            True, False)
        df_transactions = df[(df["signal_buy"]) | (df["signal_sell"])]
        return df_transactions

    def __init__(self, symbol, df):
        self.symbol = symbol
        self.df = df
