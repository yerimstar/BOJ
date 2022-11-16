# Puyo Puyo
import sys
from collections import deque

def bfs(x,y,color,cnt):
    visited = [[False for _ in range(6)] for _ in range(12)]
    q = deque()
    lst = []
    q.append((x,y,color,cnt))
    lst.append((x,y,color,cnt))
    visited[x][y] = True
    check = 1

    while q:
        x,y,color,cnt = q.popleft()
        if check >= 4:
            graph[x][y] = '.'
            for x,y,c,cnt in lst:
                if c == color:
                    graph[x][y] = '.'
            return 1
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < 12 and 0 <= dy < 6:
                if not visited[dx][dy] and graph[dx][dy] == color:
                    visited[dx][dy] = True
                    q.append((dx,dy,color,cnt + 1))
                    lst.append((dx,dy,color,cnt + 1))
                    check += 1
    return 0

def puyo_move():
    check = 0
    for i in range(6):
        q = deque()
        # 해당 열에 puyo 값이 있는지 체크
        for j in range(11,-1,-1):
            if graph[j][i] != '.':
                q.append(graph[j][i]) # puyo 값 저장
                graph[j][i] = '.' # 기존에 puyo 값이 있던 곳을 '.'으로 변경
        # puyo 위치 업데이트
        for j in range(11,-1,-1):
            # puyo 값이 있다면 -> 업데이트 진행 (중력에 의해 아래로 이동)
            if q:
                graph[j][i] = q.popleft()
            # 없다면 종료
            else:
                check += 1

    if check == 72:
        return False
    else:
        return True

graph = []
puyo = deque()
move = [[0,1],[1,0],[0,-1],[-1,0]]
for i in range(12):
    graph.append(list(sys.stdin.readline().strip()))

result = 0
while True:
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                result += bfs(i,j,graph[i][j],1)
    if not puyo_move():
        break

print(result)
