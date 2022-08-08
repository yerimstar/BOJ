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
    if rank in ranks:
        changeRank = sorted(nums)[0]
        ranks.append(changeRank)
        nums.remove(changeRank)
        score += abs(changeRank-rank)
    else:
        ranks.append(rank)
        nums.remove(rank)

print(score)
