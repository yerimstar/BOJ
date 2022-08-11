# 가장 긴 증가하는 부분 수열
import sys
# 수열의 길이
n = int(sys.stdin.readline())

# 수열 값
arr = list(map(int,sys.stdin.readline().split()))

# DP 테이블
'''
DP 테이블의 값은 해당 인덱스까지의 부분 수열 중 가장 긴 부분 수열의 길이이다. 
증가하는 수열을 발견하면 길이를 1씩 증가 시킬 것이기 때문에 초기값은 1로 초기화해두어야 한다. 
'''
d = [1] * n

for i in range(n):
    for j in range(1,i+1):
        if arr[j-1] < arr[j]:
            d[i] += 1
print(max(d))

