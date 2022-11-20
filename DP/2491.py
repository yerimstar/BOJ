#수열
import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
result = 1
cnt = 1
for i in range(1,n):
    if lst[i-1] <= lst[i]:
        cnt += 1
    else:
        cnt = 1
    if result < cnt:
        result = cnt

cnt = 1
for i in range(1,n):
    if lst[i-1] >= lst[i]:
        cnt += 1
    else:
        cnt = 1
    if result < cnt:
        result = cnt
print(result)