import sys
from collections import deque

graph = list()
N,M,V = map(int,sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    m1,m2 = map(int,sys.stdin.readline().split())
    graph[m1][m2] = graph[m2][m1] = 1

def dfs(start_node):
    visited = list()
    answer = list()
    stack = list()

    stack.append(start_node)
    visited.append(start_node)

    while stack:
        node = stack.pop()
        answer.append(node)
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and (i not in visited):
                stack.append(i)
                visited.append(i)
                break
    return answer

def bfs(start_node):
    visited = list()
    answer = list()
    queue = deque()

    queue.append(start_node)
    visited.append(start_node)

    while queue:
        node = queue.popleft()
        answer.append(node)
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and (i not in visited):
                queue.append(i)
                visited.append(i)

    return answer

print(' '.join([str(a) for a in dfs(V)]))
print(' '.join([str(a) for a in bfs(V)]))