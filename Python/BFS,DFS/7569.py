# 토마토
import sys
from collections import deque
M,N,H = map(int,sys.stdin.readline().split())

# 3차원 배열
graph = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        lst = list(map(int,sys.stdin.readline().split()))
        graph[i].append(lst)

# 익은 토마토 검출
tomato = []
zero_cnt = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                zero_cnt += 1
            elif graph[i][j][k] == 1:
                tomato.append([i,j,k])

mi = [-1,1,0,0,0,0]
mj = [0,0,-1,1,0,0]
mk = [0,0,0,0,-1,1]
def bfs():
    queue = deque(tomato)
    while queue:
        i,j,k = queue.popleft()
        for l in range(6):
            di = i + mi[l]
            dj = j + mj[l]
            dk = k + mk[l]
            if di < 0 or di >= H or dj < 0 or dj >= N or dk < 0 or dk >= M:
                continue
            if graph[di][dj][dk] == 0:
                graph[di][dj][dk] = graph[i][j][k] + 1
                queue.append([di,dj,dk])
# 안 익은 토마토가 없는 경우 0 출력 후 종료
if zero_cnt > 0:
    bfs()
    day_cnt = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    print(-1)
                    exit()
                elif graph[i][j][k] > day_cnt:
                    day_cnt = graph[i][j][k]
    print(day_cnt-1)
else:
    print(0)
