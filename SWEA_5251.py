import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for next in graph[now]:
            weight, next = next[1], next[0]
            cost = dist + weight
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))


for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    distance = [10e9] * (V+1)
    graph = [[] for _ in range(V+1)]
    edges = [list(map(int, input().split())) for _ in range(E)]

    for idx in range(E):
        x, y, weight = edges[idx]
        graph[x].append([y, weight])

    dijkstra(0)
    print(f'#{T}', distance[-1])
