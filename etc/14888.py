# 연산자 끼워넣기
import sys
from itertools import permutations

N = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
operator = list(map(int,sys.stdin.readline().split()))

min_value = 1e9
max_value = -1e9

check = 0
operators = []
for o in operator:
    check += 1
    if o != 0:
        for _ in range(o):
            if check == 1:
                operators.append("+")
            elif check == 2:
                operators.append("-")
            elif check == 3:
                operators.append("*")
            elif check == 4:
                operators.append("/")

ops = list(set(permutations(operators,N-1)))

for op in ops:
    result = number[0]
    for i in range(N-1):
        if op[i] == '+':
            result += number[i+1]
        elif op[i] == '-':
            result -= number[i+1]
        elif op[i] == '*':
            result *= number[i+1]
        elif op[i] == '/':
            result = int(result/number[i+1])

    max_value = max(result,max_value)
    min_value = min(result,min_value)

print(max_value)
print(min_value)



