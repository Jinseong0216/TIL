# import sys
# sys.stdin = open('input.txt', 'r')
# sys.setrecursionlimit(10000)
#
# for t in range(1, 11):
#     T = int(input())
#
#     grid, start = [], -1
#     for i in range(100):
#         temp = list(map(int, input()))
#         for j in range(100):
#             if temp[j] == 2:
#                 start = (i, j)
#         grid.append(temp)
#
#     dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#
#     def dfs(st, visited):
#         global ans
#
#         i, j = st[0], st[1]
#         if grid[i][j] == 3:
#             ans = 1
#
#         visited[i][j] = True
#         for di, dj in dij:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < 100 and 0 <= nj < 100 and grid[ni][nj] != 1 and (not visited[ni][nj]):
#                 dfs((ni, nj), visited)
#
#
#     ans = 0
#     visited = [[False for _ in range(100)] for _ in range(100)]
#     dfs(start, visited)
#     print(f'{T} {ans}')


# ====================================================================================
# 미로문제는 일반적으로 BFS가 맞음 DFS아님 (최단거리면 무조건 BFS임!!!!!)

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


for t in range(1, 2):
    T = int(input())

    grid, start, end = [], -1, -1
    for i in range(100):
        temp = list(map(int, input()))
        for j in range(100):
            if temp[j] == 2:
                start = (i, j)
            elif temp[j] == 3:
                end = (i,j)
        grid.append(temp)

    dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    que = deque([start])
    ans = 0
    visited = [[0]*100 for _ in range(100)]
    visited[start[0]][start[1]] = 1

    while que:
        i, j = que.popleft()

        for di, dj in dij:
            ni, nj = i+di, j+dj
            if 0 > ni or ni >= 100 or 0 > nj or nj >= 100: continue
            if visited[ni][nj] == 1: continue
            if grid[ni][nj] == 1: continue
            que.append((ni, nj))

            if (ni, nj) == end: ans = 1



    print(ans)


def bfs(st, n, m):
    dxy = [[1,0], [0,1], [-1,0], [0, -1]]

    visited = [[False] * m for _ in range(n)]

    # 큐 안에는 [x 좌표, y좌표, 이동 시간 ]
    queue = deque([0, 0, 0])
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in dxy:
            # 갈 수 있느 곳이라면 (nx, ny, n_dist) 를 저장한다.
            nx, ny = x + dx, y + dy
            n_dist = dist + 1

            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue

            # 방문한 적이 있는 경우
            if visited[nx][ny]:
                continue

            # 도로가 아닌 경우
            if road[nx][ny] == 0:
                continue

            queue.append((nx, ny, n_dist))
            visited[nx][ny] = True

            if nx == n-1 and ny == m-1:
                return n_dist
    return -1
