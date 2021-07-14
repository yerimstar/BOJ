from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def bfs(graph, start_node):
    visit = list()
    queue = deque()

    queue.append(start_node)

    while queue:
        node = queue.popleft()
        print(node)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

print(bfs(graph,'A'))