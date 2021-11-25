# 보석 도둑
import sys
N,K = map(int,sys.stdin.readline().split())
jewerly = list()
bag = list()

for _ in range(N):
    M,V = map(int,sys.stdin.readline().split())
    jewerly.append([M,V])

jewerly.sort(key = lambda x : x[0])
print(jewerly)

for _ in range(K):
    bag.append(int(sys.stdin.readline().strip()))

for i in range(K):
    for j in range(N):
        money += bag[i] // jewerly[j]

