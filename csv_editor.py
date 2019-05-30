#!/usr/bin/python3

import csv
import tkinter as tk
from tkinter import ttk


class CsvEditor(tk.Tk):
    def __init__(self, filedata):
        super().__init__()
        for row in filedata:
            Record(self, row).pack()
        self.mainloop()


class Record(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master)
        self.cells = []
        self.data = list(data)
        for cell in self.data:

            cell_data = tk.StringVar()
            cell_data.set(cell)

            cell_entry = tk.Entry(self, textvariable=cell_data)

            self.cells.append(cell_data)

            cell_entry.pack(side=tk.LEFT)
