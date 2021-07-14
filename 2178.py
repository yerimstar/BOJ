# 미로 탐색
import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0] #상하좌우 표현
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) # 시작지점
    while queue:
        x,y = queue.popleft()
        for i in range(4): # 상하좌우 탐색
            tx = x+dx[i]
            ty = y+dy[i]
            if tx < 0 or N <= tx or ty < 0 or M <= ty: # N X M안에 존재해야 함
                continue
            if graph[tx][ty] == 0: # 0값이라면 지나갈 수 없음
                continue
            if graph[tx][ty] == 1:
                graph[tx][ty] = graph[x][y] + 1 # tx,ty까지 이동한 최단거리값 저장
                queue.append((tx,ty))
    return graph[N-1][M-1] # 마지막 칸의 최단경로 값 반환

print(bfs(0,0))