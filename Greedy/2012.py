# 등수 매기기
N = int(input())
# 최종 등수
ranks = []
# 가능한 등수
nums = [i+1 for i in range(N)]
# 불만도 점수
score = 0
for _ in range(N):
    rank = int(input())
    ranks.append(rank)

ranks.sort()
check = list(set(nums)-set(ranks))

for i in range(N-1):
    if ranks[i] == ranks[i-1]:
        score += abs(check[0]-ranks[i])
        check.remove(check[0])
    else:
        pass

print(score)