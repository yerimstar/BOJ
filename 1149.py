# RGB거리
import sys
N = int(sys.stdin.readline())
home = [[0] * 3] * N
color = [0] * N
for i in range(N):
    home[i] = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(0,3):
    check = i
    for j in range(N):
        if check == 0:
            home_color = min(home[j][1], home[j][2])
            check = home[j].index(home_color)
            color[i] += home_color
        elif check == 1:
            home_color = min(home[j][0], home[j][2])
            check = home[j].index(home_color)
            color[i] += home_color
        elif check == 2:
            home_color = min(home[j][0], home[j][1])
            check = home[j].index(home_color)
            color[i] += home_color
        print(home_color)
print(color)
print(min(color))