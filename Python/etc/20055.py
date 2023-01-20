from collections import deque
import sys

N,K = map(int,sys.stdin.readline().split())
belt = deque(list(map(int,sys.stdin.readline().split())))
robots = deque([0] * N)
cnt = 0

def max_index():
    for i in range(N-1,-1,-1):
        if robots[i] == 1:
            break
    return i

while True:
    cnt += 1

    #1단계
    if robots[-1] == 1:
        robots[-1] = 0
    belt.rotate()
    robots.rotate()
    if robots[-1] == 1:
        robots[-1] = 0

    #2단계
    maxI = max_index()
    for j in range(maxI+1,-1,-1):
        if robots[j] == 1:
            if (robots[j + 1] == 0) and (belt[j + 1] >= 1):
                robots[j] = 0
                robots[j + 1] = 1
                belt[j + 1] -= 1  # 이동하는 칸 내구도 1 감소

    #3단계
    if belt[0] != 0:
        robots[0] = 1
        belt[0] -= 1

    #4단계
    if belt.count(0) >= K:
        break

print(cnt)