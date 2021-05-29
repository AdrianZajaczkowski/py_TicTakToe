import pygame
import time
from game.game import Game, GAME_STATES
from game.engine.board import board
from game.engine.constants import COLORS, WINDOW_SIZE


WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('TicTakToe')
WINDOW.fill(COLORS.D_GRAY.value)
pygame.display.update()


def start():
  run = True
  hovered = 0
  gb = board(WINDOW)
  clock = pygame.time.Clock()
  game = Game(gb)
  while run:
    clock.tick(60)
    if(game.ended):
      time.sleep(3)
      run = False
    for i in range(9):
      if board.fields[i].collidepoint(pygame.mouse.get_pos()):
        if(hovered == i or game.tiles[i] != 0):
          continue
        gb.draw_tiles(game.tiles)
        gb._drawX(board.piv_tiles[i], True) if game.current_player == 1 else gb._drawO(
            board.piv_tiles[i], True)
        hovered = i
        pygame.display.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        for i in range(9):
          if board.fields[i].collidepoint(pygame.mouse.get_pos()):
            if(game.tiles[i] == 0 and game.state == GAME_STATES.GS_TURN):
              game.makeMove(i)
  pygame.quit()


start()
