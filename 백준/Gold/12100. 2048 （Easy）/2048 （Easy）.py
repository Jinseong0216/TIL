# from pprint import pprint 

N = int(input())
grid = [list(map(lambda x: (int(x), False), input().split())) for _ in range(N)]
ans = max(grid[i][j][0] for i in range(N) for j in range(N))

def push(origin_grid, pivot, direction, cnt):
    global ans
    
    if cnt == 5: return
    if pivot == 'column':
        origin_grid = [[origin_grid[i][j] for i in range(N)] for j in range(N)]
    n_grid = []
    for i in range(N):
        n_row = []
        if direction == 1:
            j = 0
            while j < N:
                if origin_grid[i][j][0] == 0:
                    j += 1
                elif j == N-1: 
                    n_row.append(origin_grid[i][j])
                    j += 1
                else:
                    num, is_combined = origin_grid[i][j]
                    if not is_combined: 
                        for k in range(j+1, N):
                            if origin_grid[i][k][0]: break

                        if origin_grid[i][k][0] == num and origin_grid[i][k][1] == False:
                            n_row.append([2*origin_grid[i][j][0], False])
                            if ans < 2*origin_grid[i][j][0]: ans = 2*origin_grid[i][j][0]
                            j = k+1
                        else:
                            n_row.append(origin_grid[i][j])
                            j = k
                    else:
                        n_row.append(origin_grid[i][j])
                        j += 1
            L = len(n_row)
            if L < N: n_row = n_row + [(0, False)]*(N-L)
        else:
            j = N-1
            while j >= 0:
                if origin_grid[i][j][0] == 0:
                    j -= 1
                elif j == 0: 
                    n_row.append(origin_grid[i][j])
                    j -= 1
                else:
                    num, is_combined = origin_grid[i][j]
                    if not is_combined: 
                        for k in range(j-1, -1, -1):
                            if origin_grid[i][k][0]: break

                        if origin_grid[i][k][0] == num and origin_grid[i][k][1] == False:
                            n_row.append([2*origin_grid[i][j][0], False])
                            if ans < 2*origin_grid[i][j][0]: ans = 2*origin_grid[i][j][0]
                            j = k-1
                        else:
                            n_row.append(origin_grid[i][j])
                            j = k
                    else:
                        n_row.append(origin_grid[i][j])
                        j -= 1
            L = len(n_row)
            if L < N: n_row = n_row + [(0, False)]*(N-L)
            n_row = n_row[::-1]
        n_grid.append(n_row)
    
    push(n_grid, 'row', 1, cnt+1)
    push(n_grid, 'row', 2, cnt+1)
    push(n_grid, 'column', 1, cnt+1)
    push(n_grid, 'column', 2, cnt+1)
    return 


push(grid, 'row', 1, 0)
push(grid, 'row', 2, 0)
push(grid, 'column', 1, 0)
push(grid, 'column', 2, 0)

print(ans)

