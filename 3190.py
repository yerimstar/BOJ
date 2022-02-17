# 뱀
import sys
from collections import deque

apple = []
time = []
direction = []
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
for _ in range(k):
    apple.append(list(map(int,sys.stdin.readline().split())))
l = int(sys.stdin.readline().strip())
for _ in range(l):
    tmp = sys.stdin.readline().split()
    time.append(int(tmp[0]))
    direction.append(tmp[1])

snake = deque()
snake.append([1,1])
t = 0
dx = 1
dy = 0
while(1):
    if t in time:
        d = direction[time.index(t)]
        if d == 'D':
            D = 1
        elif d == 'C':
            D = 0
    t += 1 # 1초씩 증가
    if