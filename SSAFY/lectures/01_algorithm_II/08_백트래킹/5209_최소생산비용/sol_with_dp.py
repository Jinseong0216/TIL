import sys
sys.stdin = open('input.txt')

def search(data, N):
    # 모든 가능한 상태 (2^N 개)
    dp = [[15*99] * (N+1) for _ in range(1 << N+1)]
    dp[0][0] = 0  # 초기 상태 (아무 공장도 선택하지 않음)

    for mask in range(1 << N):
        for i in range(N):
            if dp[mask][i] == 15*99:
                continue
            for j in range(N):
                if not (mask & (1 << j)):  # 공장 j가 선택되지 않은 경우
                    new_mask = mask | (1 << j)
                    dp[new_mask][i + 1] = min(dp[new_mask][i + 1], dp[mask][i] + data[i][j])

    # 최종 상태 (모든 공장을 선택했을 때)
    return min(dp[(1 << N) - 1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = search(data, N)
    print(f'#{tc} {result}')
