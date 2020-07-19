import sys
N = int(sys.stdin.readline())
nums = [0]*10001
print(nums)
for i in range(N):
    num = int(sys.stdin.readline())
    nums[i] = num
for i in sorted(nums):
    if i != 0:
        print(i)