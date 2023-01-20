import sys
stack = []
def push(n):
    stack.append(int(n))
def pop():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack.pop())
def size():
    print(len(stack))
def top():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[-1])
def empty():
    if len(stack) == 0:
        print("1")
    else:
        print("0")

N = int(sys.stdin.readline())
for i in range(N):
    function = sys.stdin.readline().split()
    if function[0] == "push":
        stack.append(function[1])
    elif function[0] == "pop":
        pop()
    elif function[0] == "size":
        size()
    elif function[0] == "top":
        top()
    elif function[0] == "empty":
        empty()