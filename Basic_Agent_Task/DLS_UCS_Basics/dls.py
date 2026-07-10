'''
Write a Python function to implement Depth-Limited Search (DLS) on a graph.
The function should determine if the goal node can be reached from the start node within a given depth limit.
'''
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': ['P'],
    'H': [],
    'P': []
}

def dls(start, goal, limit):
    frontier = [(start, 0)]   # (node, depth)
    
    while frontier:
        node, depth = frontier.pop()
        print("Node:", node, "Level:", depth)

        if node == goal:
            print("Goal Found.")
            return True
        
        if depth < limit:
            for child in reversed(graph[node]):
                frontier.append((child, depth + 1))
    
    print("Goal Not Found.")
    return False

dls('A', 'P', 3)