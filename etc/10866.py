import sys
from collections import deque
N = int(sys.stdin.readline())
dq = deque([])
for i in range(N):
    function = sys.stdin.readline().split()
    if function[0] == "push_front":
        dq.appendleft(int(function[1]))
    elif function[0] == "push_back":
        dq.append(int(function[1]))
    elif function[0] == "pop_front":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq.popleft())
    elif function[0] == "pop_back":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq.pop())
    elif function[0] == "size":
        print(len(dq))
    elif function[0] == "empty":
        if len(dq) == 0:
            print("1")
        else:
            print("0")
    elif function[0] == "front":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq[0])
    elif function[0] == "back":
        if len(dq) == 0:
            print("-1")
        else:
            print(dq[-1])