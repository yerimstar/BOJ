# 맥주 마시면서 걸어가기
import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([conv[0][0],conv[0][1]])
    visited[0] = True
    while queue:
        x,y = queue.popleft()
        # 현재 위치와 도착 위치 사이의 거리가 1000 이하이면 -> happy
        if abs(x-ex) + abs(y-ey) <= 1000:
            print("happy")
            return
        for i in range(n+1):
            if not visited[i]:
                nx,ny = conv[i]
                if abs(nx - x) + abs(ny - y) <= 1000:
                    queue.append([nx,ny])
                    visited[i] = True
    print("sad")

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    # 시작위치 + 편의점 위치
    conv = []
    for _ in range(n+1):
        conv.append(list(map(int,sys.stdin.readline().split())))
    # 도착 위치
    ex,ey = map(int,sys.stdin.readline().split())
    visited = [False]*(n+1)
    bfs()


