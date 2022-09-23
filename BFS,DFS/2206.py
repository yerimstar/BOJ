# 벽 부수고 이동하기
import sys
import copy
from collections import deque

N,M = map(int,sys.stdin.readline().split())
graph = []
# 맵 생성
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().strip())))

# 벽이 있는 위치 저장
wall = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            wall.append([i,j])
            graph[i][j] = 0
        else:
            graph[i][j] = 1

move = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(map_lst):
    queue = deque([(0,0)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            if dx < 0 or dx >= N or dy < 0 or dy >= M:
               continue
            if map_lst[dx][dy] == 1:
                queue.append([dx, dy])
                map_lst[dx][dy] = map_lst[x][y] + 1
    return map_lst[N-1][M-1]

min_num = 1000
for w in wall:
    map_lst = copy.deepcopy(graph)
    map_lst[w[0]][w[1]] = 1
    num = bfs(map_lst)
    if num > 1 and num < min_num :
        min_num = num
if min_num == 1000:
    print(-1)
else:
    print(min_num)


