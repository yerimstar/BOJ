# 뱀과 사다리 게임
import sys
from collections import deque

# 주사위 횟수 저장
board = [0] * 101
# 방문처리
visited = [False] * 101

n,m = map(int,sys.stdin.readline().split())

move = dict()
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    move[x] = y
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    move[u] = v

queue = deque([1])
while queue:
    now = queue.popleft()
    if now == 100:
        print(board[100])
        exit()
    for i in range(1,7):
        next = now + i
        if next <= 100 and not visited[next]:
            # 사다리 or 뱀 -> 위치 이동
            if next in move.keys():
                next = move[next]
            # 방문처리 및 주사위 횟수 증가
            if not visited[next]:
                # 다음 위치 저장
                queue.append(next)
                # 방문처리
                visited[next] = True
                # 주사위 횟수 증가
                board[next] = board[now] + 1
