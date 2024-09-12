T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    total = 0
    for x in range(N):
        for y in range(N):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (0 <= nx < N) and (0 <= ny < N):
                    total += abs(matrix[nx][ny] - matrix[x][y])
    print(f'#{t}', total)
