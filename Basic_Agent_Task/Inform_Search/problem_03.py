'''
3. Using this graph, search for the path to G from S using greedy best first tree search.
'''

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

def greedy(start, goal):
    frontier = [(start, [start])]
    expanded = []
    step = 1

    while frontier:
        min_index = 0

        for i in range(len(frontier)):
            node, path = frontier[i]
            best_node, best_path = frontier[min_index]

            if h[node] < h[best_node]:
                min_index = i

        node, path = frontier.pop(min_index)

        print("\nStep", step)
        print("Expand: ", node)

        expanded.append(node)

        if node == goal:
            print("\nGoal Found!")
            print("Path: ", "--> ".join(path))
            print("Expanded Order: ", expanded)
            return
        
        # Expand children 
        for child, cost in graph[node]:
            frontier.append((child, path + [child]))

        # show frontier
        print("Frontier: ")
        for n, p in frontier:
            print(n, "h = ", h[n])
        step += 1

    print("Goal Not Found.")

greedy("S", "G") 