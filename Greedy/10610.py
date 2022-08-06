# 30
from itertools import permutations
n = input()
lst = list(permutations(n,len(n)))
result = -1
for l in lst:
    num = int("".join(l))
    if num % 30 == 0 and l[0] != 0:
        result = max(result,num)
print(result)