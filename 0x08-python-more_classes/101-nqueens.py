#!/usr/bin/python3

"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.
"""

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 'Q':
                solution.append([r, c])
                break
    return solution

def xout(board, row, col):
    """X out spots on a chessboard where non-attacking queens can no longer be played."""
    n = len(board)
    for i in range(n):
        board[row][i] = 'x'  # X out row
        board[i][col] = 'x'  # X out column
        if row + i < n and col + i < n:
            board[row + i][col + i] = 'x'  # X out diagonal (down-right)
        if row - i >= 0 and col - i >= 0:
            board[row - i][col - i] = 'x'  # X out diagonal (up-left)
        if row + i < n and col - i >= 0:
            board[row + i][col - i] = 'x'  # X out diagonal (down-left)
        if row - i >= 0 and col + i < n:
            board[row - i][col + i] = 'x'  # X out diagonal (up-right)

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for col in range(n):
        if board[row][col] == ' ':
            tmp_board = [row[:] for row in board]  # Create a copy of the board
            tmp_board[row][col] = 'Q'  # Place a queen
            xout(tmp_board, row, col)  # X out spots on the board
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board_size = int(sys.argv[1])
    board = init_board(board_size)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
