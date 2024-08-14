# BFS로  풀기

# import sys
# from collections import deque
#
# sys.stdin = open('input.txt', 'r')
#
# for t in range(1, 11):
#     T = int(input())
#
#     start = end = -1
#     grid = []
#     for i in range(100):
#         temp = list(map(int, input()))
#         for j in range(100):
#             if temp[j] == 2: start = (i, j)
#             elif temp[j] == 3: end = (i, j)
#         grid.append(temp)
#
#     def bfs(grid, start, n, m):
#         global ans
#         dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         visited = [[False]*m for _ in range(n)]
#
#         que = deque([start])
#         visited[start[0]][start[1]] = True
#
#         while que:
#             i, j = que.popleft()
#
#             for di, dj in dij:
#                 ni, nj = i+di, j+dj
#
#                 if 0 > ni or ni >= n or 0 > nj or nj >= m:
#                     continue
#                 if visited[ni][nj]:
#                     continue
#                 if grid[ni][nj] == 1:
#                     continue
#
#                 que.append([ni, nj])
#                 visited[ni][nj] = True
#
#                 if (ni, nj) == end:
#                     ans = 1
#                     return
#
#     ans = 0
#     bfs(grid, start, 100, 100)
#     print(f'#{T} {ans}')

# DFS로  풀기

import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 2):
    T = int(input())

    start = end = -1
    grid = []
    for i in range(100):
        temp = list(map(int, input()))
        for j in range(100):
            if temp[j] == 2: start = [i, j]
            elif temp[j] == 3: end = [i, j]
        grid.append(temp)


    def dfs(vertex, grid, visited, n, m):
        global ans
        print(vertex)
        if vertex == end:
            ans = 1
            return

        dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for di, dj in dij:
            ni, nj = i+di, j+dj
            if 0 > ni or ni >= n or 0 > nj or nj >= m:
                continue
            if visited[ni][nj]:
                continue
            if grid[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            dfs([ni, nj], grid, visited, n, m)
            visited[ni][nj] = False

    print(start)
    print(end)
    visited = [[False] * 100 for _ in range(100)]
    visited[start[0]][start[1]] = True
    ans = 0
    dfs(start, grid, visited, 100, 100)
    print(f'#{T} {ans}')
