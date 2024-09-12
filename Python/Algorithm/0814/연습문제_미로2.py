# BFS로  풀기
#
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
#         global ans, cnt, cnt_2
#         dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         visited = [[False]*m for _ in range(n)]
#
#         que = deque([start])
#         visited[start[0]][start[1]] = True
#
#
#         while que:
#             cnt += 1
#             i, j = que.popleft()
#             print(que)
#             if len(que) > cnt_2: cnt_2 = len(que)
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
#                 cnt += 1
#                 que.append([ni, nj])
#                 visited[ni][nj] = True
#
#                 if (ni, nj) == end:
#                     ans = 1
#                     return
#
#     ans = 0
#     cnt = 0
#     cnt_2 = 0
#     bfs(grid, start, 100, 100)
#     print(f'#{T} {ans} {cnt} {cnt_2}')

# DFS로  풀기
import time
import sys

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(2648)

start = time.time()
print(start)
for t in range(1, 11):
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

        if vertex == end:
            ans = 1
            return

        dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for di, dj in dij:
            ni, nj = vertex[0]+di, vertex[1]+dj
            if 0 > ni or ni >= n or 0 > nj or nj >= m:
                continue
            if visited[ni][nj]:
                continue
            if grid[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            dfs([ni, nj], grid, visited, n, m)
            visited[ni][nj] = False


    visited = [[False] * 100 for _ in range(100)]
    visited[start[0]][start[1]] = True
    ans = 0
    dfs(start, grid, visited, 100, 100)
    print(f'#{T} {ans}')

end = time.time()

print(start - end)