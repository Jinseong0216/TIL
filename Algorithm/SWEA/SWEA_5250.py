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
    # N, E = map(int, input().split())
    V = int(input())
    distance = [10e9] * (V * V)
    grid = [list(map(int, input().split())) for _ in range(V)]
    graph = [[] for _ in range(V * V)]

    for idx in range(V):
        for jdx in range(V):
            node = idx * V + jdx
            dij = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for di, dj in dij:
                n_idx, n_jdx = idx + di, jdx + dj
                if n_idx < 0 or n_jdx < 0 or n_idx >= V or n_jdx >= V: continue
                nbr = n_idx * V + n_jdx
                dist = max(0, grid[n_idx][n_jdx] - grid[idx][jdx]) + 1
                graph[node].append([nbr, dist])
    dijkstra(0)
    print(f'#{T}', distance[-1])
