# 치즈
import sys
from collections import deque

def bfs(x,y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([x,y])
    visited[x][y] = True  # 방문처리
    while q:
        x,y = q.popleft()
        for mx,my in move: # 4방향 탐색
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m: # 범위 내부인지 체크
                if not visited[dx][dy]: # 아직 방문하지 않은 곳이라면
                    if graph[dx][dy] == 1: # 해당 치즈를 처음 만나는 경우
                        graph[dx][dy] = -1
                    elif graph[dx][dy] < 0:# 해당 치즈를 이미 만난 경우
                        graph[dx][dy] -= 1
                    elif graph[dx][dy] == 0: # 공기인 경우
                        q.append([dx, dy])
                        visited[dx][dy] = True # 방문처리
    cnt = 0 # 치즈 격자 개수
    for i in range(n):
        for j in range(m):
            if graph[i][j] <= -2: # 외부 공기와 2번 이상 접촉한 치즈
                graph[i][j] = 0 # 녹아버림
            elif graph[i][j] == -1: # 외부 공기와 1번 접촉한 치즈
                graph[i][j] = 1 # 녹지 않음

            if graph[i][j] == 1: # 현재 남아있는 치즈 개수 세기
                cnt += 1
    return cnt

n,m = map(int,sys.stdin.readline().split())
check = 0
graph = []
move = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for i in range(m):
        if tmp[i] == 1: # 초반 치즈 격자 개수 세기
            check += 1
    graph.append(tmp)

year = 0
while check != 0: # 치즈가 모두 사라질 때까지
    cnt = bfs(0,0)
    check = cnt
    year += 1 # 1년 증가
print(year)

