# 파도반 수열
import sys
t = int(sys.stdin.readline())
lst = [1, 1, 1, 2,2]
for _ in range(t):
    n = int(sys.stdin.readline())
    if n <= len(lst):
        print(lst[n-1])
    else:
        for i in range(len(lst)-5,n-5):
            lst.append(lst[i]+lst[-1])
        print(lst[n-1])


