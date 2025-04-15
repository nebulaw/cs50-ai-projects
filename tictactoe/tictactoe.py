"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
  """
  Returns starting state of the board.
  """
  return [[EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

def player(board):
  """
  Returns player who has the next turn on a board.
  """
  if not board: raise ValueError("Board is empty")

  x_count, o_count = 0, 0
  for row in board:
    for cell in row:
      if cell == X: x_count += 1
      elif cell == O: o_count += 1
  # X always starts first
  return O if x_count > o_count else X

def actions(board):
  """
  Returns set of all possible actions (i, j) available on the board.
  """
  if not board: raise ValueError("Board is empty")

  actions = set()
  for i, row in enumerate(board):
    for j, cell in enumerate(row):
      if cell == EMPTY:
        actions.add((i, j))
  return actions

def result(board, action):
  """
  Returns the board that results from making move (i, j) on the board.
  """
  if not (board and action): return None

  # unpack action
  i, j = action
  if board[i][j] != EMPTY: raise ValueError("Invalid action")

  # create a copy of the board and update the cell
  result_board = deepcopy(board)
  result_board[i][j] = player(board)
  return result_board

def winner(board):
  """
  Returns the winner of the game, if there is one.
  """
  # brute force the states

  # check horizontal rows
  for row in board:
    if row[0] is not EMPTY and row[0] == row[1] == row[2]: return row[0]
  # check vertical columns 
  for j in range(3):
    if board[0][j] is not EMPTY and board[0][j] == board[1][j] == board[2][j]: return board[0][j]
  # check diagonals
  if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]: return board[0][0]
  if board[0][2] is not EMPTY and board[0][2] == board[1][1] == board[2][0]: return board[0][2]
  # otherwise we have no winner
  return None

def terminal(board):
  """
  Returns True if game is over, False otherwise.
  """
  if not board: raise ValueError("Board is empty")
  return winner(board) or not actions(board)

def utility(board):
  """
  Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
  """
  if not board: raise ValueError("Board is empty")
  w = winner(board)
  if w == X: return 1
  elif w == O: return -1
  return 0

def minimax(board):
  """
  Returns the optimal action for the current player on the board.
  """
  # check if board has a winner
  if terminal(board): return None

  # auxiliary functions to compute the minimax value
  def minval(board):
    # if game is over, return the utility
    if terminal(board): return utility(board)
    val = math.inf
    # iterate over possible actions
    for action in actions(board):
      # compute the value of the result board after
      # the action and find the minimum one
      val = min(val, maxval(result(board, action)))
    return val
  
  def maxval(board):
    if terminal(board): return utility(board)
    val = -math.inf
    for action in actions(board):
      val = max(val, minval(result(board, action)))
    return val

  # get the best possible action
  current_player = player(board)
  best_action = None

  # maximize value if current player is X
  # otherwise minimize value
  if current_player == X:
    mval = -math.inf
    # iterate over actions and find the action which has
    # the highest value matched with the best action
    for action in actions(board):
      val = minval(result(board, action))
      if val > mval:
        mval = val
        best_action = action
  else:
    mval = math.inf
    # iterate over actions and find the action which has
    # the minimum value matched with the best action
    for action in actions(board):
      val = maxval(result(board, action))
      if val < mval:
        mval = val
        best_action = action

  return best_action

