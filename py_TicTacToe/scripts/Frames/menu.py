from board import Board
from constants import SIZE
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        geom = f"{SIZE['WIDTH']}x{SIZE['HEIGHT']}"

        self.title("TicTacToe")
        self.geometry(geom)

        self.start = ttk.Button(
            self, text="Start the game", command=self._start, width=50)

        self.start.pack()

    def _start(self):
        # pass
        Board(app)
        # app.withdraw()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
