from collections import deque
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

visited = [[0] * N for _ in range(N)]

dx = [-1,1,0,0] # 상하좌우 값
dy = [0,0,-1,1]

cnts = [] # 각 집의 수 저장
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1 # 처음 위치 방문 체크
    cnt = 1 # 집의 수 count
    while queue:
        x,y = queue.popleft()
        for i in range(4): # 상하좌우 체크
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= N: # 구간 밖 체크 안함
                continue
            if visited[tx][ty] == 1 or graph[tx][ty] == 0: # 처음 방문(visited 값 0) + 원래 값도 1을 가지고 있어야 방문 가능
                continue
            queue.append((tx,ty)) # 다음 방문 위치
            visited[tx][ty] = 1 # 방문 표시
            cnt += 1 # 집의 수 1 증가
    cnts.append(str(cnt))

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == 1: # 처음 방문(visited 값 0) + 원래 값도 1을 가지고 있어야 방문 가능
            bfs(i,j)

cnts = sorted(cnts) # 집의 수를 오름차순 정렬
print(len(cnts))
for c in cnts:
    print(c)


