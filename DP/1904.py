# 01타일
import sys
from math import factorial
n = int(sys.stdin.readline())
result = 1 # 1로만 이루어진 01타일
for i in range(n//2):
    total = n-(i+1)
    one = n-(i+1)*2
    zero = i+1
    result += (factorial(total)//((factorial(one))*factorial(zero)))
print(result)