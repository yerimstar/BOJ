# DSLR
import sys
from collections import deque

def bfs(s,e):
    q = deque()
    q.append(s)
    while q:
        n = q.popleft()
        for m in move:
            if m == 'D':
                if 2 * n > 9999:
                    register = 2 * n % 10000
                else:
                    register = 2 * n
            elif m == 'S':
                if n == 0:
                    register = 9999
                else:
                    register = n - 1
            elif m == 'L':
                if len(str(n)) == 4:
                    n = str(n)
                    register = int(n[1] + n[2] + n[3] + n[0])
            elif m == 'R':
                if len(str(n)) == 4:
                    n = str(n)
                    register = int(n[3] + n[0] + n[1] + n[2])
            n = int(n)
            if 0 <= register < 10000:
                q.append(register)
                visited[register] = visited[n] + m
                if register == e:
                    return
    return
t = int(sys.stdin.readline())
move = ['D','S','L','R']
for _ in range(t):
    visited = ['' for _ in range(10000)]
    A,B = map(int,sys.stdin.readline().split())
    bfs(A,B)
    print(visited[B])