# 뱀
import sys
from collections import deque

apple = []
time = []
direction = []
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    a,b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1 # 사과
l = int(sys.stdin.readline().strip())
for _ in range(l):
    tmp = sys.stdin.readline().split()
    time.append(int(tmp[0]))
    direction.append(tmp[1])

dx = [1,0,-1,0] # 우 하 좌 상
dy = [0,1,0,-1]

snake = deque()
snake.append([0,0]) # 꼬리 자르기 체크하기 위함
t = 1
check_direction = 0
x,y = 0, 0
graph[y][x] = 2 # 방문처리

while True:
    x = x + dx[check_direction]
    y = y + dy[check_direction]
    if 0 <= x < n and 0 <= y < n and graph[y][x] != 2:
        if graph[y][x] != 1: # 사과 없으면 꼬리 자르기
            tail_y, tail_x = snake.popleft()
            graph[tail_y][tail_x] = 0  # 꼬리 자르기
        graph[y][x] = 2 # 방문처리
        snake.append([y,x])
        if t in time:
            d = direction[time.index(t)]
            if d == 'D':
                check_direction = (check_direction+1) % 4
            elif d == 'L':
                check_direction = (check_direction-1) % 4
        t += 1 # 1초씩 증가
    else:
        print(t)
        exit()