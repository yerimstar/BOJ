# 단어 정렬하기
from queue import PriorityQueue

N = int(input())
que = PriorityQueue()
result = 0


for _ in range(N):
    que.put(int(input()))

if N == 1:
    result = 0
else:
    for i in range(N):
        tmp = que.get()
        print("tmp = ",tmp)
        if i == 0:
            result += tmp
        elif i == 1:
            result += tmp
            pretmpresult = result
        else:
            pretmpresult += tmp
            result += pretmpresult
print(result)


