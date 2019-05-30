#!/usr/bin/python3

import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class CsvEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.filepath = ''
        btnfrm = tk.Frame(self)
        btnfrm.pack(side=tk.BOTTOM)
        tk.Button(btnfrm, text='Open...', command=self.load_file).pack(side=tk.LEFT)
        tk.Button(btnfrm, text='Save', command=self.save_file).pack(side=tk.LEFT)
        tk.Button(btnfrm, text='Save As...', command=self.save_as).pack(side=tk.LEFT)

    def load_file(self):
        self.filepath = filedialog.askopenfilename()
        if not self.filepath:
            return
        self.records = []
        with open(self.filepath) as f:
            for row in csv.reader(f):
                new_record = Record(self, row)
                self.records.append(new_record)
                new_record.pack()

    def save_as(self):
        self.save_file(as_new=True)

    def save_file(self, as_new=False):
        if as_new:
            new_path = filedialog.asksaveasfilename()
            if new_path:
                self.filepath = new_path
        with open(self.filepath, 'w') as f:
            for record in self.records:
                row_data = []
                for cell in record.cells:
                    row_data.append(cell.get())
                f.write(f"{','.join(row_data)}\n")


    def load(self):
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


if __name__ == '__main__':
    app = CsvEditor()
    app.load()
