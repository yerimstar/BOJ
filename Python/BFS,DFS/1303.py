# 전쟁 - 전투
import sys
from collections import deque
def bfs(x,y,check):
    cnt_b = 1
    cnt_w = 1
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        # 이동 방향
        for mx,my in move:
            dx = x + mx
            dy = y + my
            # 전쟁터 밖 확인 
            if 0 <= dx < m and 0 <= dy < n:
                if check == 'W' and not visited[dx][dy] and graph[dx][dy] == 'W':
                    cnt_w += 1
                    q.append([dx,dy])
                    visited[dx][dy] = True
                elif check == 'B' and not visited[dx][dy] and graph[dx][dy] == 'B':
                    cnt_b += 1
                    q.append([dx,dy])
                    visited[dx][dy] = True
    if check == 'W':
        return cnt_w**2
    elif check == 'B':
        return cnt_b**2

n,m = map(int,sys.stdin.readline().split()) # 가로, 세로 길이
graph = [] # 전쟁터
visited = [[False for _ in range(n)] for _ in range(m)] # 방문 처리
move = [[0,1],[0,-1],[1,0],[-1,0]] # 이동 방향
# 전쟁터 병사 위치 입력 받기
for _ in range(m):
    graph.append(list(sys.stdin.readline().strip()))
white = []
blue = []
for i in range(m):
    for j in range(n):
        # 우리팀(흰색) 병력 체크
        if graph[i][j] == 'W' and not visited[i][j]:
            white.append(bfs(i,j,'W'))
        # 상대팀(파란색) 병력 체크
        elif graph[i][j] == 'B' and not visited[i][j]:
            blue.append(bfs(i,j,'B'))

print(sum(white),sum(blue))