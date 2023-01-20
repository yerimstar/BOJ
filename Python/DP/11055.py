# 가장 큰 증가 부분 수열
import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dp = [0] * (n+1) # dp 테이블 생성
for i in range(n): # 값 초기화
    dp[i] = lst[i]

for i in range(1,n):
    for j in range(i):
        if lst[j] < lst[i]: # 값 비교
            dp[i] = max(dp[i],dp[j]+lst[i])

print(max(dp)) # 최댓값 출력

'''
반례
3
105 31 104
'''