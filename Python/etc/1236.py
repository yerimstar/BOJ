"""
문제를 잘못 이해함 -> N이 10000개까지 가능힘
N = int(input())
num = []
for i in range(10):
    num.append(int(str(i)+"666"))
    num.append(int("666"+str(i)))

num_sort = sorted(num)
for i in range(len(num_sort)):
    if (N-1) == i:
        print(num_sort[i])

"""
N = int(input())
num = []
for i in range(2700000):
    a = str(i)
    if a.count("666") == 1:
        num.append(a)
    elif a.count("666") == 2:
        num.append(a)
print(num[N-1])