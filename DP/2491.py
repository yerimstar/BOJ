#수열
import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
increase_lst = []
decrease_lst = []
cnt = 1
for i in range(1,n):
    if lst[i-1] <= lst[i]:
        cnt += 1
    else:
        increase_lst.append(cnt)
        cnt = 1
if cnt > 1:
    increase_lst.append(cnt)

cnt = 1
for i in range(1,n):
    if lst[i-1] >= lst[i]:
        cnt += 1
    else:
        decrease_lst.append(cnt)
        cnt = 1
if cnt > 1:
    decrease_lst.append(cnt)
result = max(max(increase_lst),max(decrease_lst))
print(result)