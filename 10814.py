from sys import stdin
name = list(stdin.readline().rstrip() for i in range(int(input())))
name.sort(key = lambda x:int(x.split(' ')[0]))
for n in name:
    print(n)
