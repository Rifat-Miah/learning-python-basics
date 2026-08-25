#Problem 1. (Map Coloring)
colors = ["blue", "green", "red"]
neighbors = {
    0: [1, 4, 5],
    1: [0, 3, 4],
    2: [3, 4],
    3: [1, 2],
    4: [0, 1, 2, 5],
    5: [0, 4]
}
assignment = {}
solutions = []
def is_valid(territory, color):

    for neighbor in neighbors[territory]:

        if neighbor in assignment:

            if assignment[neighbor] == color:
                return False

    return True

def solve(territory):

    if territory == 6:
        solutions.append(assignment.copy())
        return

    for color in colors:

        if is_valid(territory, color):

            assignment[territory] = color
            solve(territory + 1)
            del assignment[territory]

solve(0)

print("Total Solutions:", len(solutions))
print()

for i, solution in enumerate(solutions, 1):
    print("Solution", i, ":")

    for territory in range(6):
        print(territory, "=", solution[territory])

    print()