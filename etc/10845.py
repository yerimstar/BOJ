import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    # print("q = ",q)
    tmp = sys.stdin.readline().split()
    if len(tmp) == 2:
        s = tmp[0]
        num = int(tmp[1])
    elif len(tmp) == 1:
        s = tmp[0]

    if s == 'push':
        q.append(num)
    elif s == 'pop':
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif s == 'size':
        print(len(q))
    elif s == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if q:
            print(q[0])
        else:
            print("-1")
    elif s == 'back':
        if q:
            print(q[-1])
        else:
            print("-1")