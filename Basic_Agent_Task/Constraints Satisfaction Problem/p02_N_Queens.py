N = 5
board = [-1] * N
def safe(row, col):
    for r in range(row):
        c = board[r]
        if c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True
def solve(row):
    if row == N:
        return True
    for col in range(N):
        if safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1
    return False
solve(0)
for row in range(N):
    for col in range(N):
        if board[row] == col:
            print("Q", end=" ")
        else:
            print(".", end=" ")

    print()