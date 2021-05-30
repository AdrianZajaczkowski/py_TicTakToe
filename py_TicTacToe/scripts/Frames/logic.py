import tkinter as tk
from tkinter import ttk
import numpy as np
from constants import SIZE, SYMBOL


class Logic():
    def __init__(self, window, canvas, rounds):

        self.window = window
        self.winner = None
        self.rounds = rounds
        self.win = ''
        self.window.title(f'Round: {self.rounds}')
        self.canvas = canvas

        self.turn_X = True
        self.start_X = True
        self.X_win = False
        self.O_win = False
        self.gameover = False
        self.reset_board = False
        self.tie = False

        self.board_status = np.zeros(shape=(3, 3))
        self.symbol_s = SYMBOL["SIZE"]
        self.symbol_color_X = SYMBOL["X"]
        self.symbol_color_O = SYMBOL["O"]
        self.window.bind('<Button-1>', self.click)

    def draw_X(self, logic_pos):

        grid_pos = self.get_grid_pos(logic_pos)
        self.canvas.create_line(grid_pos[0]-self.symbol_s, grid_pos[1]-self.symbol_s, grid_pos[0] +
                                self.symbol_s, grid_pos[1]+self.symbol_s, width=self.symbol_s,)
        self.canvas.create_line(grid_pos[0]-self.symbol_s, grid_pos[1]+self.symbol_s, grid_pos[0] +
                                self.symbol_s, grid_pos[1]-self.symbol_s, width=self.symbol_s, fill=self.symbol_color_X)

    def draw_O(self, logic_pos):

        logic_pos = np.array(logic_pos)
        grid_pos = self.get_grid_pos(logic_pos)
        self.canvas.create_oval(grid_pos[0]-self.symbol_s, grid_pos[1]+self.symbol_s, grid_pos[0] +
                                self.symbol_s, grid_pos[1]-self.symbol_s, width=self.symbol_s, outline=self.symbol_color_O)

    def get_grid_pos(self, logic_position):
        logic_position = np.array(logic_position, dtype=int)
        return (SIZE["WIDTH"] / 3)*logic_position + SIZE["WIDTH"] / 6

    def get_logic_pos(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (SIZE["WIDTH"]/3), dtype=int)

    def ocuupied_place(self, logic_position):
        if self.board_status[logic_position[0]][logic_position[1]] == 0:
            return False
        else:
            return True

    def check_win(self, player):
        player = -1 if player == 'X' else 1
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True
        if self.board_status[2][0] == self.board_status[1][1] == self.board_status[0][2] == player:
            return True
        return False

    def is_tie(self):
        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True

        return tie

    def is_gameover(self):
        self.X_win = self.check_win('X')
        if not self.X_win:
            self.O_win = self.check_win('O')
        if not self.O_win:
            self.tie = self.is_tie()

        gameover = self.X_win or self.O_win or self.tie
        if self.X_win:
            self._winner('X won')
        elif self.O_win:
            self._winner('O won')
        elif self.tie:
            self._winner('is a tie')
        return gameover

    def gameover_window(self):
        self.reset_board = True

    def _winner(self, win):
        self.winner = tk.Tk()
        positionRight = int(
            self.window.winfo_screenwidth()/2 - SIZE["WIDTH"]/4)
        positionDown = int(
            self.window.winfo_screenheight()/2 - SIZE["WIDTH"]/4+20)
        self.winner.geometry("+{}+{}".format(positionRight, positionDown))
        self.button = tk.Button(self.winner, text=win, command=self._clean)
        self.button.config(font=('Helvetica bold', 40))
        self.button.pack()
        self.winner.title('Winner')

    def _clean(self):
        self.winner.destroy()
        self.window.destroy()
        self.reset_board = False

    def click(self, event):

        grid_position = [event.x, event.y]
        logic_position = self.get_logic_pos(grid_position)
        if not self.reset_board:
            if self.turn_X:
                if not self.ocuupied_place(logic_position):
                    self.draw_X(logic_position)
                    self.board_status[logic_position[0]
                                      ][logic_position[1]] = -1
                    self.turn_X = not self.turn_X
            else:
                if not self.ocuupied_place(logic_position):
                    self.draw_O(logic_position)
                    self.board_status[logic_position[0]
                                      ][logic_position[1]] = 1
                    self.turn_X = not self.turn_X
            if self.is_gameover():
                self.gameover_window()
