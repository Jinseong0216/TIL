import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    result = B  # 충분히 높은 타워와 B의 크기 차

    # 만들 수 있는 모든 경우의 수 2^N
    for i in range(2**N):
        top = 0     # 현재 경우의 수에서 만들어질 탑의 높이
        for j in range(N):  # 모든 요소에 대해
            if i & (1<<j):  # i번째 경우의 수에 j번째 값이 사용되는지 여부 확인
                top += data[j]      # 사용된다면 값 누적
        # 누적한 값의 높이가 B 이상이면서,
        if top >= B and result >= top - B:
            # 누적한 값과 B의 차가 가장 적은 값을 result에 할당
            result = top - B
    print(f'#{tc} {result}')

