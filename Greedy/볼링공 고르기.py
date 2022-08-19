import sys
n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
result = 0
for i in range(n):
    for j in range(i+1,n):
        if lst[i] != lst[j]:
            result += 1
print(result)