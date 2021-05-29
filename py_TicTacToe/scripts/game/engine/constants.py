from enum import Enum, IntEnum

# MOST OTHER CONSTANTS ARE RELATIVE
WINDOW_SIZE = (500, 500)


class COLORS(Enum):
  D_GRAY = (40, 61, 59)
  F_BLUE = (25, 114, 120)
  H_BLUE = (45, 125, 150)
  L_PING = (207, 191, 182)
  H_PING = (237, 221, 212)
  RED = (196, 69, 54)
  D_RED = (119, 46, 37)
  ORANGE = (255, 82, 27)


GAME_SIZE = (int(WINDOW_SIZE[0] * 0.95), int(WINDOW_SIZE[1] * 0.95))
LINE_WIDTH = int(WINDOW_SIZE[0] * 0.02)
SIGN_SIZE_V = int(WINDOW_SIZE[0] * 0.05)
SIGN_SIZE_H = int(WINDOW_SIZE[1] * 0.05)


class PIV_POINTS(IntEnum):
    PV_13_V = int(WINDOW_SIZE[0] / 3)
    PV_13_H = int(WINDOW_SIZE[1] / 3)
