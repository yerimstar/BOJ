# 계단 오르기
N = int(input())
stair = []
for _ in range(N):
    stair.append(int(input()))

if N == 1: # 런타임 에러 해결
    d = [stair[0]]
elif N == 2:
    d = [stair[0], stair[0] + stair[1]]
elif 2 < N:
    d = [stair[0], stair[0] + stair[1], max(stair[0] + stair[2], stair[1] + stair[2])]

for i in range(3,N):
    d.append(max(stair[i-1]+stair[i]+d[i-3],stair[i]+d[i-2]))
    # 1칸 전 + 3개 연속 불가능하기 때문에 3칸 전 , 2칸 전 => 최댓값
print(d[N-1])