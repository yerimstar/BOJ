# 가장 긴 감소하는 부분 수열
import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
len = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:
            len[i] = max(len[i],len[j]+1)

print(max(len))