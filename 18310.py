# 안테나
import sys
n = int(sys.stdin.readline().strip())
house = list(map(int,sys.stdin.readline().split()))
house.sort()
if n % 2 == 0:
    print(house[n//2-1])
else:
    print(house[n//2])