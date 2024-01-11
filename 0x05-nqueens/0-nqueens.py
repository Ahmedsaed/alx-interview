#!/usr/bin/python3
"""A program to final all solutions to the nqueens problem"""


def nqueens(n):
    """A function to find all solutions to the nqueens problem"""
    if type(n) is not int:
        raise TypeError("n must be a positive integer")
    if n < 4:
        raise ValueError("n must be at least 4")
    board = [[0 for x in range(n)] for y in range(n)]
    solve(board, 0, n)


def solve(board, col, n):
    """A recursive function to solve the nqueens problem"""
    if col == n:
        print_board(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve(board, col + 1, n) or res
            board[i][col] = 0
    return res


def is_safe(board, row, col, n):
    """A function to check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < n:
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1
    return True


def print_board(board):
    """A function to print the board"""
    print("[", end="")
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end="")
                if i != len(board) - 1:
                    print(", ", end="")
    print("]")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    n = sys.argv[1]

    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(int(sys.argv[1]))
