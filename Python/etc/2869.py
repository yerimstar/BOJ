"""
시간초과
import sys
A,B,V = map(int,sys.stdin.readline().split())
i = 1
h = 0
while(1):
    h += A
    if h == V:
        break
    h -= B
    if h == V:
        break
    i += 1
sys.stdout.write(str(i))
"""
A,B,V = map(int,input().split())
k = (V-B)//(A-B)
if (V-B)%(A-B) != 0:
    print(k+1)
else:
    print(k)