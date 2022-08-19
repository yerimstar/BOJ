import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
group = 0
check = lst[0]
cnt = 0
for i in range(len(lst)):
    if cnt != check and check == lst[i]:
        cnt += 1
    if cnt == check:
        group += 1
        cnt = 0
        if i != len(lst) -1:
            check = lst[i+1]
print(group)