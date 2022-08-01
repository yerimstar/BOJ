import sys
from collections import deque
dq = deque([])
def push(X):
    dq.append(X)
def pop():
    if len(dq) == 0:
        print("-1")
    else:
        print(dq.popleft())
def size():
    print(len(dq))
def empty():
    if len(dq) == 0:
        print("1")
    else:
        print("0")
def front():
    if len(dq) == 0:
        print("-1")
    else:
        print(dq[0])
def back():
    if len(dq) == 0:
        print("-1")
    else:
        print(dq[-1])

N = int(sys.stdin.readline())
for i in range(N):
    function = sys.stdin.readline().split()
    if function[0] == "push":
        push(int(function[1]))
    elif function[0] == "pop":
        pop()
    elif function[0] == "size":
        size()
    elif function[0] == "empty":
        empty()
    elif function[0] == "front":
        front()
    elif function[0] == "back":
        back()
