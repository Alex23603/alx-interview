#!/usr/bin/python3
"""
Calculate the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of ints): A 2D list representation of the grid
                                      where 0 = water, 1 = land.

    Returns:
        int: Perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check top
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check right
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
