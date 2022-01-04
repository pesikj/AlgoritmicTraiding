import tkinter as tk
from tkinter import ttk
from charter import charter
import matplotlib.pyplot as plt

import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from data_reader.data_reader import DataReader
from stock_analyzer import stock_analyzer


class ChartFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.contents.set("GOOGL")
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>', self.print_contents)

        self.btn_add_chart = tk.Button(master=self.master, text="Load stock", command=self.add_chart)
        self.btn_add_chart.pack()

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.data_reader = DataReader()

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

    def add_chart(self):
        self.fig.clf()
        df = self.data_reader.get_dataframe(self.contents.get())
        sa = stock_analyzer.StockAnalyzer(self.contents.get(), df)
        aapl = sa.add_adx_indicator()

        ax1 = plt.subplot2grid((11, 1), (0, 0), rowspan=5, colspan=1, fig=self.fig)
        ax2 = plt.subplot2grid((11, 1), (6, 0), rowspan=5, colspan=1, fig=self.fig)
        ax1.plot(aapl["datetime"], aapl['close'], linewidth=2, color='#ff9800')

        df_buy = df[df["signal_buy"]]
        ax1.plot(df_buy["datetime"], df_buy['close'], marker='^', color='#26a69a', markersize=14, linewidth=0, label='BUY SIGNAL')

        df_sell = df[df["signal_sell"]]
        ax1.plot(df_sell["datetime"], df_sell['close'], marker = 'v', color = '#f44336', markersize = 14, linewidth = 0, label = 'SELL SIGNAL')

        ax1.set_title('AAPL CLOSING PRICE')

        ax2.plot(aapl['adx_neg'], color='#26a69a', label='+ DI 14', linewidth=3, alpha=0.3)
        ax2.plot(aapl['adx_pos'], color='#f44336', label='- DI 14', linewidth=3, alpha=0.3)
        ax2.plot(aapl['adx'], color='#2196f3', label='ADX 14', linewidth=3)
        ax2.axhline(25, color='grey', linewidth=2, linestyle='--')
        ax2.legend()
        ax2.set_title('AAPL ADX 14')

        self.canvas.draw()


ws = tk.Tk()
ws.geometry("800x600")
ws.title("Algorithmic Trading")
frame1 = ChartFrame(ws)

ws.mainloop()
