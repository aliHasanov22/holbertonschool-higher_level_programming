#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]"""
    for i in range(row):
        # Check column
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Backtracking function to find all solutions"""
    if row == n:
        # Format the solution: [[row, col], ...]
        res = [[i, board[i]] for i in range(n)]
        solutions.append(res)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            # Backtrack happens naturally as we overwrite board[row]


def main():
    # 1. Argument validation
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

    # 2. Solve the problem
    solutions = []
    # board[i] will store the column index for row i
    board = [0] * n
    solve_nqueens(n, 0, board, solutions)

    # 3. Print results
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
