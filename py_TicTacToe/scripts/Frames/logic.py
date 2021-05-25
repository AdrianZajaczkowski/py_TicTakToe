import tkinter as tk
from tkinter import ttk
import numpy as np
from constants import SIZE, SYMBOL


class Logic():
    def __init__(self, window, canvas):

        self.window = window

        self.canvas = canvas

        self.turn_X = True
        self.start_X = True
        self.X_win = False
        self.O_win = False
        self.gameover = False
        self.reset_board = False
        self.tie = False
        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0
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
                                self.symbol_s, grid_pos[1]-self.symbol_s, width=self.symbol_s)

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
        player = [-1 if player == "X" else 1]
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
        pass

    def gameover(self):
        self.X_win = self.check_win(("X"))
        if not self.X_win:
            self.O_win = self.check_win("O")
        if not self.O_win:
            self.tie = self.is_tie()

        gameover = self.X_win or self.O_win or self.tie

        return gameover

    def gameover_window(self):
        pass

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

        '''if self.gameover():
                    self.gameover_window()
        else:
            self.canvas.delete("all")
'''
