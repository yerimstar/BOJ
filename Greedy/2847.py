# 게임을 만든 동준이
N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

cnt = 0
while True:
    check = 0
    for i in range(N - 1):
        if scores[i] >= scores[i + 1]:
            scores[i] -= 1
            cnt += 1
        else:
            check += 1
    if check == (N-1):
        break

print(cnt)