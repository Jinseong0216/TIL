import sys
input = sys.stdin.readline

def dfs(i, j):
    stack = [(i, j)]
    while stack:
        ci, cj = stack.pop()
        if visited[ci][cj]:
            continue
        visited[ci][cj] = 1
        for di, dj in dij:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and grid[ni][nj] == 1:
                stack.append((ni, nj))

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    for _ in range(K):
        jdx, idx = map(int, input().split())
        grid[idx][jdx] = 1

    visited = [[0] * M for _ in range(N)]
    ans = 0
    dij = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                ans += 1

    print(ans)
