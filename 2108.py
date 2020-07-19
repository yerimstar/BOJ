def most(num):
    most_num = {}
    for n in num:
        if most_num.get(n) is None:
            most_num[n] = 1
        else:
            most_num[n] += 1
    max_list = {}
    most = max(most_num.values())
    for key,value in most_num.items():
        if value == most:
            max_list[key] = value
    sort_dict = sorted(max_list.items())
    if len(max_list) == 1:
        return sort_dict[0][0]
    else:
        return sort_dict[1][0]

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
print("%.0f" %(sum(num)/N))
sort_num = sorted(num)
print(sort_num[int(len(sort_num)//2)])
print(most(num))
print(max(num)-min(num))