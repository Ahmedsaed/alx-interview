#!/usr/bin/python3
"""A program to rotate a 2d matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """A function to rotate a 2d matrix 90 degrees clockwise"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0:
        return
    if len(matrix) != len(matrix[0]):
        raise TypeError("matrix must be a square matrix")
    n = len(matrix)
    for x in range(int(n / 2)):
        for y in range(x, n - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]
            matrix[y][n - 1 - x] = temp
