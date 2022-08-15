# 정수 삼각형
import sys
n = int(sys.stdin.readline().rstrip())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

d = [0] * ((n*(n+1))//2)
d[0] = lst[0][0]

for i in range(1,n):
    for j in range(len(lst[i])):
        k = (i * (i + 1)) // 2 + j
        if j == 0:
            d[k] = d[k - i] + lst[i][j]
        elif j == len(lst[i])-1:
            d[k] = d[k - (i+1)] + lst[i][j]
        else:
            d[k] = max(d[k-(i+1)],d[k-i]) + lst[i][j]
print(max(d))


