# 캠핑
import sys
while(1):
    L,P,V = map(int,sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0: # 종료조건
        exit()

    camping = V // P
    max_camping = L * camping + (V - P * camping)
    print(max_camping)