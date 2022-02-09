# 안테나
import sys
n = int(sys.stdin.readline().strip())
house = list(map(int,sys.stdin.readline().split()))
tmp = []
for i in range(1,max(house)+1):
    sum = 0
    for h in house:
        sum += abs(h-i)
    tmp.append([i,sum])
print(min(tmp,key = lambda x: x[1])[0])