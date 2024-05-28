#!/usr/bin/python3
"""0. Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    pascal_triangle = [[1]]  # Initialize the first row of the triangle

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Compute the value based on the two values above it
            row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
        row.append(1)  # End each row with a 1
        pascal_triangle.append(row)  # Add the row to the triangle

    return pascal_triangle
