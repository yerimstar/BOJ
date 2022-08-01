# RGB거리
import sys
N = int(sys.stdin.readline())
color = []
home = []
for i in range(N):
    home.append(list(map(int,sys.stdin.readline().rstrip().split())))

color.append([home[0][0],home[0][1],home[0][2]])

for i in range(1,N):
    color.append([min(color[i - 1][1], color[i - 1][2]) + home[i][0],min(color[i - 1][0], color[i - 1][2]) + home[i][1],min(color[i - 1][0], color[i - 1][1]) + home[i][2]])

print(min(color[N-1]))

# 궁금한 점
# color = [[0] * 3] * N 이렇게 두고 코드를 짰더니 ..
# color[1],color[2]값이 동시에 변경됨...이유가 뭘까..ㅜㅜ
# -> for문으로 해결해줘야 함