# 캠핑
import sys
i = 1
while(1):
    L,P,V = map(int,sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    camping = V // P
    max_camping = L * camping + min(L,V % P)
    print("Case %d: %d" %(i,max_camping))
    i += 1