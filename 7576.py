# 토마토
# 1차 아이디어
"""
미로찾기 문제랑 비슷..?
단, 토마토가 없는 경우도 체크해야함..
없을 경우에는 패스..하는 방향으로.?
"""
import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int,sys.stdin.readline().split())))

move = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    print(queue)
    cnt = 0
    while queue:
        x,y = queue.popleft()
        cnt += 1
        print("x =",x,"y =",y)
        if tomato[x][y] == 1:
            for i in range(4):
                dx = x + move[i][0]
                dy = y + move[i][1]
                print("dx =",dx,"dy =",dy)
                if dx < 0 or dx >= N or dy < 0 or dy >= M:
                    continue
                if tomato[dx][dy] == 0:
                    tomato[dx][dy] = 1
                    queue.append([dx,dy])
            print(tomato)
    print(cnt)

zero_count = 0
one_count = 0
s = 0
e = 0
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 0:
            zero_count += 1
        elif tomato[n][m] == 1:
            s = n
            e = m
            one_count += 1

if one_count == M*N:
    print(0)
else:
    bfs(s,e)
