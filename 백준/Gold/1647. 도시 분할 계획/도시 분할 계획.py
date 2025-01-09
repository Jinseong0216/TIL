import heapq, sys
input = sys.stdin.readline

def find_mst(houses):
    connected, total_weight, max_cost = 0, 0, 0
    visited = [False]*(N+1)
    heap = [(0, houses[0])]

    while heap and connected < len(houses):
        cost, house = heapq.heappop(heap)
        if visited[house]: continue
        visited[house] = True
        connected += 1; total_weight += cost        
        if max_cost < cost: max_cost = cost
        for nbr, cost in edges[house].items():
            if visited[nbr]: continue
            heapq.heappush(heap, (cost, nbr))
    
    return total_weight, max_cost


N, M = map(int, input().split())
houses = list(range(1, N+1))
edges = {i: {} for i in range(1, N+1)}
for _ in range(M):
    i, j, cost = map(int, input().split())
    edges[i][j], edges[j][i] = cost, cost

total_weight, max_cost = find_mst(houses)
print(total_weight - max_cost)
