# 순열
import sys
from itertools import permutations
n = int(sys.stdin.readline())
lst = [str(_) for _ in range(1,n+1)]
per = list(permutations(lst,n))
for p in per:
    print(' '.join(p))

