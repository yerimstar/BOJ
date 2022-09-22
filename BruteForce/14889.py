# 스타트와 링크
import sys
from itertools import combinations
from itertools import permutations
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
nums = [i+1 for i in range(N)]

# 팀 나누기
lst = list(combinations(nums,N//2))
starter_lst = []
link_lst = []
for l in lst[:len(lst)//2]:
    starter = l
    link = list(set(nums)-set(l))
    starter_lst.append(starter)
    link_lst.append(link)

result_sum = 101
for i in range(len(lst)//2):
    s = starter_lst[i]
    s_lst = list(permutations(s,2))
    starter_sum = 0
    for ss in s_lst:
        a,b = ss
        starter_sum += graph[a-1][b-1]
    l = link_lst[i]
    l_lst = list(permutations(l,2))
    link_sum = 0
    for ll in l_lst:
        a,b = ll
        link_sum += graph[a-1][b-1]
    if abs(starter_sum-link_sum) < result_sum:
        result_sum = abs(starter_sum-link_sum)
print(result_sum)
