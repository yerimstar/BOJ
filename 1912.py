# 연속합
import sys
max = -1000
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().rstrip().split()))

def fget_max(num):
    global max
    for i in range(N):
        max_num = 0
        if i+num <= N:
            for j in range(i, i + num):
                max_num += nums[j]
            if max_num > max:
                max = max_num

for i in range(1,N+1):
    fget_max(i)
print(max)