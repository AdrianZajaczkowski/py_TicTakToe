from board import Board
from constants import SIZE
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.round = 1
        self.title("TicTacToe: Menu")
        positionRight = int(
            self.winfo_screenwidth()/2 - SIZE["WIDTH"]/2)
        positionDown = int(
            self.winfo_screenheight()/2 - SIZE["WIDTH"]/2+20)

        self.geometry("+{}+{}".format(positionRight, positionDown))

        self.start = ttk.Button(
            self, text="Start the game", command=self._start, width=50)

        self.start.pack()
        self.again = ttk.Button(
            self, text="Play again", command=self._again, width=50)

        self.start.pack()

    def _start(self):
        # pass
        Board(self.round)
        self.round += 1
        # app.withdraw()

    def _again():
        pass


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
