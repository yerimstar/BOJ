import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M): # 구글링 도움 받음...
    m1,m2 = map(int,sys.stdin.readline().split())
    graph[m1].append(m2)
    graph[m2].append(m1)
    graph[m1].sort()
    graph[m2].sort()

def dfs(start_node):
    visited = []
    answer = []
    stack = [start_node] # stack 초기값은 시작노드

    while stack:
        node = stack.pop() # 제일 위에 있는 값 pop해줌
        if node not in visited:
            visited.append(node) # 방문한 노드 체크
            answer.append(node) # 답 출력용
            stack.extend(reversed(list(set(graph[node])-set(visited)))) # list는 뺄셈 불가 -> set으로 처리, 정점 번호 작은 것부터 방문 -> reversed
        if len(visited) == N: # 정점 개수와 방문 개수가 동일해지면 멈춤
            break
    return answer


def bfs(start_node):
    visited = []
    answer = []
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            answer.append(node)
            queue.extend(list(set(graph[node])-set(visited))) # bfs -> queue여서 뒤에 정점들이 더 붙어도, 바로 인접했던 것들부터 방문함
        if len(answer) == N:
            break
    return answer

print(' '.join([str(a) for a in dfs(V)]))
print(' '.join([str(a) for a in bfs(V)]))

