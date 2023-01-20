from sys import stdin
num = list(int(stdin.readline()) for i in range(int(input())))
num.sort()
for n in num:
    print(n)
