#!/usr/bin/python3
"""a function that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    if grid is None:
        return 0

    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                if not x < 0 and grid[x-1][y] == 0:
                    perimeter += 1
                if not x > len(grid) - 1 and grid[x+1][y] == 0:
                    perimeter += 1
                if not y < 0 and grid[x][y-1] == 0:
                    perimeter += 1
                if not y > len(grid[0]) - 1 and grid[x][y+1] == 0:
                    perimeter += 1

    return perimeter
