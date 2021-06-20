N,K = map(int,input().split())
jewerly = []
bag = []
money = 0

for i in range(N):
    M,V = map(int,input().split())
    jewerly.append((M,V))

jewerly.sort(key = lambda x : x[0])
print(jewerly)

for i in range(K):
    bag.append(int(input()))

for i in range(K):
    for j in range(N):
        money += bag[i] // jewerly[j]

