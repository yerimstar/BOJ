# 병사 배치하기
import sys

n = int(sys.stdin.readline())
power = list(map(int,sys.stdin.readline().split()))
d = [1] * n

for i in range(n):
    for j in range(i):
        if power[i] < power[j]:
            d[i] = max(d[i],d[j]+1)
print(n-max(d))