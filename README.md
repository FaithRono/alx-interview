Pascal's Triangle
Description
A Python function pascal_triangle(n) that returns a list of lists of integers representing Pascal’s Triangle up to the nth row.
Features
Generates Pascal's Triangle up to the specified number of rows.
Each row starts and ends with 1.
Intermediate values are calculated based on the sum of two values directly above.
Usage
Input: An integer n representing the number of rows.
Output: A list of lists, where each inner list represents a row in Pascal's Triangle.
Example
For n = 5, the function returns:
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
Notes
Returns an empty list if n <= 0.
Iterates inclusively to compute the values of each row.
Running the Script
Ensure the script has executable permissions.
Run the script using Python.