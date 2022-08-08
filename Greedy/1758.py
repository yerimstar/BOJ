# 알바생 강호
# 서있는 고객수
N = int(input())
tips = []
result = 0

for _ in range(N):
    tip = int(input())
    tips.append(tip)

# 내림차순 정렬 - 팁 많이 주는 사람을 앞으로 배치
tips.sort(reverse=True)

for i in range(N):
    finalTip = tips[i]-((i+1)-1)
    if finalTip > 0:
        result += finalTip
print(result)