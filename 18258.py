import sys
import collections
queue = collections.deque([])
def push(X):
    queue.append(X)
    print(queue[-1])
def pop():
    print(queue.popleft())
def size():
    print(len(queue))
def empty():
    if len(queue) == 0:
        print("1")
    else:
        print("0")
def front():
    if len(queue) == 0:
        print("-1")
    else:
        print(queue[-1])
def back():
    if len(queue) == 0:
        print("-1")
    else:
        print(queue[0])
N = int(sys.stdin.readline())
for i in range(N):
    func = sys.stdin.readline().split()
    if 'push' in func:
        push(int(func[-1]))
    elif 'pop' in func:
        pop()
    elif 'size' in func:
        size()
    elif 'empty' in func:
        empty()
    elif 'front' in func:
        front()
    elif 'back' in func:
        back()