# 요세푸스 문제 0
import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
q = deque([_ for _ in range(1,n+1)])
cnt = 0
lst = []
while q:
    cnt += 1
    tmp = q.popleft()
    if cnt == k:
        cnt = 0
        lst.append(tmp)
    else:
        q.append(tmp)
print("<" +', '.join(map(str,lst)) + ">")
