for t in range(1,11):
    dummy_input = input()
    grid1 = [input().strip() for _ in range(100)]
    grid2 = [ list(grid1[j][i] for j in range(100)) for i in range(100) ]
    grid = grid1 + grid2
 
    M = k = 1
    for i in range(200):
        k = M + 1
        while k < M + 3:
            for j in range(100-k+1):
                if grid[i][j:j+k] == grid[i][j:j+k][::-1]:
                    M = k
                    k += 1
                    break
            k += 1
    print(f'#{t} {M}')


def pal_len(grid):
    for k in range(100,0,-1):
        for i in range(200):
            for j in range(100 - k + 1):
                if grid[i][j:j + k] == grid[i][j:j + k][::-1]:
                    return k
 
for _ in range(1, 11):
    t = int(input())
    grid1 = [input().strip() for _ in range(100)]
    grid2 = [''.join(grid1[j][i] for j in range(100)) for i in range(100)]
    grid = grid1 + grid2
 
    ans = pal_len(grid)
    print(f'#{t} {ans}')

