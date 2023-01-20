# 빙산
import sys
from collections import deque

def bfs(x,y):
    iceLst = []
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        ice_cnt = 0 # 4방향 바다 개수 세기
        x,y = q.popleft()
        for mx,my in move: # 4방향 체크
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m: # 범위 밖 체크
                if graph[dx][dy] == 0: # 바다인 경우
                    ice_cnt += 1 # 바다 개수
                elif not visited[dx][dy] and graph[dx][dy] > 0: # 빙하인데 아직 방문 전
                    q.append([dx,dy])
                    visited[dx][dy] = True
        if ice_cnt > 0: # 바다와 인접해있는 경우
            iceLst.append([x,y,ice_cnt])
    for x,y,ice_cnt in iceLst:
        graph[x][y] = max(0,graph[x][y]-ice_cnt) # 0미만 값 불가 -> max(0,녹은빙하)
    return 1

n,m = map(int,sys.stdin.readline().split())
graph = []
move = [[0,1],[0,-1],[1,0],[-1,0]]
ice = deque()
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if tmp[j]: # 빙하 위치 저장
            ice.append((i,j))
    graph.append(tmp)

year = 0
while ice:
    visited = [[False for _ in range(m)] for _ in range(n)]
    oceanLst = []
    cnt = 0
    for i, j in ice:
        if graph[i][j] > 0 and not visited[i][j]: # 빙하이고 아직 방문하지 않은 곳
            cnt += bfs(i,j)
        elif graph[i][j] == 0: # 바다인 경우
            oceanLst.append((i,j))
    if cnt > 1:
        print(year)
        break
    ice = list(set(ice)-set(oceanLst)) # 빙하리스트 업데이트
    year += 1

if cnt < 2: # 다 녹을 때까지 2덩이 이상이 안되는 경우
    print(0)
