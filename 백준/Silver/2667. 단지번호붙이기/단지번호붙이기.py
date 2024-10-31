N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []

def dfs(i, j):
    stack = [(i, j)]
    population = 0
    while stack:
        ci, cj = stack.pop()
        if visited[ci][cj]:
            continue
        visited[ci][cj] = 1
        population += 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and grid[ni][nj] == 1:
                stack.append((ni, nj))
    return population

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            ans.append(dfs(i, j))

ans.sort()
print(len(ans))
for p in ans:
    print(p)
