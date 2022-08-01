# K번째 수
import sys
N, K = map(int,sys.stdin.readline().split())
nums = sorted(list(map(int,sys.stdin.readline().split())))
print(nums[K-1])
