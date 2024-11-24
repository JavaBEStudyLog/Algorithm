from collections import deque

def bfs(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count

def solution(n, wires):
    answer = float('inf')

    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue
            v1, v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)

        count1 = bfs(graph, 1, n)
        count2 = n - count1
        answer = min(answer, abs(count1 - count2))

    return answer