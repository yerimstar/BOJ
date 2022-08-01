N = int(input())
lst = []
tmp = []

for i in range(0,N): # N개의 로프의 각 중량값을 입력받는다
    lst.append(int(input()))

lst.sort() # 오름차순 정렬

for i in range(0,N): # 작은 값부터 중량값을 구한다
    tmp.append(lst[i]*(N-i))

print(max(tmp)) # 중량값들 중 최댓값을 구한다