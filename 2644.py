import sys
from collections import deque

n = int(sys.stdin.readline())
n1,n2 = map(int ,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(101)]
for _ in range(m):
    m1,m2 = map(int,sys.stdin.readline().split())
    graph[m1].append(m2)
    graph[m2].append(m1)

def bfs(n1):
    visited = [n1] # 시작 지점 방문 체크 해줘야 함
    queue = deque()
    queue.append(n1)
    cnt = 0
    while queue:
        node = queue.popleft()
        cnt += 1
        for i in range(len(graph[node])):
            tmp = graph[node][i]
            if tmp == n2: # 도착 지점 발견
                return cnt
            if tmp not in visited:
                visited.append(tmp)
                queue.append(tmp)
    return -1 # 찾지 못한 경우

print(bfs(n1))