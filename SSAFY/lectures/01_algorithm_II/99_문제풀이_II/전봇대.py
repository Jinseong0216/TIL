T = int(input())
for tc in range(1, T+1):
    N = int(input())

    ab = [list(map(int, input().split())) for _ in range(N)]

    ab.sort()
    cnt = 0         # 교차 수
    for i in range(1, N):
        for j in range(i):
            if ab[j][1] > ab[i][1]: # a가 더 아래있지만 b가 더 높으면 교차점
                cnt += 1

    print(f'#{tc} {cnt}')