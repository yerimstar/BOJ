# 스티커
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = []
    for _ in range(2):
        lst.append(list(map(int,sys.stdin.readline().split())))
    for j in range(1,n):
        if j == 1:
            lst[0][j] += lst[1][j-1]
            lst[1][j] += lst[0][j-1]
        else:
            lst[0][j] += max(lst[1][j-1],lst[1][j-2])
            lst[1][j] += max(lst[0][j - 1], lst[0][j - 2])
    print(max(lst[0][-1],lst[1][-1]))