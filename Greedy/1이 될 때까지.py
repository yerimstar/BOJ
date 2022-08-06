N,K = map(int,input().split())
# 수행해야 하는 최소 횟수 변수 선언
result = 0
for _ in range(N):
    if N == 1:
        break
    if N % K == 0:
        N //= K
        result += 1
        continue
    N -= 1
    result += 1
print(result)
