"""
Tic Tac Toe Player
"""

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
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError

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

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if any_row_matches(board, X):
        print("matched x on row")
        return 1
    if any_column_matches(board, X):
        print("matched x on column")
        return 1
    if any_diagonal_matches(board, X):
        print("matched x on diagonal")
        return 1
    if any_row_matches(board, O):
        print("matched o on row")
        return -1
    if any_column_matches(board, O):
        print("matched o on column")
        return -1
    if any_diagonal_matches(board, O):
        print("matched o on diagonal")
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

board = initial_state()
print(board)

board[0][0] = X
print(board)
board[1][1] = X
print(board)
board[2][2] = X
print(board)



_player = player(board)
print(_player)

print(utility(board))

#board[0][2] = O
#print(board)


