import sys
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
for i in sorted(nums):
    sys.stdout.write(str(i)+'\n')

