import sys
from collections import deque

n = int(sys.stdin.readline())
num1,num2 = map(int ,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    m1,m2 = map(int,sys.stdin.readline().split())
    graph[m1].append(m2)
    graph[m2].append(m1)
print(graph)

def check(start_node):
    visited = list()
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        print("node = ",node)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])



print(check(num1))