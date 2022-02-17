# 치킨 배달
import sys
from itertools import combinations

def distance(r1,c1,r2,c2):
    return abs(r1-r2) + abs(c1-c2)

n, m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i+1,j+1])
        elif graph[i][j] == 2:
            chicken.append([i+1,j+1])

result = 9999
for store in list(combinations(chicken,m)):
    distance = 0
    for j in range(len(house)):
        tmp = 9999
        for k in range(len(store)):
            tmp = min(tmp, abs(house[j][0]-store[k][0]) + abs(house[j][1]-store[k][1]))
        distance += tmp
    result = min(result,distance)

print(result)
