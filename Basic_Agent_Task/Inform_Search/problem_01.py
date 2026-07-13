# 1. Show the frontier after each step, the order of expanded nodes, and the solution found. 

graph = {
    'S' : [('A', 3), ('B', 2)],
    'A' : [('C', 4), ('D', 1)],
    'B' : [('E', 3), ('F', 1)],
    'c' : [],
    'D' : [],
    'E' : [('H', 5)],
    'F' : [('I', 2), ('G', 3)],
    'H' : [],
    'I' : [],
    'G' : []
}

h = {
    'A' : 12,
    'B' : 4,
    'C' : 7,
    'D' : 3,
    'E' : 8,
    'F' : 2,
    'H' : 4,
    'I' : 9,
    'S' : 13,
    'G' : 0
}

def gbfs(start, goal):
    frontier = [(start, [start])]
    explored = []
    step = 1


    while frontier:
        min_index = 0
        for i in range(len(frontier)):
            if h[frontier[i][0]] < h[frontier[min_index][0]]:
                min_index = i

        node, path = frontier.pop(min_index)
        print("\nStep", step)
        print("Expand: ", node)

        explored.append(node)

        if node == goal:
            print("\nGoal Found!")
            print("Path: ", "--> ".join(path))
            print("Expanded Order: ", explored)
            return
        
        for child, cost in graph[node]:
            frontier.append((child, path + [child]))
        print("Frontier: ")

        for n, p in frontier:
            print(n, "h = ", h[n])

        step += 1
gbfs("S", "G")