import sys
from itertools import permutations #순열 permutations
N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split())) # N개의 숫자 카드
nums_permutation = list(permutations(nums,3))# N개의 숫자 카드로 이루어진 조합
maxs = [] # 최댓값 구하기
for i in range(len(nums_permutation)): # 조합 중에서 합이 M이하인 값들을 구한다
    num = sum(nums_permutation[i]) # 튜플의
    if num <= M: # M이하면 maxs에 저장한다
        maxs.append(num)
sort_max = sorted(maxs,reverse = True) #오름차순으로 sorting
print(sort_max[0]) # 가장 큰 값을 출력한다
