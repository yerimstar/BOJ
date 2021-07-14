import sys
n = int(sys.stdin.readline())
num1,num2 = map(int ,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    m1,m2 = map(int,sys.stdin.readline().split())
    graph[m1].append(m2)
    graph[m2].append(m1)
print(graph)

def dfs(start_node):
    visited = list()
    answer = list()
    stack = list()

    stack.append(start_node)
    visited.append(start_node)

    while stack:
        node = stack.pop()
        answer.append(node)

        for i in range(len(graph[node])):
            if i not in visited:
                if graph[node][i] == 2:
                    stack.append(i)
                    visited.append(i)
                    break
                elif graph[node][i] == 1:
                    stack.append(i)
                    visited.append(i)
                    break
    if start_node == num1:
        if num2 in answer:
            return answer.index(num2)
        else:
            return -1
    elif start_node == num2:
        if num1 in answer:
            return answer.index(num1)
        else:
            return -1

print(max(dfs(num1),dfs(num2)))
