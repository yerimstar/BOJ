"""
import sys
n = int(sys.stdin.readline())
fibonacci = [0 for i in range(n+1)]
fibonacci[1] = 1
for i in range(2,n+1):
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]
print(fibonacci[n])
"""
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-2)+fibonacci(num-1)
n = int(input())
print(fibonacci(n))