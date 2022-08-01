# 연속합
import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
sums = [0] * N
sums[0] = nums[0]

for i in range(1,N):
    if nums[i] > nums[i] + sums[i-1]:
        sums[i] = nums[i]
    else:
        sums[i] = nums[i] + sums[i-1]
print(max(sums))

