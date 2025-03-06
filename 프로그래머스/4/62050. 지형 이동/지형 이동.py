import sys
sys.setrecursionlimit(10000000)

def solution(land, height):
    info, island_num = find_island(len(land), land, height)
    edges = find_edges(land, info)
    answer = kruskal(island_num, edges)
    return answer

def find_island(N, land, height):
    island_id = 0
    info = [[0 for _ in range(N)] for  _ in range(N)]

    def dfs(i, j, island_id, height, N):
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i+di, j+dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
            if info[ni][nj]: continue
            if abs(land[i][j] - land[ni][nj]) > height: continue
            info[ni][nj] = island_id
            dfs(ni, nj, island_id, height, N)

    for i in range(N):
        for j in range(N):
            if info[i][j]: continue
            island_id += 1
            info[i][j] = island_id
            dfs(i, j, island_id, height, N)

    return info, island_id

def find_edges(land, info):
    edges = []
    N = len(land)

    for i in range(N):
        for j in range(N):
            vertex_1 = info[i][j]
            for di, dj in [[0, 1], [1, 0]]:
                ni, nj = i+di, j+dj
                if ni<0 or nj<0 or ni>=N or nj>=N: continue
                vertex_2 = info[ni][nj]
                if vertex_1 == vertex_2: continue
                edges.append((abs(land[i][j]-land[ni][nj]), vertex_1, vertex_2))
    # 괜찮은 tech'
    edges.sort(key=lambda x: x[0])
    return edges

def kruskal(V, edges):
    parents = [i for i in range(V+1)]

    def find_set(x):
        if parents[x] == x:
            return x
        parents[x] = find_set(parents[x])  # 경로 압축
        return parents[x]

    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)
        if root_x == root_y:
            return
        # 더 작은 루트노트에 합친다.
        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y

    cnt = 0 
    total = 0
    for weight, u, v in edges:
        # 싸이클이 없다면
        if find_set(u) != find_set(v):
            cnt += 1
            total += weight
            union(u, v)
            if cnt == V - 1: break
    return total