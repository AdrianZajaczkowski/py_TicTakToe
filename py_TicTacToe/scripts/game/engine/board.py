import pygame
from .constants import GAME_SIZE, COLORS, PIV_POINTS, LINE_WIDTH, WINDOW_SIZE, SIGN_SIZE_H, SIGN_SIZE_V


def PIV_GAME_V(x): return x + WINDOW_SIZE[0] * 0.05 / 2
def PIV_GAME_H(x): return x + WINDOW_SIZE[1] * 0.05 / 2


class board:
  piv_tiles = [
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2),
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2)),
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2 + PIV_POINTS.PV_13_V.value),
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2)),
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2) + PIV_POINTS.PV_13_V.value*2,
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2)),
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2),
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2 + PIV_POINTS.PV_13_H.value)),
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2 + PIV_POINTS.PV_13_V.value),
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2 + PIV_POINTS.PV_13_H.value)),
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2) + PIV_POINTS.PV_13_V.value*2,
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2 + PIV_POINTS.PV_13_H.value)),
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2),
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2) + PIV_POINTS.PV_13_H.value*2),
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2 + PIV_POINTS.PV_13_V.value),
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2) + PIV_POINTS.PV_13_H.value*2),
      (PIV_GAME_V(PIV_POINTS.PV_13_V.value / 2 - SIGN_SIZE_V / 2) + PIV_POINTS.PV_13_V.value*2,
       PIV_GAME_H(PIV_POINTS.PV_13_H.value / 2 - SIGN_SIZE_H / 2) + PIV_POINTS.PV_13_H.value*2),
  ]
  lines = [
      pygame.Rect(
          PIV_POINTS.PV_13_V.value - LINE_WIDTH / 2,
          PIV_GAME_H(0),
          LINE_WIDTH,
          GAME_SIZE[1]),
      pygame.Rect(
          PIV_POINTS.PV_13_V.value*2 - LINE_WIDTH / 2,
          PIV_GAME_H(0),
          LINE_WIDTH,
          GAME_SIZE[1]
      ),
      pygame.Rect(
          PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value - LINE_WIDTH / 2,
          GAME_SIZE[0],
          LINE_WIDTH,
      ),
      pygame.Rect(
          PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value*2 - LINE_WIDTH / 2,
          GAME_SIZE[0],
          LINE_WIDTH,
      )
  ]
  fields = [
      pygame.Rect(
          PIV_GAME_V(0),
          PIV_GAME_H(0),
          PIV_POINTS.PV_13_V.value-PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value-PIV_GAME_V(0),
      ),
      pygame.Rect(
          PIV_POINTS.PV_13_V.value,
          PIV_GAME_H(0),
          PIV_POINTS.PV_13_V.value,
          PIV_POINTS.PV_13_H.value-PIV_GAME_V(0),
      ),
      pygame.Rect(
          PIV_POINTS.PV_13_V.value*2,
          PIV_GAME_H(0),
          PIV_POINTS.PV_13_V.value-PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value-PIV_GAME_V(0),
      ),
      pygame.Rect(
          PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value,
          PIV_POINTS.PV_13_V.value-PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value,
      ),
      pygame.Rect(
          PIV_POINTS.PV_13_V.value,
          PIV_POINTS.PV_13_H.value,
          PIV_POINTS.PV_13_V.value,
          PIV_POINTS.PV_13_H.value,
      ),
      pygame.Rect(
          PIV_POINTS.PV_13_V.value*2,
          PIV_POINTS.PV_13_H.value,
          PIV_POINTS.PV_13_V.value-PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value,
      ),
      pygame.Rect(
          PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value*2,
          PIV_POINTS.PV_13_V.value-PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value-PIV_GAME_V(0),
      ),
      pygame.Rect(
          PIV_POINTS.PV_13_V.value,
          PIV_POINTS.PV_13_H.value*2,
          PIV_POINTS.PV_13_V.value,
          PIV_POINTS.PV_13_H.value-PIV_GAME_V(0),
      ),
      pygame.Rect(
          PIV_POINTS.PV_13_V.value*2,
          PIV_POINTS.PV_13_H.value*2,
          PIV_POINTS.PV_13_V.value-PIV_GAME_V(0),
          PIV_POINTS.PV_13_H.value-PIV_GAME_V(0),
      ),
  ]

  def __init__(self, window):
    self.window = window

  def draw_self(self):
    self.window.fill(COLORS.D_GRAY.value)
    for line in self.lines:
      pygame.draw.rect(self.window, COLORS.RED.value, line)
    pygame.display.update()

  def _drawX(self, cords, hover=False):
    drawCol = COLORS.H_PING.value if hover else COLORS.L_PING.value
    pygame.draw.line(
        self.window,
        drawCol,
        [cords[0]-SIGN_SIZE_V*2, cords[1]-SIGN_SIZE_H*2],
        [cords[0]+SIGN_SIZE_V*2, cords[1]+SIGN_SIZE_H*2],
        SIGN_SIZE_V
    )
    pygame.draw.line(
        self.window,
        drawCol,
        [cords[0]+SIGN_SIZE_V*2, cords[1]-SIGN_SIZE_H*2],
        [cords[0]-SIGN_SIZE_V*2, cords[1]+SIGN_SIZE_H*2],
        SIGN_SIZE_V
    )

  def _drawO(self, cords, hover=False):
    color = COLORS.H_BLUE.value if hover else COLORS.F_BLUE.value
    pygame.draw.circle(self.window, color,
                       cords, SIGN_SIZE_V*2.5)
    pygame.draw.circle(self.window, COLORS.D_GRAY.value,
                       cords, SIGN_SIZE_V*2)

  def draw_tiles(self, tiles):
    self.window.fill(COLORS.D_GRAY.value)
    self.draw_self()

    for i in range(9):
      if(tiles[i] == 0):
        continue
      self._drawX(self.piv_tiles[i]) if tiles[i] == 1 else self._drawO(
          self.piv_tiles[i])
    pygame.display.update()
