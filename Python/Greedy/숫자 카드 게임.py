N,M = map(int,input().split())
result = 0
for _ in range(N):
    lst = list(map(int,input().split()))
    # 현재 행에서 가장 작은 값과 최종 값을 비교해서 더 큰 값으로 치환
    result = max(result,min(lst))
print(result)