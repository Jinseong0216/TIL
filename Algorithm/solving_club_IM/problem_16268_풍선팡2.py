import sys

sys.stdin = open('input16268.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [[0]*(M+2)] + \
           [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + \
           [[0]*(M+2)]
    max_count = 0
    for i in range(1, N + 1):
        for j in range(1, M+1):
            max_count = max(max_count, sum(grid[i][j-1:j+2]) + grid[i-1][j] + grid[i+1][j])

    print(f'#{t}', max_count)
