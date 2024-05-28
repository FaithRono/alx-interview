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

    for integer in range(1, n):
        pascal_row = [1]  # Start each row with a 1
        for j in range(1, integer):
            # Compute the value based on the two values above it
            pascal_row.append(pascal_triangle[integer - 1][j - 1] + pascal_triangle[integer - 1][j])
        pascal_row.append(1)  # End each row with a 1
        pascal_triangle.append(pascal_row)  # Add the row to the triangle

    return pascal_triangle
