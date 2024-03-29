# 숨바꼭질
# 1차 아이디어
"""
미로 찾기랑 비슷..?
graph를 visited처럼 사용함. 기존 값 0 -> 방문하면 1
"""
import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
graph = [0 for _ in range(100002)] # 런타임에러 해결
graph[N] = 1
graph[K] = 1

def bfs(x,y):
    if x == y: # 조건 추가 !!
        return 0
    queue = deque()
    cnt = 1
    queue.append([x,cnt])
    while queue:
        x,cnt = queue.popleft()
        for tx in (x-1,x+1,x*2):
            if tx < 0 or tx > 100001: # 런타임에러 해결
                continue
            if tx == y:
                return cnt
            if graph[tx] == 0:
                graph[tx] = 1
                queue.append([tx,cnt+1])

print(bfs(N,K))