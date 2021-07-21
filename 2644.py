# 촌수 계산
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

def bfs(start,end):
    visited = [start] # 시작 지점 방문 체크 해줘야 함
    queue = deque()
    cnt = 1
    queue.append([start,cnt]) # 해당 지점까지 촌수 저장

    while queue:
        node,cnt = queue.popleft()
        for i in range(len(graph[node])):
            tmp = graph[node][i]
            if tmp == end: # 도착 지점 발견
                return cnt
            if tmp not in visited:
                visited.append(tmp)
                queue.append([tmp,cnt+1])

    return -1 # 찾지 못한 경우

print(bfs(n1,n2))