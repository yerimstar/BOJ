from queue import PriorityQueue

N = int(input())
que = PriorityQueue()
result = 0
tmpresult = 0

for _ in range(N):
    que.put(int(input()))

for i in range(N):
    if i > 1:
        tmpresult = result
    result += (tmpresult + que.get())
    print(result)

print(result)


