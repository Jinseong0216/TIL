# 20739 고대 유적 2

T = int(input())    # 문제 수
for tc in range(1, T+1):    # 문제 수 별 반복문 진행
    N, M = map(int, input().split())    # N=행의 길이, M=열의 길이
    grid = [list(map(int, input().split())) for _ in range(N)] # NxM 배열이 됨
    grid_2 = list(zip(*grid))   # MxN 배열이 됨
    longest = 0 # 발견한 유적의 최대 길이

    def fnct(grid, N, M):
        global longest

        for idx in range(N):
            # 유적의 길이 측정을 위함(초기값 0)
            jdx = now_len = 0
            # jdx가 M보다 작은 경우까지만
            while jdx < M:
                # 0인 경우 길이 초기화, jdx = jdx+1
                if grid[idx][jdx] == 0:
                    # 이전 발견했던 유적 길이가 2이상, longest보다 길다면
                    if longest < now_len and now_len >= 2: longest = now_len
                    jdx, now_len = jdx+1, 0
                    continue
                # 1인 경우, 길이=길이+1, jdx = jdx+1
                if grid[idx][jdx] == 1:
                    jdx, now_len = jdx+1, now_len+1
            # 마지막 인덱스까지 조회했는데, 이때 now_len의 길이가 0보다 큰 경우가 있음. 그 경우에도 비교 후 업데이트
            if longest < now_len and now_len >= 2: longest = now_len

    fnct(grid, N, M)
    fnct(grid_2, M, N)
    print(f'#{tc} {longest}')

