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


# 노드의 개수, 간선의 개수를 입력받기
V, E = 7, 11
edge = [
    [0, 1, 32],
    [0, 2, 31],
    [0, 5, 60],
    [0, 6, 51],
    [1, 2, 21],
    [2, 4, 46],
    [2, 6, 25],
    [3, 4, 34],
    [3, 5, 18],
    [4, 5, 40],
    [4, 6, 51],
]
# 인접 리스트
graph = [[] for _ in range(V)]
distance = [10e9]* V

for idx in range(E):
    x, y, weight = edge[idx]
    graph[x].append([y, weight])
    graph[y].append([x, weight])

dijkstra(0)
# 모든 노드로 가기 위한 최단 거리 출력
for i in range(V):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == 1e9:
        print("INF", end=' ')
    else:
        print(distance[i], end=' ')
