import sys
from itertools import permutations #순열 permutations
N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split())) # N개의 숫자 카드
nums_permutation = list(permutations(nums,3))# N개의 숫자 카드로 이루어진 조
maxs = [] # 최댓값 구하기
for i in range(len(nums_permutation)):
    num = sum(nums_permutation[i])
    if num <= M:
        maxs.append(num)
sort_max = sorted(maxs,reverse = True)
print(sort_max[0])
