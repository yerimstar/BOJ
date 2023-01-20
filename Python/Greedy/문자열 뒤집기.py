import sys
lst = list(map(int,sys.stdin.readline().rstrip()))
one_check = 0
zero_check = 0
print(lst)
# 0과 1이 구분되는 지점을 체크하면 된다.
for i in range(len(lst)):
    if i == (len(lst) - 1):
        if lst[i] == 0:
            zero_check += 1
        elif lst[i] == 1:
            one_check += 1
    elif lst[i] != lst[i+1]:
        if lst[i] == 0:
            zero_check += 1
        elif lst[i] == 1:
            one_check += 1
# 연속된 0 구간과 연속된 1 구간 중에서 더 작은 값이 최솟값이 된다.
print(min(one_check,zero_check))