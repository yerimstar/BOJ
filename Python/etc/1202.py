# 보석 도둑
import sys
import heapq

N,K = map(int,sys.stdin.readline().split())
jewerly = []
bags = []

for _ in range(N):
    M,V = map(int,sys.stdin.readline().split())
    heapq.heappush(jewerly,[M,V])

for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

result = []
money = 0

for bag in bags:
    while jewerly and bag >= jewerly[0][0]:
            [m,v] = heapq.heappop(jewerly)
            heapq.heappush(result,-v)
    if result:
        money -= heapq.heappop(result)
    elif not jewerly:
        break
print(money)



