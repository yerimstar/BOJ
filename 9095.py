# 1,2,3 더하기
T = int(input())
lst = []

for _ in range(T):
    num = [0, 1, 2, 4]
    N = int(input())
    for i in range(4,N+1):
        num.append(num[i-1]+num[i-2]+num[i-3])
    lst.append(num[N])

for l in lst:
    print(l)