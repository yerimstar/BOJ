# 스타트링크
import sys
from collections import deque

F,S,G,U,D = map(int,sys.stdin.readline().split())
queue = deque([S])
visited = [0] * (F+1)
visited[S] = 1
while queue:
    now = queue.popleft()
    if now == G:
        print(visited[now]-1)
        exit()
    for stair in (now+U,now-D):
        if 0 < stair <= F and visited[stair] == 0:
            queue.append(stair)
            visited[stair] = visited[now] + 1
print("use the stairs")