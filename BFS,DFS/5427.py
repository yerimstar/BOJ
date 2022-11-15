# 불
import sys
from collections import deque
def bfs(sx,sy):
    q = deque(fire)
    visited = [[False for _ in range(w)] for _ in range(h)]
    s = deque()
    s.append((sx,sy,0))
    visited[sx][sy] = True
    while s:
        # 불
        for _ in range(len(q)):
            x, y, t = q.popleft()
            for mx, my in move:
                dx = x + mx
                dy = y + my
                if 0 <= dx < h and 0 <= dy < w:
                    if graph[dx][dy] != '#' and graph[dx][dy] != '*':
                        graph[dx][dy] = '*'
                        q.append((dx, dy, t + 1))
        # 상근
        for _ in range(len(s)):
            sx, sy, st = s.popleft()
            for mx, my in move:
                dx = sx + mx
                dy = sy + my
                if 0 <= dx < h and 0 <= dy < w:
                    if not visited[dx][dy] and graph[dx][dy] != '#' and graph[dx][dy] != '*':
                        visited[dx][dy] = True
                        s.append((dx, dy, st + 1))
                else:
                    print(st+1)
                    return
    print("IMPOSSIBLE")
    return
t = int(sys.stdin.readline())
for _ in range(t):
    w,h = map(int,sys.stdin.readline().split())
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    graph = []
    fire = []
    for i in range(h):
        tmp = list(sys.stdin.readline().strip())
        for j in range(w):
            if tmp[j] == '@':
                sx,sy = i,j
            elif tmp[j] == '*':
                fire.append((i,j,0))
        graph.append(tmp)
    bfs(sx,sy)