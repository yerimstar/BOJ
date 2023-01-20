# 감시피하기
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dq = deque()
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().split()))

def bfs():
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'T':
                dq.append((i,j))
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            tx,ty = x,y
            while True:
                nx = tx + dx[i]
                ny = ty + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
            #         if graph[nx][ny] == 'X' and visited[nx][ny] == False:
            #             visited[nx][ny] = True
            #         elif graph[nx][ny] == 'S':
            #             return False
            #         elif graph[nx][ny] == 'O':
            #             break
            #         tx, ty = nx, ny
            #     else:
            #         break
            # return True

def recursive(index):
    global check
    if index == 3:
        if bfs():
            check = True
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                recursive(index + 1)
                graph[i][j] = 'X'


recursive(0)
if check:
    print("YES")
else:
    print("NO")
