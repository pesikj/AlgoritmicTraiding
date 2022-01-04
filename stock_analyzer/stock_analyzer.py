import numpy as np
import pandas as pd
from ta.trend import ADXIndicator


class StockAnalyzer:
    symbol: str
    data: pd.DataFrame

    def add_adx_indicator(self):
        df = self.df
        indicator_adx = ADXIndicator(high=df["high"], low=df["low"], close=df["close"])
        df["adx"] = indicator_adx.adx()
        df["adx_pos"] = indicator_adx.adx_pos()
        df["adx_neg"] = indicator_adx.adx_neg()
        df["di_higher"] = np.where((df["adx_pos"] > df["adx_neg"]), "pos", "neg")
        df["di_higher_t-1"] = df["di_higher"].shift()

        df["signal_buy"] = np.where(
            (df["adx"] > 20) & (df["di_higher"] == "pos") & (df["di_higher_t-1"] == "neg"),
            True, False)
        df["signal_sell"] = np.where(
            (df["adx"] > 20) & (df["di_higher"] == "neg") & (df["di_higher_t-1"] == "pos"),
            True, False)
        return df

    def __init__(self, symbol, df):
        self.symbol = symbol
        self.df = df
