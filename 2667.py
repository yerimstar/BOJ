from collections import deque
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

visited = [[0] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnts = []
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while queue:
        x,y = queue.popleft()
        print(queue)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue
            if visited[tx][ty] == 1 or graph[tx][ty] == 0:
                continue
            queue.append((tx,ty))
            visited[x][y] = 1
            cnt += 1

    cnts.append(str(cnt))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            print("i = ",i,"j = ",j)
            bfs(i,j)

print(graph)
print(len(cnts))
print(sorted(cnts))
for i in sorted(cnts):
    print(i)