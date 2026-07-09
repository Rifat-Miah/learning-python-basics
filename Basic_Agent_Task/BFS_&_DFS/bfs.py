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

def bfs(start, goal):
    node = start
    
    if node == goal:
        return node
    
    frontier = [node]
    reached = [node]

    while len(frontier) != 0:
        node = frontier.pop(0)
        print(node, end=" ")

        for child in graph[node]:
            if child == goal:
                print(child) 
                return
            
            if child not in reached:
                reached.append(child)
                frontier.append(child)
    return "Failure"

bfs("A", "p")
            