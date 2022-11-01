# 맥주 마시면서 걸어가기
import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    beer = 1000
    x,y = map(int,sys.stdin.readline().split()) # 시작
    check = 0
    for _ in range(n+1):
        tmpx,tmpy = map(int,sys.stdin.readline().split())
        distance = math.sqrt((tmpy-y)**2+(tmpx-x)**2)
        x,y = tmpx,tmpy
        if beer >= distance:
            beer = 1000
        else:
            check += 1
            break
    if check != 0:
        print("sad")
    else:
        print("happy")

