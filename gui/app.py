import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from charter.charter import Charter
from data_reader.data_reader import DataReader
from stock_analyzer import stock_analyzer
import tkcalendar


class ChartFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.initUI()
        # self.pack()
        #
        # self.entrythingy = tk.Entry()
        # self.entrythingy.pack()
        #
        # self.contents = tk.StringVar()
        # self.contents.set("GOOGL")
        # self.entrythingy["textvariable"] = self.contents
        #
        # # Define a callback for when the user hits return.
        # # It prints the current value of the variable.
        # self.entrythingy.bind('<Key-Return>', self.print_contents)
        #
        # self.btn_add_chart = tk.Button(master=self.master, text="Load stock", command=self.add_chart)
        # self.btn_add_chart.pack()
        #
        # self.fig = Figure(figsize=(5, 4), dpi=100)
        # self.ax = self.fig.add_subplot(111)
        #
        # self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        # self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.data_reader = DataReader()

    def initUI(self):
        plot_frame = tk.Frame(self.master)
        plot_frame.pack(fill=tk.BOTH)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        button_frame = tk.Frame(self.master)

        lbl1 = tk.Label(button_frame, text="Symbol").grid(row=0, sticky=tk.W)
        self.entry_symbol = tk.Entry(button_frame)
        self.entry_symbol.grid(row=0, column=1)

        self.contents = tk.StringVar()
        self.contents.set("GOOGL")
        self.entry_symbol["textvariable"] = self.contents

        lbl2 = tk.Label(button_frame, text="Date from").grid(row=1, sticky=tk.W)
        self.entry_date_from = tk.Entry(button_frame)
        self.entry_date_from.grid(row=1, column=1)

        btn_add_chart = tk.Button(master=button_frame, text="Load stock", command=self.add_chart)
        btn_add_chart.grid(row=2, sticky=tk.W)

        button_frame.pack(fill=tk.BOTH)


    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

    def add_chart(self):
        self.fig.clf()
        charter = Charter()

        charter.get_adx_chart(self.fig, self.contents.get())

        self.canvas.draw()


ws = tk.Tk()
ws.geometry("800x600")
ws.title("Algorithmic Trading")
frame1 = ChartFrame(ws)

ws.mainloop()
