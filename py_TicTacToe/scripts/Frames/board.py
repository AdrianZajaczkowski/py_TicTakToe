import tkinter as tk
from tkinter import ttk
import numpy as np
from constants import SIZE
from logic import Logic


class Board(tk.Toplevel):
    def __init__(self, app):

        #self.backWindow = app
        self.window = app

        self.canvas = tk.Canvas(
            self.window, width=SIZE["WIDTH"], height=SIZE["HEIGHT"])
        self.canvas.pack()

        self.window.title("Start")

        self.drawBoard()
        Logic(self.window, self.canvas)
        self.window.mainloop

    def mainloop(self):
        self.window.mainloop()

    def drawBoard(self):

        for i in range(2):
            self.canvas.create_line(
                (i + 1) * SIZE["WIDTH"] / 3, 40, (i+1) * SIZE["WIDTH"]/3, SIZE["WIDTH"])
        for i in range(2):
            self.canvas.create_line(
                0, (i+1)*SIZE["WIDTH"]/3, SIZE["WIDTH"], (i+1)*SIZE["WIDTH"]/3)
