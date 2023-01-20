# 숨바꼭질3
import sys
from collections import deque

max_num = 100001
n,k = map(int,sys.stdin.readline().split())
visited = [0] * max_num
queue = deque([n])
while queue:
    now = queue.popleft()
    # 동생을 찾으면
    if now == k:
        print(visited[now])
        break
    for d in (now*2,now-1,now+1):
        if 0 <= d < max_num and visited[d] == 0:
            if d == now*2:
                visited[d] = visited[now]
            else:
                visited[d] = visited[now]+1
            queue.append(d)



