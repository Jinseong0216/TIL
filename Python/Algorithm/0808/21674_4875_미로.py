T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    grid = [list(input().strip()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '2':
                start_x, start_y = i, j
                break
    visited = [[0]*N for _ in range(N)]
    result = 0

    def DFS(x, y):
        global result, visited

        if grid[x][y] == '3':
            result = 1
            return

        visited[x][y] = 1
        dxy = [[0, 1], [0,-1], [1,0], [-1,0]]
        for dx, dy in dxy:
            nx, ny = x +dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] != '1' and visited[nx][ny] == 0:
                    DFS(nx,ny)
        return
    DFS(start_x, start_y)
    print(f'#{t} {result}')