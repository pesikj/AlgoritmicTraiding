import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from charter.charter import Charter
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
        charter = Charter()

        charter.get_adx_chart(self.fig, self.contents.get())

        self.canvas.draw()


ws = tk.Tk()
ws.geometry("800x600")
ws.title("Algorithmic Trading")
frame1 = ChartFrame(ws)

ws.mainloop()
