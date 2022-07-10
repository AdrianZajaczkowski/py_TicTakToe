import tkinter as tk
from tkinter import ttk
import numpy as np
from constants import SIZE
from logic import Logic


class Board(tk.Toplevel):
    def __init__(self, rounds):
        self.rounds = rounds
        #self.backWindow = app
        self.window = tk.Tk()
        positionRight = int(
            self.window.winfo_screenwidth()/2 - SIZE["WIDTH"]/2)
        positionDown = int(
            self.window.winfo_screenheight()/2 - SIZE["WIDTH"]/2)

        self.canvas = tk.Canvas(
            self.window, width=SIZE["WIDTH"], height=SIZE["HEIGHT"])
        self.canvas.pack()
        self.window.geometry("+{}+{}".format(positionRight, positionDown))
        self.drawBoard()

        Logic(self.window, self.canvas, self.rounds)
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
