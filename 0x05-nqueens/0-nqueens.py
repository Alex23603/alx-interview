#!/usr/bin/python3
import sys

def print_solution(board):
    """Helper function to format and print the solution."""
    solution = [[row, col] for row, col in enumerate(board)]
    print(solution)

def is_safe(board, row, col):
    """Check if a queen can be placed at board[row] = col without conflicts."""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(board, row, n):
    """Recursive function to solve N-Queens using backtracking."""
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1  # Reset (backtrack)

def main():
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board with -1, representing empty spaces
    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()
