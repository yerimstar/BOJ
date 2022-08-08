import sys
# 등수 매기기
N = int(sys.stdin.readline())
# 최종 등수
ranks = []
# 불만도 점수
score = 0
for _ in range(N):
    rank = int(sys.stdin.readline())
    ranks.append(rank)

ranks.sort()

for i in range(1,N+1):
    score += abs(ranks[i-1]-i)
print(score)