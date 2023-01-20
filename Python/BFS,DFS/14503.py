# 로봇 청소기
from collections import deque
def bfs(r,c,d):
    cnt = 0
    visited = [[False]*M for _ in range(N)]
    queue = deque()
    visited[r][c] = True
    # 현재 위치 청소
    if graph[r][c] == 0:
        graph[r][c] = -1
        cnt += 1
    queue.append((r,c))
    while queue:
        y,x = queue.popleft()
        for _ in range(4):
            # 청소 가능 여부와 상관없이 방향 전환 - 왼쪽부터 탐색
            if d == 0:
                d = 3
            else:
                d -= 1
            mx = x + mv[d][0]
            my = y + mv[d][1]
            # 처음 방문하는 곳인지 체크
            if not visited[my][mx]:
                # 범위 내부에 있는지 체크
                if 0 <= mx < M and 0 <= my < N:
                    # 청소가 가능한 공간인지 체크
                    if graph[my][mx] == 0:
                        # 한 칸 전진
                        queue.append((my, mx))
                        # 현재 위치 청소
                        visited[my][mx] = True
                        graph[my][mx] = -1
                        cnt += 1
                        break
        # 4방향 모두 청소가 이미 되어있거나 벽인 경우
        if not queue:
            bx = x + mv[d][0]*(-1)
            by = y + mv[d][1]*(-1)
            # 벽이 아니면 후진 가능
            if graph[by][bx] != 1:
                queue.append((by,bx))
    return cnt

N,M = map(int,input().split())
r,c,d = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]
mv = [[0,-1],[1,0],[0,1],[-1,0]]
print(bfs(r,c,d))
