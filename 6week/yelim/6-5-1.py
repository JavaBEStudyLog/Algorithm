import heapq

def solution(N, road, K):
    graph = {i: [] for i in range(1, N+1)}
    for a, b, t in road:
        graph[a].append((b, t))
        graph[b].append((a, t))

    def dijkstra(start):
        distances = {i: float('inf') for i in range(1, N+1)}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    shortest_distances = dijkstra(1)

    reachable_villages = sum(1 for time in shortest_distances.values() if time <= K)

    return reachable_villages

