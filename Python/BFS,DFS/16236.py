# 아기 상어
import sys
from collections import deque
def bfs(sx,sy):
    visited = [[0 for _ in range(N)] for _ in range(N)] # 방문처리
    distance = [[0 for _ in range(N)] for _ in range(N)] # 거리(시간) 체크
    q = deque()
    q.append([sx,sy])
    visited[sx][sy] = 1
    tmp = []
    while q:
        x,y = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < N and 0 <= dy < N:
                if not visited[dx][dy] and graph[dx][dy] <= ssize: # 아직 방문하지 않은 곳이면서 상어가 지나갈 수 있는 곳
                    distance[dx][dy] = distance[x][y] + 1 # 거리(시간) 업데이트
                    visited[dx][dy] = 1 # 방문처리
                    q.append([dx,dy])
                    if 0 < graph[dx][dy] < ssize: # 상어가 먹을 수 있는 물고기
                        tmp.append([distance[dx][dy],dx,dy])
    return sorted(tmp,key = lambda x : (-x[0],-x[1],-x[2])) # 가장 거리가 짧은 것, 가장 위쪽, 가장 왼쪽

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    graph.append(tmp)
    for j in range(N):
        if tmp[j] == 9: # 아기 상어 초기 위치 파악
            sx,sy = i,j

ssize = 2 # 아기 상어 초기 사이즈
t = 0
cnt = 0
move = [[-1,0],[0,-1],[1,0],[0,1]]
while(1):
    tmp = bfs(sx,sy)
    if len(tmp) == 0:
        break
    distance,x,y = tmp.pop()
    graph[sx][sy] = 0 # 아기 상어 위치 0으로 초기화
    graph[x][y] = 0 # 물고기 먹은 위치 0으로 초기화
    sx,sy = x,y # 아기 상어 위치 변경 (물고기 먹은 곳)
    cnt += 1 # 상어 크기랑 같은 수만큼 물고기를 먹으면 사이즈 업
    t += distance # distance값이 상어 위치에서 물고기를 잡아먹은 위치까지의 거리를 의미함
    if cnt == ssize:
        ssize += 1
        # 횟수 초기화
        cnt = 0
print(t)