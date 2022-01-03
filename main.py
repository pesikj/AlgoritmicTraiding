# https://medium.com/codex/algorithmic-trading-with-average-directional-index-in-python-2b5a20ecf06a
# https://school.stockcharts.com/doku.php?id=technical_indicators:average_directional_index_adx
# https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.ADXIndicator

import pandas as pd
from ta.utils import dropna

import tkinter as tk
from gui import app

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")
#
# fig = Figure(figsize=(5, 4), dpi=100)
# t = np.arange(0, 3, .01)
#
# ax = fig.add_subplot(111)
#
# ax = df["close"].plot(ax=ax)
#
# canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
# canvas.draw()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def _quit():
    root.quit()
    root.destroy()


# button = tkinter.Button(master=root, text="Quit", command=_quit)
# button.pack(side=tkinter.BOTTOM)
# tkinter.mainloop()

