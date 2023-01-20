# Puyo Puyo
import sys
from collections import deque

def bfs(x,y,color,cnt):
    visited = [[False for _ in range(6)] for _ in range(12)] # 방문처리
    q = deque()
    lst = []
    q.append((x,y,color,cnt))
    lst.append((x,y,color,cnt)) # 뿌요 값 저장
    visited[x][y] = True

    while q:
        x,y,color,cnt = q.popleft()
        for mx,my in move: # 동서남북 탐색
            dx = x + mx
            dy = y + my
            if 0 <= dx < 12 and 0 <= dy < 6: # 범위 체크
                if not visited[dx][dy] and graph[dx][dy] == color: # 아직 방문하지 않은 곳 + 색상이 동일한 뿌요
                    visited[dx][dy] = True # 방문처리
                    q.append((dx,dy,color,cnt + 1))
                    lst.append((dx,dy,color,cnt + 1))
    if len(lst) >= 4: # 같은 색상 뿌요가 4개 이상이라면 터짐
        # 뿌요의 원래 위치 '.'로 변경
        graph[x][y] = '.'
        for x, y, c, cnt in lst:
            if c == color:
                graph[x][y] = '.'
        return 1 # 뿌요 터짐

    return 0 # 뿌요 안 터짐

def puyo_move(): # 뿌요 중력에 의해 아래로 내려감
    check = 0
    for i in range(6):
        q = deque()
        # 해당 열에 puyo 값이 있는지 체크
        for j in range(11,-1,-1): # 오른쪽 아래부터 탐색 시작
            if graph[j][i] != '.':
                q.append(graph[j][i]) # puyo 값 저장
                graph[j][i] = '.' # 기존에 puyo 값이 있던 곳을 '.'으로 변경
        # puyo 위치 업데이트
        for j in range(11,-1,-1): # 오른쪽 아래부터 탐색 시작
            # puyo 값이 있다면 -> 업데이트 진행 (중력에 의해 아래로 이동)
            if q:
                graph[j][i] = q.popleft()
            # 없다면 종료
            else:
                check += 1

    if check == 72: # 행(12) * 열(6)이 모두 '.'라면 False 반환
        return False
    else:
        return True

graph = []
puyo = deque()
move = [[0,1],[1,0],[0,-1],[-1,0]] # 동서남북

for i in range(12):
    graph.append(list(sys.stdin.readline().strip()))

time = 0
while True:
    check = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.': # 뿌요
                check += bfs(i,j,graph[i][j],1) # 뿌요 터질 수 있는지 체크
    if check > 0: # 뿌요그룹이 하나이상 터졌다면
        time += 1 # 시간 증가
    else:
        break
    if not puyo_move(): # 뿌요가 하나도 없다면 중단
        break

print(time)
