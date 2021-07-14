import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    m1,m2 = map(int,sys.stdin.readline().split())
    graph[m1].append(m2)
    graph[m2].append(m1)

def dfs(start_node):
    visited = []
    stack = [start_node] # stack 초기값은 시작노드

    while stack:
        node = stack.pop() # 제일 위에 있는 값 pop해줌
        if node not in visited:
            visited.append(node) # 방문한 노드 체크
            stack.extend(sorted(list(set(graph[node])-set(visited)),reverse=True)) # list는 뺄셈 불가 -> set으로 처리, 정점 번호 작은 것부터 방문 -> reversed
    return visited


def bfs(start_node):
    visited = []
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(list(set(graph[node])-set(visited)))) # bfs -> queue여서 뒤에 정점들이 더 붙어도, 바로 인접했던 것들부터 방문함
    return visited

print(' '.join([str(a) for a in dfs(V)]))
print(' '.join([str(a) for a in bfs(V)]))

