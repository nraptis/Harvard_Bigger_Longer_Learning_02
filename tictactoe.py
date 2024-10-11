"""
Tic Tac Toe Player
"""

import copy
import math

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
    x_count = 0
    o_count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                x_count += 1
            if board[i][j] == O:
                o_count += 1
    if o_count < x_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                res.append((i, j))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] < 0 or action[0] > 2:
        raise IndexError
    if action[1] < 0 or action[1] > 2:
        raise IndexError
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError
    res = copy.deepcopy(board)
    res[action[0]][action[1]] = player(board)
    #print("applied ", action, " for ", player(board), "to ", board, " and got ", res)
    return res

def any_row_matches(board, symbol):
    for j in range(0, 3):
        if board[j][0] == symbol and board[j][1] == symbol and board[j][2] == symbol:
            return True
    return False

def any_column_matches(board, symbol):
    for i in range(0, 3):
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    return False

def any_diagonal_matches(board, symbol):
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol:
        return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if any_row_matches(board, X):
        return X
    if any_column_matches(board, X):
        return X
    if any_diagonal_matches(board, X):
        return X
    if any_row_matches(board, O):
        return O
    if any_column_matches(board, O):
        return O
    if any_diagonal_matches(board, O):
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == EMPTY:
                    return False
        return True
    else:
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    _winner = winner(board)
    if _winner == X:
        return 1
    elif _winner == O:
        return -1
    else:
        return 0

best_action = (-1, -1)

def min_value(board, depth):
    global best_action
    if terminal(board):
        return utility(board)
    v = 1000
    for action in actions(board):
        new_board = result(board, action)
        new_value = max_value(new_board, depth + 1)
        if new_value < v:
            v = new_value
            if depth == 0:
                best_action = action
                print("New Best Movie For O: ", action, " Value Was ", v)
    return v

def max_value(board, depth):
    global best_action
    if terminal(board):
        return utility(board)
    v = -1000
    for action in actions(board):
        new_board = result(board, action)
        new_value = min_value(new_board, depth + 1)
        if new_value > v:
            v = new_value
            if depth == 0:
                best_action = action
                print("New Best Movie For X: ", action, " Value Was ", v)
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global best_action
    best_action = (-1, -1)
    _player = player(board)
    if _player == X:
        max_value(board, 0)
    elif _player == O:
        min_value(board, 0)
    print("best_action = ", best_action)
    return best_action
