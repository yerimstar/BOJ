# 상범 빌딩
import sys
from collections import deque

def bfs(z,x,y):
    q = deque()
    q.append([z,x,y])
    visited[z][x][y] = 1 # 방문처리
    while q:
        z,x,y = q.popleft()
        for mz,mx,my in move:
            dz = z + mz
            dx = x + mx
            dy = y + my
            if 0 <= dz < l and 0 <= dx < r and 0 <= dy < c: # 범위 체크
                if not visited[dz][dx][dy]:
                    if graph[dz][dx][dy] == '.': # 비어 있는 곳이라면
                        visited[dz][dx][dy] = visited[z][x][y] + 1 # 이동
                        q.append([dz,dx,dy])
                    elif graph[dz][dx][dy] == 'E': # 탈출
                        visited[dz][dx][dy] = visited[z][x][y] + 1
                        return

move = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]] # 동서남북상하

while True:
    l, r, c = map(int, sys.stdin.readline().split())
    if l == 0 and r == 0 and c == 0: # 종료 조건
        break
    graph = [[]for _ in range(l)]
    visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    for i in range(l):
        for j in range(r+1):
            tmp = list(sys.stdin.readline().strip()) # 한 층마다 빈 줄이 있음
            if len(tmp) != 0: # 빈 줄이 아니라면
                graph[i].append(tmp)
                for k in range(c):
                    if tmp[k] == 'S': # 시작
                        sz,sx,sy = i,j,k
                    elif tmp[k] == 'E': # 탈출
                        ez,ex,ey = i,j,k

    bfs(sz,sx,sy)
    if visited[ez][ex][ey] != 0: # 탈출 가능
        print("Escaped in " + str(visited[ez][ex][ey]-1) + " minute(s).")
    else: # 탈출 불가능
        print("Trapped!")