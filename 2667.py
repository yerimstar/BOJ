from collections import deque
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

move = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y):
    check = 0
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            if graph[dx][dy] == 1:
                graph[dx][dy] = -1
                queue.append([dx, dy])
                check += 1
    if check == 0 and graph[x][y] == 1:
        return 1
    else:
        return check

count = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            check = bfs(i, j)
            if check != 0:
                count.append(check)

print(len(count))
count = sorted(count)
for c in count:
    print(c)