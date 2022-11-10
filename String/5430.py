# AC
import sys
from collections import deque

def f(lst,p):
    lst = deque(lst)
    q = deque(p)
    while q:
        method = q.popleft()
        if method == 'R':
            lst.reverse()
        elif method == 'D':
            if len(lst) == 0:
                print("error")
                return
            lst.popleft()
    return list(lst)

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    lst = sys.stdin.readline().strip().replace('[','').replace(']','').split(',')
    if n == 0:
        print("error")
        continue
    result = f(lst,p)
    if type(result) == list:
        result = list(map(int, result))
        print(result)







