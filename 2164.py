"""
1번 시도 - 시간초과
-> stack 사용
import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    stack.append(N-i)
for i in range(N-1):
    stack.pop()
    temp = stack[-1]
    M = len(stack)-1
    for k in range(M):
        stack[M-k] = stack[M-k-1]
    stack[0] = temp
    if i == N-2:
        print(stack[0])

"""
# deque 사용
import sys
from collections import deque
N = int(sys.stdin.readline())
dq = deque([i for i in range(1,N+1)])
for i in range(N-1):
    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)
print(dq[0])