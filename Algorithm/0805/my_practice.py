ans = []
for t in range(1,2):
    dummy_input = input()
    grid1 = [input().strip() for _ in range(100)]
    grid2 = [ list(grid1[j][i] for j in range(100)) for i in range(100) ]
    grid = grid1 + grid2

    M = 0
    k = M + 1
    for i in range(200):
        while k < M + 3:
            for j in range(100-k+1):
                if grid[i][j:j+k] == grid[i][j:j+k][::-1]:
                    M = k
                    break
            k += 1
        k = M + 1
    ans.append(f'#{t} {M}')

print(ans)
        