board = [6, 1, 10, 2,
         7, 11, 4, 14,
         5, 0, 9, 15,
         8, 12, 13, 3]
goal = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 0]

print("Initial State:")
for i in range(0, 16, 4):
    print(board[i:i+4])

inversion = 0

for i in range(len(board)):
    for j in range(i + 1, len(board)):
        if board[i] != 0 and board[j] != 0:
            if board[i] > board[j]:
                inversion += 1

print("\nInversion =", inversion)

blank_index = board.index(0)
blank_row = blank_index // 4
row_from_bottom = 4 - blank_row

print("Blank Row from Bottom =", row_from_bottom)

if (row_from_bottom % 2 == 0 and inversion % 2 == 1) or \
   (row_from_bottom % 2 == 1 and inversion % 2 == 0):

    print("\nPuzzle is Solvable")

    print("\nGoal State:")
    for i in range(0, 16, 4):
        print(goal[i:i+4])

else:
    print("\nPuzzle is Not Solvable")