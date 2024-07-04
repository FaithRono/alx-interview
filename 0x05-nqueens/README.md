## N-Queens Problem Solver
This Python script solves the classic N-Queens problem using a backtracking algorithm. The goal is to place N queens on an NxN chessboard such that no two queens threaten each other (i.e., they don’t share the same row, column, or diagonal).

####  Usage
Make sure you have Python 3 installed on your system.
Run the script with the desired value of N as a command-line argument.
                           python nqueens.py N
Replace N with the desired board size (e.g., 8 for an 8x8 chessboard).

##  Algorithm Explanation
1).Backtracking Approach:
---Start by placing queens one by one in different columns.
---For each column, explore all possible rows to place the queen.
---If a valid row is found, mark it as part of the solution.
---If no valid row is found, backtrack and try other rows.
2). Optimization:
---Utilizes properties of diagonals to reduce checks.
---The sum of row index and column index is constant for each right diagonal.
---The difference between row index and column index is constant for each left diagonal.
## Example Output
For N = 8, the script will find all distinct solutions and print the positions of queens on the chessboard.
