# 연구소
"""
1. 벽 3개 세우기
2. 바이러스 확산
3. 안전영역 최댓값 갱신
BFS,DFS / DFS 활용해야 할 것 같음
"""
import copy
import sys
from collections import deque

def bfs():
    global result
    map_copy = copy.deepcopy(tmp)
    for i in range(n):
        for j in range(m):
            if map_copy[i][j] == 2:
                dq.append([i,j])
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 범위안에 있는지 체크
                if map_copy[nx][ny] == 0: # 값이 0이라면 바이러스 전염됨
                    map_copy[nx][ny] = 2
                    dq.append([nx,ny])
    cnt = 0
    for data in map_copy:
        cnt += data.count(0) # 안전영역(0인 값) 체크
    result = max(result,cnt) # 값 비교 후 최댓값으로 업데이트

def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                tmp[i][j] = 1
                wall(x+1)
                tmp[i][j] = 0

# 방향 값
dx = [0, 0, 1, -1]
dy = [1, -1, 0 , 0]

n,m = map(int,sys.stdin.readline().split())
tmp = []
dq = deque()
# 지도 만들기
for _ in range(n):
    tmp.append(list(map(int, sys.stdin.readline().split())))

result = 0
wall(0)
print(result)