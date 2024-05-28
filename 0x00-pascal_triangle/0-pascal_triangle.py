#!/usr/bin/python3
"""a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:"""


def pascal_triangle(n):
    """a pascals triangle is has rows of integers,it doesn't contain a 0 or a neg number,
    the first row begins with 1 and the last row ends with 1, iteration occurs inclusively
    so as to compute the middle values of a row

    Args:
        n (int): n is the number of rows to be generated for the pascals triangle

    Returns:
       List[List[int]]: returns a list of lists of integers representing the Pascal’s triangle of n
    """
    #check if n is less than 0 or equal then return an empty list
    if n <= 0:
        return []
    
    # Initialize an empty list to store the rows of Pascal's Triangle
    pascal_triangle = [[1]]
    
    #BUILDING EACH ROW OF A PASCAL TRIANGLE
    # Iterate over the range of n inclusively(n-1) to generate each row
    for integer in range(1, n):
        # Initialize the first row with a single 1, every row in a pascals start with 1
        first_row = [1]
        # If there's a previous row in the triangle
        if pascal_triangle:
            # Get the last row of the triangle
            last_row = pascal_triangle[-1]
            # Calculate the middle values of the current row based on the last row
            for j in range(1, integer):
                first_row.append(last_row[j - 1] + last_row[j])
            # End the current row with a 1
            first_row.append(1)
        
        # Add the current row to the triangle
        pascal_triangle.append(first_row)
    
    # Return the completed Pascal's Triangle
    return pascal_triangle

