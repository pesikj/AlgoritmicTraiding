import tkinter as tk
from tkinter import ttk
from charter import charter

import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        self.contents.set("GOOGL")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

        self.btn_add_chart = tk.Button(master=self.master, text="Load stock", command=self.add_chart)
        self.btn_add_chart.pack()

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

    def add_chart(self):
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        chr = charter.Charter(self.contents.get())
        chr.get_plot(ax)

        canvas = FigureCanvasTkAgg(fig, master=self.master)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


root = tk.Tk()
myapp = App(root)
myapp.mainloop()
