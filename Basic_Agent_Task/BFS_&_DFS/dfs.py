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

def dfs(start, goal):
    stack = [start]

    while len(stack) != 0:
        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            return "Success" 
        
        for child in reversed(graph[node]):
            stack.append(child)
        
    return "Failure"

print(dfs("A", "P"))
dfs("A", "P")