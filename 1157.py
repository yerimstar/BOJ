import collections

words = input().upper()
count = collections.Counter(words)
max_num = max(count.values())
check = 0
for k,v in count.items():
    if v == max_num:
        check += 1
if check == 1:
    print(list(count.keys())[list(count.values()).index(max_num)])
elif check != 1:
    print("?")