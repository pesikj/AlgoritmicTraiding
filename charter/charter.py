import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from stock_analyzer.stock_analyzer import StockAnalyzer


class Charter:
    data_frame: pd.DataFrame
    symbol: str

    def get_data_frame(self):
        pass

    def get_adx_chart(self, fig, symbol):
        stock_analyzer_obj = StockAnalyzer(symbol)
        df = stock_analyzer_obj.adx_indicator()

        ax1 = plt.subplot2grid((11, 1), (0, 0), rowspan=5, colspan=1, fig=fig)
        ax2 = plt.subplot2grid((11, 1), (6, 0), rowspan=5, colspan=1, fig=fig)
        ax1.plot(df["datetime"], df['close'], linewidth=2, color='#ff9800')

        ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))

        df_buy = df[df["signal_buy"]]
        ax1.plot(df_buy["datetime"], df_buy['close'], marker='^', color='#26a69a', linewidth=0,
                 label='BUY SIGNAL')

        df_sell = df[df["signal_sell"]]
        ax1.plot(df_sell["datetime"], df_sell['close'], marker='v', color='#f44336', linewidth=0,
                 label='SELL SIGNAL')

        ax1.set_title('df CLOSING PRICE')

        ax2.plot(df['adx_neg'], color='#26a69a', label='+ DI 14', linewidth=3, alpha=0.3)
        ax2.plot(df['adx_pos'], color='#f44336', label='- DI 14', linewidth=3, alpha=0.3)
        ax2.plot(df['adx'], color='#2196f3', label='ADX 14', linewidth=3)
        ax2.axhline(25, color='grey', linewidth=2, linestyle='--')
        ax2.legend()
        ax2.set_title('df ADX 14')
