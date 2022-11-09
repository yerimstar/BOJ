# DSLR
import sys
from collections import deque

def bfs(s,e):
    q = deque()
    q.append(s)
    visited[s] = 'Z'
    while q:
        n = q.popleft()
        for m in move:
            d1 = n // 1000
            d2 = (n-1000*d1) // 100
            d3 = (n-1000*d1-100*d2) // 10
            d4 = n-1000*d1-100*d2-10*d3
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
                register = int(str(d2) + str(d3) + str(d4) + str(d1))
            elif m == 'R':
                register = int(str(d4) + str(d1) + str(d2) + str(d3))
            n = int(n)
            if 0 <= register < 10000 and visited[register] == '':
                q.append(register)
                visited[register] = visited[n] + m
                if register == e:
                    return

t = int(sys.stdin.readline())
move = ['D','S','L','R']
for _ in range(t):
    visited = ['' for _ in range(10000)]
    A,B = map(int,sys.stdin.readline().split())
    bfs(A,B)
    print(visited[B][1:])