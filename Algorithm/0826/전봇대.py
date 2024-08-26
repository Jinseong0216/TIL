T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for start, end in info:
        for S, E in info:
            if start < S and end > E: ans += 1

    print(f'#{tc} {ans}')
