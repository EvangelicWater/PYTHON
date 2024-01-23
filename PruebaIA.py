class TicTacToe:
  def __init__(self):
    self.board = [[' ' for i in range(3)] for j in range(3)]
    self.turn = 'X'
    self.winner = None
    self.draw = False
    self.game_over = False
  def move(self, x, y):
    if self.game_over:
      return
    if self.board[x][y] != ' ':
      return
    self.board[x][y] = self.turn
    if self.turn == 'X':
      self.turn = 'O'
    else:
      self.turn = 'X'
    self.check_winner()
    self.check_draw()
  def check_winner(self):
    for i in range(3):
      if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
        self.winner = self.board[i][0]
        self.game_over = True
      if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
        self.winner = self.board[0][i]
        self.game_over = True
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
      self.winner = self.board[0][0]
      self.game_over = True
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
      self.winner = self.board[0][2]
      self.game_over = True
  def check_draw(self):
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == ' ':
          return
    self.draw = True
    self.game_over = True
