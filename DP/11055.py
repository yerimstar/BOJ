# 가장 큰 증가 부분 수열
import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dp = [0] * (n+1)
for i in range(n):
    dp[i] = lst[i]

for i in range(1,n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i],dp[j]+lst[i])

print(max(dp))

'''
3
105 31 104
'''