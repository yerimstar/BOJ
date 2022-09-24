# 숨바꼭질3
import sys
from collections import deque
max_num = 100001
n,k = map(int,sys.stdin.readline().split())
visited = [0] * max_num
distance = [0] * max_num
queue = deque([n])
visited[n] = 1
while queue:
    now = queue.popleft()
    # 동생을 찾으면
    if now == k:
        print(distance[now])
        break
    for d in (now-1,now+1,now*2):
        if 0 <= d <= max_num and visited[d] == 0:
            if d == now*2:
                distance[d] = distance[now]
            else:
                distance[d] = distance[now]+1
            queue.append(d)
            visited[d] = 1



