# DFS로 풀기

# for t in range(1, 11):
#     T = int(input())
#
#     start = end = -1
#     grid = []
#     for i in range(16):
#         temp = list(map(int, input()))
#         for j in range(16):
#             if temp[j] == 2: start = (i, j)
#             elif temp[j] == 3: end = (i, j)
#         grid.append(temp)
#     visited = [[False for _ in range(16)] for _ in range(16)]
#     dij = [[0,1], [0, -1], [1, 0], [-1, 0]]
#
#
#     def dfs(st, visited):
#         global ans
#
#         i, j = st[0], st[1]
#         if grid[i][j] == 3: ans = 1
#
#         visited[i][j] = True
#         for di, dj in dij:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < 16 and 0 <= nj < 16 and grid[ni][nj] != 1 and (not visited[ni][nj]):
#                 dfs((ni, nj), visited)
#
#
#     ans = 0
#     dfs(start, visited)
#     print(f'{T} {ans}')

# BFS로  풀기
from collections import deque

for t in range(1, 11):
    T = int(input())

    start = end = -1
    grid = []
    for i in range(16):
        temp = list(map(int, input()))
        for j in range(16):
            if temp[j] == 2: start = (i, j)
            elif temp[j] == 3: end = (i, j)
        grid.append(temp)

    def bfs(grid, start, n, m):
        global ans
        dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False]*m for _ in range(n)]

        que = deque([start])
        visited[start[0]][start[1]] = True

        while que:
            i, j = que.popleft()

            for di, dj in dij:
                ni, nj = i+di, j+dj

                if 0 > ni or ni >= n or 0 > nj or nj >= m:
                    continue
                if visited[ni][nj]:
                    continue
                if grid[ni][nj] == 1:
                    continue

                que.append([ni, nj])
                visited[ni][nj] = True

                if (ni, nj) == end:
                    ans = 1
                    return

    ans = 0
    bfs(grid, start, 16, 16)
    print(f'#{T} {ans}')
