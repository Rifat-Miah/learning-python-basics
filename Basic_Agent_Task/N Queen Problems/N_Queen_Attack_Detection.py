queens = [(4,4), (2,2), (2,2), (3,4)]

attack = False

for i in range(len(queens)):
    for j in range(i + 1, len(queens)):

        r1, c1 = queens[i]
        r2, c2 = queens[j]

        if r1 == r2:
            print("Row Attack:", queens[i], queens[j])
            attack = True

        elif c1 == c2:
            print("Column Attack:", queens[i], queens[j])
            attack = True

        elif abs(r1 - r2) == abs(c1 - c2):
            print("Diagonal Attack:", queens[i], queens[j])
            attack = True

if attack == False:
    print("No Queen Attack")