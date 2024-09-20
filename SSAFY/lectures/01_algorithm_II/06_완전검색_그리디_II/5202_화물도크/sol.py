import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 종료 시간 기준 오름차순
    data.sort(key=lambda x: x[1])

    result = 1
    end_time = data[0][1]
    for i in range(1, N):
        if data[i][0] >= end_time:  # 다음 시작 시간이 종료시간 보다 크다면,
            result += 1
            end_time = data[i][1]   # 종료시간 갱신.
    print(f'#{tc} {result}')
