T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    counts = []
    for _ in range(N):
        colors = input()
        counts += [[M - colors.count('W'), M - colors.count('B'), M - colors.count('R')]]

    min_num = N*M
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            num = sum(counts[k][0] for k in range(i+1))
            num += sum(counts[k][1] for k in range(i+1, j+1))
            num += sum(counts[k][2] for k in range(j+1, N))
            min_num = min(min_num, num)

    print(f'#{t}', min_num)