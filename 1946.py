T = int(input())

for _ in range(T):
    tmp = []
    N = int(input())

    for _ in range(0, N):
        first, second = map(int, input().split())
        tmp.append((first, second))
    tmp.sort(key=lambda x: x[0])

    cnt = 1  # 1차 시험 1등은 무조건 합격

    val = tmp[0][1]

    for i in range(N):
        if val > tmp[i][1]:
            val = tmp[i][1]
            cnt += 1
    print(cnt)




