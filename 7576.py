# 토마토
# 1차 아이디어
"""
미로찾기 문제랑 비슷..?
단, 토마토가 없는 경우도 체크해야함..
없을 경우에는 패스..하는 방향으로.?
"""
# 2차 아이디어
"""
1이 있는 경우를 graph에 append해서...간선끼리 체크하는 방법..!
그래야 하루가 지날 때마다 연결되어 있는 애들이 동시 다발적으로 익기 때문!
"""
import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int,sys.stdin.readline().split())))

graph = []
zero_count = 0
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 1: # 익은 토마토 미리 체크
            graph.append([n,m])
        elif tomato[n][m] == 0:
            zero_count += 1


move = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs():
    queue = deque(graph)
    while queue:
        x,y = queue.popleft()
        if tomato[x][y] == -1:
            continue
        else:
            for i in range(4):
                dx = x + move[i][0]
                dy = y + move[i][1]
                if dx < 0 or dx >= N or dy < 0 or dy >= M:
                    continue
                if tomato[dx][dy] == 0:
                    tomato[dx][dy] = tomato[x][y] + 1
                    queue.append([dx,dy])


if zero_count > 0:
    bfs()
    max = 0
    print(tomato)
    for n in range(N):
        for m in range(M):
            if tomato[n][m] == 0:
                print(-1)
                exit()
            elif tomato[n][m] > max:
                max = tomato[n][m]
    print(max-1) # 시작값이 1이였으니까...최소 일수를 출력하는 거니까 -1 해줘야됨
else:
    print(0)


