from collections import deque

graph = [[1, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 0, 1]]

def bfs(graph, input_start):
    visited = [False] * len(graph)
    answer = list()
    queue = deque()

    queue.append(input_start)
    visited[input_start] = True

    while queue:
        node = queue.popleft()
        print("node = ",node)
        answer.append(node)
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and not visited[i] and node != i:
                print("i = ",i)
                queue.append(i)
                visited[i] = True
    return answer

print(bfs(graph,0))

