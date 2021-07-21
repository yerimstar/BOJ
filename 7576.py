# 토마토
# 1차 아이디어
"""
미로찾기 문제랑 비슷..?
단, 토마토가 없는 경우도 체크해야함..
없을 경우에는 패스..하는 방향으로.?
"""
# 2차 아이디어
"""
1이 있는 경우를 graph에 append해서...간선끼리 체크하는 방법..!
그래야 하루가 지날 때마다 연결되어 있는 애들이 동시 다발적으로 익기 때문!
"""
import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int,sys.stdin.readline().split())))

zero_count = 0
one_count = 0
graph = []
# graph = [[] for _ in range(max(M,N)+1)]
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 0:
            zero_count += 1
        elif tomato[n][m] == 1:
            s = n
            e = m
            graph.append([n,m])
            one_count += 1
print(graph)

move = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs():
    queue = deque()
    queue.append([[graph[0][0],graph[0][1]]])
    print(queue)
    cnt = 0
    while queue:
        node = queue.popleft()
        print("node = ",node)
        cnt += 1
        print("len =",len(node))
        for i in range(len(node)):
            x = node[i][0]
            y = node[i][1]
            if tomato[x][y] == 1:
                tmp = []
                for i in range(4):
                    dx = x + move[i][0]
                    dy = y + move[i][1]
                    print("dx =", dx, "dy =", dy)
                    if dx < 0 or dx >= N or dy < 0 or dy >= M:
                        continue
                    if tomato[dx][dy] == 0:
                        tomato[dx][dy] = 1
                        tmp.append([dx, dy])
                queue.append(tmp)
        print(tomato)
    print(cnt)

if one_count == M*N:
    print(0)
else:
    bfs()
