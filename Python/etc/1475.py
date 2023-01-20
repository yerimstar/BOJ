import math
nums = input()
nums = list(nums.replace('6','9')) # 모든 6을 9로 치환 + str에서 list로 변환
count = [nums.count(n) if n != '9' else math.floor(nums.count(n)/2+0.5) for n in nums]
print(max(count))