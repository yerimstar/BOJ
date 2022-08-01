import sys
N = sys.stdin.readline().strip('\n')
num = []
for i in range(len(N)):
    num.append(int(N[i]))
sort = sorted(num,reverse=True)
for i in range(len(sort)):
    print(sort[i],end = '')
