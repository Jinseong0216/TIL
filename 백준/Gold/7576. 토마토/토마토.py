from collections import deque

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

starting_list = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == 1]
day = [[-1 if grid[i][j] != -1 else 0 for j in range(M)] for i in range(N)]
def bfs():
    queue = deque(starting_list)
    for start in starting_list:
        day[start[0]][start[1]] = 0

    dij = [[0,1],[0,-1],[1,0],[-1,0]]
    while queue:
        i, j = queue.popleft()
        for di, dj in dij:
            ni, nj = i+di, j+dj
            if ni<0 or nj<0 or ni>=N or nj>=M: continue
            if grid[ni][nj] == -1 or grid[ni][nj] == 1: continue
            if day[ni][nj] == -1 or day[ni][nj] > day[i][j] + 1:
                day[ni][nj] = day[i][j] + 1
                queue.append((ni, nj))

bfs()
min_day = 1000
max_day = -1
for i in range(N):
    for j in range(M):
        if min_day > day[i][j]: min_day = day[i][j]
        if max_day < day[i][j]: max_day = day[i][j]

if min_day == -1: print(-1)
else: print(max_day)
