#!/usr/bin/env python3

# Import the sys module to handle command-line arguments
import sys


# Define a function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Return True if no queens are attacking the position
    return True


# Define a utility function to solve the N Queens problem
def solve_nqueens_util(board, col, solutions):
    """Utilize backtracking to find all solutions."""

    # If all queens are placed, add the solution to the list
    if col >= len(board):
        # Create a list to store the current solution
        solution = []
        # Iterate through the board to find the positions of the queens
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        # Append the current solution to the solutions list
        solutions.append(solution)
        return True

    # Initialize result as False
    res = False
    # Try placing a queen in all rows one by one
    for i in range(len(board)):
        # Check if it's safe to place the queen at board[i][col]
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1
            # Recur to place the rest of the queens
            res = solve_nqueens_util(board, col + 1, solutions) or res
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen (backtrack)
            board[i][col] = 0

    # Return result
    return res


# Define a function to solve the N Queens problem
def solve_nqueens(N):
    """Solve the N Queens problem and print all solutions."""

    # Initialize the chessboard with 0s
    board = [[0 for _ in range(N)] for _ in range(N)]
    # Initialize the list to store solutions
    solutions = []
    # Call the utility function to solve the problem
    solve_nqueens_util(board, 0, solutions)
    # Print all solutions
    for solution in solutions:
        print(solution)


# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        # Print usage information and exit with status 1
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Try to convert the argument to an integer
        N = int(sys.argv[1])
    except ValueError:
        # Print an error message if the argument is not an integer
        print("N must be a number")
        sys.exit(1)

    # Check if the integer is at least 4
    if N < 4:
        # Print an error message if N is less than 4
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(N)
