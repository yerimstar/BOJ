import sys
from itertools import permutations
N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
max = list(permutations(nums,3))
maxs = []
for i in range(len(max)):
    num = sum(max[i])
    if num < M:
        maxs.append(num)
sort_max = sorted(maxs,reverse = True)
print(sort_max[0])