from collections import deque

M, N, H = map(int, input().split())
grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
starting_list = [(h, i, j) for h in range(H) for i in range(N) for j in range(M) if grid[h][i][j] == 1]
day = [[[-1 if grid[h][i][j] != -1 else 0 for j in range(M)] for i in range(N)] for h in range(H)]

def bfs():
    queue = deque(starting_list)
    for start in starting_list:
        day[start[0]][start[1]][start[2]] = 0

    dhij = [[1,0,0],[-1,0,0],[0,0,1],[0,0,-1],[0,1,0],[0,-1,0]]
    while queue:
        h, i, j = queue.popleft()
        for dh, di, dj in dhij:
            nh, ni, nj = h+dh, i+di, j+dj
            if nh<0 or ni<0 or nj<0 or nh>=H or ni>=N or nj>=M: continue
            if grid[nh][ni][nj] == -1 or grid[nh][ni][nj] == 1: continue
            if day[nh][ni][nj] == -1 or day[nh][ni][nj] > day[h][i][j] + 1:
                day[nh][ni][nj] = day[h][i][j] + 1
                queue.append((nh, ni, nj))

bfs()
min_day = 10000
max_day = -1
for h in range(H):
    for i in range(N):
        for j in range(M):
            if min_day > day[h][i][j]: min_day = day[h][i][j]
            if max_day < day[h][i][j]: max_day = day[h][i][j]

if min_day == -1: print(-1)
else: print(max_day)
