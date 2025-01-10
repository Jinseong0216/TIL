import heapq

N, M, K = map(int, input().split())
generators = list(map(int, input().split()))
disconnected = set([i for i in range(1, N+1) if i not in generators])
connection, edges = {}, {}

for i in range(1, N+1): 
    edges[i] = {}
    connection[i] = 0

for _ in range(M):
    u, v, cost = map(int, input().split())
    edges[u][v], edges[v][u] = cost, cost

min_price = 0
heap = [(0, generator, generator) for generator in generators]
while heap and disconnected:
    cost, before, city = heapq.heappop(heap)
    if connection[city]: continue
    connection[city] = before
    disconnected = disconnected - set([city])
    min_price += cost
    for next in edges[city]:
        if connection[next]: continue
        heapq.heappush(heap, (edges[city][next], city, next))
print(min_price)