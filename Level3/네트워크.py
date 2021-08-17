from collections import deque
# BFS
def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            while queue:
                v = queue.popleft()
                for j in range(n):
                    if computers[v][j] and v != j and not visited[j]:
                        queue.append(j)
                        visited[j] = True
            answer += 1
    return answer

# DFS
def dfs(graph, start, visited):
    visited[start] = True
    for i in range(len(graph[start])): # 그냥 len(graph)해도 됨
        if graph[start][i] and not visited[i]:
            dfs(graph,i,visited)

def solution2(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(computers,i,visited)
            answer += 1
    return answer