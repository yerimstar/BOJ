# 불
import sys
from collections import deque
def bfs(sx,sy):
    q = deque(fire) # 불 deque
    visited = [[False for _ in range(w)] for _ in range(h)] # 방문처리
    s = deque() # 상근 deque
    s.append((sx,sy,0)) # 시작위치 저장
    visited[sx][sy] = True # 방문처리하기
    while s:
        # 불
        for _ in range(len(q)):
            x, y, t = q.popleft()
            for mx, my in move: # 동서남북 체크
                dx = x + mx
                dy = y + my
                if 0 <= dx < h and 0 <= dy < w: # 범위 내부에 있는지 확인
                    if graph[dx][dy] != '#' and graph[dx][dy] != '*': # 벽이 아니고 불이 아니라면
                        graph[dx][dy] = '*' # 불이 번짐
                        q.append((dx, dy, t + 1)) # 시간과 함께 불 위치 저장
        # 상근
        for _ in range(len(s)):
            sx, sy, st = s.popleft()
            for mx, my in move: # 동서남북 체크
                dx = sx + mx
                dy = sy + my
                if 0 <= dx < h and 0 <= dy < w: # 내부에 있다면
                    if not visited[dx][dy] and graph[dx][dy] != '#' and graph[dx][dy] != '*': # 아직 방문하지 않았고, 벽 x, 불 x
                        visited[dx][dy] = True # 방문처리
                        s.append((dx, dy, st + 1)) # 시간과 함께 상근이 위치 저장
                else: # 범위를 벗어난다면 -> 탈출
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
            if tmp[j] == '@': # 시작위치 저장
                sx,sy = i,j
            elif tmp[j] == '*': # 불 위치 저장
                fire.append((i,j,0))
        graph.append(tmp)
    bfs(sx,sy)