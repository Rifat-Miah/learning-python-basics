'''
Solve the graph by following UCS algorithm. Show the path and cost. 
graph = { 
'A': [('B', 1), ('C', 4)], 
'B': [('A', 1), ('C', 2), ('D', 5)], 
'C': [('A', 4), ('B', 2), ('D', 1)], 
'D': [('B', 5), ('C', 1)] 
}
'''

graph = { 
    'A': [('B', 1), ('C', 4)], 
    'B': [('A', 1), ('C', 2), ('D', 5)], 
    'C': [('A', 4), ('B', 2), ('D', 1)], 
    'D': [('B', 5), ('C', 1)] 
}

def ucs(start, goal):

    frontier = [(start, 0, [start])] # (Node, Cost, Path)

    explored = []

    while len(frontier) > 0:
        frontier.sort(key=lambda x: x[1])

        node, cost, path = frontier.pop(0)

        print("Visit:", node, "Cost:", cost)

        if node == goal:
            print("\nGoal Found.")
            print("Path:", " --> ".join(path))
            print("Total Cost: ", cost)
            return
        explored.append(node)

        for child, weight in graph[node]:
            if child not in explored:
                frontier.append((child, cost + weight, path + [child]))

    print("Goal Not Found.")

ucs('A', 'D')