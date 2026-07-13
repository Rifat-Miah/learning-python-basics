''' 1. Same as problem 1 but use A* search with the straight-line distance heuristic.
 When showing the frontier, include the f, g, and h score for each node.'''

graph = {
    'S' : [('A', 3), ('B', 2)],
    'A' : [('C', 4), ('D', 1)],
    'B' : [('E', 3), ('F', 1)],
    'C' : [],
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

def astar(start, goal):
    frontier = [(start, 0, [start])]  # (node, g, path)
    explored = []
    step = 1

    while frontier: 
        min_index = 0  # find node with smallest f = g + h

        for i in range(len(frontier)):
            node, g, path = frontier[i]
            best_node, best_g, best_path = frontier[min_index]

            if g + h[node] < best_g + h[best_node]:
                min_index = i
        
        node, g, path = frontier.pop(min_index)
        print("\nStep", step)
        print("Expand: ", node)

        explored.append(node)

        if node == goal:
                print("\nGoal Found!")
                print("Path: ", "--> ".join(path))
                print("Cost: ", g)
                print("Expanded Order: ", explored)
                return
        
        # Expand Children
        for child, cost in graph[node]:
             frontier.append((child, g + cost, path + [child]))
        
        # show Frontier
        print("Frontier: ")

        for node, g, path in frontier:
            print(node, "g = ", g, 
                  "h = ", h[node], 
                  "f = ", g + h[node])
        
        step += 1
astar("S", "G")


