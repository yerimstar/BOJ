N,K = map(int,input().split())
belt = list(map(int,input().split()))
belt[0] -= 1
robots = [0] * N
robots[0] = 1
cnt = 0

def robot_move():
    for i in range(N,0,-1):
        if (i-1) == 0:
            robots[0] = 0
        else:
            robots[i-1] = robots[i-2]

    # for i in range(N):
    #     if robots[i] == 1:
    #         belt[i] -= 1

def belt_move():
    tmp = belt[-1]
    for i in range(2 * N, 0, -1):
        if i == 1:
            belt[0] = tmp
        else:
            belt[i - 1] = belt[i - 2]

def robot_check():
    check = 0
    for i in range(1,N-1):
        if robots[i] == 0:
            check += 1
    print(check)
    return check

def belt_check1():
    check = 0
    for i in range(2*N):
        if belt[i] >= 1:
            check += 1
    return check

while True:
    cnt += 1
    print("count = ",cnt)
    print("기본")
    print(belt)
    print(robots)

    print("1단계")
    belt_move()
    robot_move()

    if robots[-1] == 1:
        robots[-1] = 0

    print(belt)
    print(robots)

    print("2단계")
    if (robot_check() == N-2) and (belt_check1() == N*2):
        robot_move()
        belt[robots.index(max(robots))] -= 1 # 이동하는 칸 내구도 1 감소

    print(belt)
    print(robots)

    print("3단계")
    if belt[0] != 0:
        robots[0] = 1
        belt[0] -= 1

    print(belt)
    print(robots)

    print("4단계")
    if len(list(filter(lambda x : x == 0, belt))) >= K:
        break

    # if cnt == 5:
    #     break


print("final = ",cnt)







