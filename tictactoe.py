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
    if board == initial_state():
        return X
    turns = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is not EMPTY:
                turns += 1
    if (turns % 2 == 0):
        return X
    else: 
        return O
  

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j]) is EMPTY:
                actions.add( (i, j) )
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid Move")
    board_copy = deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3): 
        if (board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY): #horizontal
            if board[0][i] == X:
                return X
            else:
                return O 
        elif (board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY): #vertical 
            if board[i][0] == X:
                return X
            else:
                return O
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY ):  #diagonal L to R
        if board[0][0] == X:
                return X
        else:
            return O
    elif (board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY):  #diagonal R to L
        if board[0][2] == X:
                return X
        else:
            return O
    else: 
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X or winner(board) == O):
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        return maxVal(board, float("-inf"), float("inf"))[1]
    else:
        return minVal(board, float("-inf"), float("inf"))[1]

def maxVal(board, maxi, mini):
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    optmove = None
    for action in actions(board):
        vv = minVal(result(board, action), maxi, mini)[0]
        maxi = max(maxi, vv)
        if vv > v:
            v = vv
            optmove = action
        if maxi >= mini:
            break
    return [v, optmove]

def minVal(board, maxi, mini):
    if terminal(board):
        return [utility(board), None]
    v = float('inf')
    optmove = None
    for action in actions(board):
        vv = maxVal(result(board, action), maxi, mini)[0]
        mini = min(mini, vv)
        if v > vv:
            v = vv
            optmove = action
        if maxi >= mini:
            break
    return [v, optmove]

