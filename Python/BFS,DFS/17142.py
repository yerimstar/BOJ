# 연구소 3
import sys
from collections import deque
from itertools import combinations

def bfs(v):
    visited = [[0 for _ in range(n)] for _ in range(n)] # 방문처리
    q = deque()
    tmp_graph = [x[:] for x in graph] # graph 복제

    for x,y,t in v: # 바이러스
        q.append([x,y,t])
        visited[x][y] = 1

    cnt = 0 # 시간 체크
    while q:
        x,y,c = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < n: # 범위 체크
                if not visited[dx][dy] and tmp_graph[dx][dy] != 1: # 아직 방문하지 않은 곳 + 벽이 아닌 곳 탐색
                    visited[dx][dy] = 1 # 방문처리
                    if tmp_graph[dx][dy] == 0: # 빈 공간이라면 바이러스 전염 가능
                        tmp_graph[dx][dy] = 2 # 바이러스 전염
                        cnt = c + 1 # 바이러스 전염되었으므로 시간 추가
                    q.append([dx,dy,c + 1]) # 비활성 바이러스여도 시간은 추가되어야 함
    check = 0
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] == 0: # 비어있는 공간이 하나라도 있는지 체크하기 위함
                check += 1
    if check > 0: # 빈 공간이 있다면
        return -1
    else:
        return cnt

n,m = map(int,sys.stdin.readline().split())
graph = []
virus = []
empty = 0
move = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if tmp[j] == 2: # 바이러스 체크
            virus.append([i,j,0])
        elif tmp[j] == 0: # 빈공간 체크
            empty += 1
    graph.append(tmp)

virus_lst = list(combinations(virus,m)) # 조합으로 바이러스 위치 결정
result = 10**6

if empty == 0: # 빈공간이 하나도 없다면 바이러스 전염 불가
    result = 0
else:
    for v in virus_lst:
        cnt = bfs(v)
        if cnt != -1:
            result = min(result,cnt)
if result == 10**6:
    result = -1
print(result)
