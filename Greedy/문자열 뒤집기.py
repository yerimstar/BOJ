import sys
lst = list(map(int,sys.stdin.readline().rstrip()))
one_check = 0
zero_check = 0
print(lst)
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
print(min(one_check,zero_check))