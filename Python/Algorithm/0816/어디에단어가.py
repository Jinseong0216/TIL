T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    Matrix_1 = [list(map(int, input().split())) for _ in range(N)]
    Matrix_2 = [[Matrix_1[j][i] for j in range(N)] for i in range(N)]

    for n in range(N):
        row_1, row_2 = [0] + Matrix_1[n] + [0], [0] + Matrix_2[n] + [0]
        tg = [0] + [1 for j in range(K)] + [0]

        for i in range(1, N - K + 2):
            r1 = row_1[i - 1:i + K + 1]
            r2 = row_2[i - 1:i + K + 1]
            cnt += (r1 == tg) + (r2 == tg)
    print(f'#{t} {cnt}')