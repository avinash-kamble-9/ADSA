def is_safe(board, row, col, N):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queen(board, row, N, solutions):
    # Base case: all queens placed
    if row == N:
        # Convert board into a readable format
        solution = ["".join("Q" if x == 1 else "." for x in r) for r in board]
        solutions.append(solution)
        return

    # Try placing queen in each column
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queen(board, row + 1, N, solutions)
            board[row][col] = 0  # Backtrack


# ---- Main Program ----
if __name__ == "__main__":
    N = int(input("Enter number of Queens (N): "))
    board = [[0] * N for _ in range(N)]
    solutions = []

    solve_n_queen(board, 0, N, solutions)

    if not solutions:
        print(f"No solution exists for N = {N}")
    else:
        print(f"Total solutions for N = {N}: {len(solutions)}\n")
        for idx, sol in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            for row in sol:
                print(row)
            print()
