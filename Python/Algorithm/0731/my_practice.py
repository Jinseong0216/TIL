for t in range(1, 11):
    dummy_input = input()

    grid = [list(map(int, input().split())) for _ in range(100)]
    sums = [sum(grid[i]) for i in range(100)]
    sums += [sum(grid[i][j] for i in range(100)) for j in range(100)]
    sums += [sum(grid[i][i] for i in range(100)), sum(grid[i][99-i] for i in range(100))]
    print(f'#{t}', max(sums))
