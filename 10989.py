import sys
N = int(sys.stdin.readline())
nums = [0]*(N)
print(nums)
for i in range(N):
    num = int(input())
    nums[i] = num
for i in sorted(nums):
    print(i)