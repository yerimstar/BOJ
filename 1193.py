"""
#Python3 - 시간 초과 PyPy3 - 메모리 초과
X= int(input())
p = []
i = 1
def print_num(a):
    print(p[p.index(a)])
while(1):
    for j in range(i):
        x = [str(i-j),str(j+1)]
        a = "/".join(x)
        p.append(a)
        if len(p) == X:
            print_num(a)
            exit()

    i += 1

    for k in range(i):
        y = [str(k+1),str(i-k)]
        b = "/".join(y)
        p.append(b)
        if len(p) == X:
            print_num(b)
            exit()
    i += 1
"""

