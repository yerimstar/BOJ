N,K = map(int,input().split())
belt = list(map(int,input().split()))
robots = [0] * N
cnt = 0

def belt_move():
    tmp = belt[-1]
    for i in range(2 * N, 0, -1):
        if i == 1:
            belt[0] = tmp
        else:
            belt[i - 1] = belt[i - 2]

def robot_move():
    for i in range(N-1,-1,-1):
        if i == 0:
            robots[0] = 0
        else:
            robots[i] = robots[i-1]

def max_index():
    for i in range(N-1,-1,-1):
        if robots[i] == 1:
            break
    return i

while True:
    cnt += 1

    #1단계
    if robots[-1] == 1:
        robots[-1] = 0
    belt_move()
    robot_move()
    if robots[-1] == 1:
        robots[-1] = 0

    #2단계
    maxI = max_index()
    for j in range(maxI+1,-1,-1):
        if robots[j] == 1:
            if (robots[j + 1] == 0) and (belt[j + 1] >= 1):
                robots[j] = 0
                robots[j + 1] = 1
                belt[j + 1] -= 1  # 이동하는 칸 내구도 1 감소

    #3단계
    if belt[0] != 0:
        robots[0] = 1
        belt[0] -= 1

    #4단계
    if len(list(filter(lambda x : x == 0, belt))) >= K:
        break

print(cnt)