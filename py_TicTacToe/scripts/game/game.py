from enum import Enum


class GAME_STATES(Enum):
    GS_START = 0
    GS_TURN = 1
    GS_CHECK = 2
    GS_DRAW = 3
    GS_WIN = 4
    GS_END = 5


class Game:
  state = GAME_STATES.GS_START
  ended = False
  # 1 = x / 2 = o
  current_player = 1
  tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  winningTiles = []
  winOptions = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
  ]

  def nextState(self, state=True):
    if(state == True):
        self.state = GAME_STATES(self.state.value + 1)
    elif(isinstance(state, GAME_STATES)):
        self.state = state
    else:
        self.state = GAME_STATES(state)
    self.run()

  def ACTION_START(self):
    print('start')
    self.nextState()

  def ACTION_TURN(self):
    print('turn')
    #self.makeMove(1)

  def makeMove(self, tile):
    self.tiles[tile] = self.current_player
    self.nextState(GAME_STATES.GS_CHECK)

  def ACTION_CHECK(self):
    #print('check')
    for i in range(9):
      print(self.tiles[i], end='' if (i+1) % 3 != 0 else '\n')
    for option in self.winOptions:
      f1, f2, f3 = option
      if(self.tiles[f1] == self.tiles[f2] == self.tiles[f3] == self.current_player):
        self.winningTiles = option
        return self.nextState(GAME_STATES.GS_WIN)
    if(all(self.tiles)):
        return self.nextState(GAME_STATES.GS_DRAW)
    self.current_player = 1 if self.current_player == 2 else 2
    self.nextState(GAME_STATES.GS_TURN)

  def ACTION_DRAW(self):
    print('draw')
    self.nextState(GAME_STATES.GS_END)

  def ACTION_WIN(self):
    print('win')
    self.nextState(GAME_STATES.GS_END)

  def ACTION_END(self):
    print('end')
    self.ended = True
    return

  def run(self):
    game_actions = {
        0: self.ACTION_START,
        1: self.ACTION_TURN,
        2: self.ACTION_CHECK,
        3: self.ACTION_DRAW,
        4: self.ACTION_WIN,
        5: self.ACTION_END,
    }
    self.board.draw_tiles(self.tiles)
    game_actions.get(self.state.value)()

  def __init__(self, board):
    self.board = board
    self.run()
