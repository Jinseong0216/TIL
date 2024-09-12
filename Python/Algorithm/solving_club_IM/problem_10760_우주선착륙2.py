import sys

sys.stdin = open('input10760.txt')

T = int(input())

for t in range(1, 1+T):
    N, M = map(int, input().split())
    grid = [[10]*(M+2)] + \
           [[10] + list(map(int, input().split())) + [10] for _ in range(N)] + \
           [[10]*(M+2)]
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            nearby = grid[i-1][j-1:j+2] + grid[i][j-1:j+2] + grid[i+1][j-1:j+2]
            how_many = sum(1 for height in nearby if height < grid[i][j])
            if 3 < how_many:
                cnt += 1
    print(f'#{t}', cnt)