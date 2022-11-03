# 다리 놓기
import sys
from itertools import combinations
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    print(len(list(combinations(list(range(m)),n))))
