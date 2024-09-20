import sys
sys.stdin = open('input.txt')


def search():
    changes = 0  # 교환 횟수
    current = 0  # 현재 위치
    max_reach = stations[0]  # 현재 위치에서 최대 도달 가능 정류장 수

    while current + max_reach < N - 1:
        # 다음으로 도달할 수 있는 가장 멀리 있는 정류장을 찾음
        next_reach = max(range(current + 1, current + max_reach + 1), key=lambda x: x + M[x])
        current = next_reach
        max_reach = M[current]
        changes += 1

    return changes

T = int(input())
for tc in range(1, T+1):
    N, *stations = list(map(int, input().split()))

    result = 0                  # 교환 횟수
    now = 0                     # 현재 위치
    max_reach = stations[0]     # 현재 위치에서 최대 도달 가능 정류장 수

    while now + max_reach < N - 1:
        # 다음으로 도달할 수 있는 가장 멀리 있는 정류장을 찾음
        next_reach = max(range(now + 1, now + max_reach + 1), key=lambda x: x + stations[x])
        now = next_reach
        max_reach = stations[now]
        result += 1

    print(f'#{tc} {result}')
