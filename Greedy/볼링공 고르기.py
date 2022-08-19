import sys
n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
result = 0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] != lst[j]:
            result += 1
print(result)