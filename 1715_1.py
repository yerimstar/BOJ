# 카드 정렬하기
import sys
from queue import PriorityQueue

q = PriorityQueue()

n = int(sys.stdin.readline().strip())
for _ in range(n):
    q.put(int(sys.stdin.readline().strip()))

result = 0
while q.qsize() > 1:
    tmp1 = q.get()
    tmp2 = q.get()
    tmp = tmp1 + tmp2
    result += tmp
    q.put(tmp)

print(result)