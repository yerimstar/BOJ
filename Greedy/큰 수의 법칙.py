N,M,K = map(int,input().split())
nums = sorted(list(map(int,input().split())),reverse=True)
# M을 초과하지 않으면서 (K + 1)개가 몇개 들어갈 수 있을지
result = nums[0]*(M//(K+1))*K +nums[1]*(M//(K+1)) + nums[0]*(M%(K+1))
print(result)