#!/usr/bin/python3
"""Find all valid solutions for the N Queens problem."""
import sys


def solve_nqueens(n):
    """Print all arrangements of N non-attacking queens."""
    positions = []
    columns = set()
    diagonals_one = set()
    diagonals_two = set()

    def backtrack(row):
        """Place one queen in each row using backtracking."""
        if row == n:
            print(positions[:])
            return

        for col in range(n):
            if (col in columns or row - col in diagonals_one or
                    row + col in diagonals_two):
                continue

            positions.append([row, col])
            columns.add(col)
            diagonals_one.add(row - col)
            diagonals_two.add(row + col)

            backtrack(row + 1)

            positions.pop()
            columns.remove(col)
            diagonals_one.remove(row - col)
            diagonals_two.remove(row + col)

    backtrack(0)


if __name__ == "__main__":
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

    solve_nqueens(n)
