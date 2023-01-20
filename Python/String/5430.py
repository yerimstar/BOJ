# AC
import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    lst = deque(sys.stdin.readline().strip()[1: -1].split(','))
    point = True
    error = False

    if n == 0:
        lst = deque()
    for method in p:
        if method == 'R':
            # 방향 교체
            if point:
                point = False
            else:
                point = True
        elif method == 'D':
            if lst:
                if point:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                error = True
                break
    if error:
        print("error")
    elif not point:
        lst.reverse()
        print('[' + ','.join(lst) + ']')
    else:
        print('[' + ','.join(lst) + ']')