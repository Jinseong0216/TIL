# BOJ 13418 / 학교 탐방하기 / MST
import heapq,sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = {i:{} for i in range(V+1)}
for _ in range(E+1):
    i, j, weight = map(int, input().split())
    weight = (weight+1)%2
    edges[i][j], edges[j][i] = weight, weight 

# 최소힙
heap = [(0, 0)]; visited = [False]*(V+1); connected = 0; min_weight = 0
while heap and connected < V+1:
    weight, building = heapq.heappop(heap)
    if visited[building]: continue
    visited[building]= True; connected +=1; min_weight += weight

    for nbr, weight in edges[building].items():
        if visited[nbr]: continue
        heapq.heappush(heap, (weight, nbr))

# 최대힙
heap = [(0, 0)]; visited = [False]*(V+1); connected = 0; max_weight = 0
while heap and connected < V+1: 
    weight, building = heapq.heappop(heap)
    if visited[building]: continue
    visited[building]= True; connected +=1; max_weight += weight
    for nbr, weight in edges[building].items():
        if visited[nbr]: continue
        heapq.heappush(heap, (-weight, nbr))

print(max_weight**2 - min_weight**2)