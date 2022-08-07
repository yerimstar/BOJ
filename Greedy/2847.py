# 게임을 만든 동준이
N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

cnt = 0
# while True:
#     check = 0
#     for i in range(N - 1):
#         if scores[i] >= scores[i + 1]:
#             scores[i] -= 1
#             cnt += 1
#         else:
#             check += 1
#     if check == (N-1):
#         break
for i in range(N-1,0,-1):
    # 이전 레벨 점수가 현재 레벨 점수보다 크거나 같다면 -> 점수 감소
    if scores[i-1] >= scores[i]:
        # 레벨간 점수 차이 + 1 만큼 감소시켜야 한다
        cnt += (scores[i-1]-scores[i]+1)
        # 최소한으로 줄이는 것이 목적이기 때문에 이전 레벨 점수를 현재 레벨 점수 -1로 변경한다
        scores[i-1] = scores[i]-1
print(cnt)