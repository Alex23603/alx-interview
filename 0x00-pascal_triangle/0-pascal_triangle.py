#!/usr/bin/python3
"""
Module 0-pascal_triangle
Generates Pascal's triangle of a given size n.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle.
    :param n: size of Pascal's triangle (int)
    :return: List of lists of integers (Pascal's triangle)
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
