import sys
sys.stdin = open('input.txt')

from collections import deque

#     상  하  좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def search(x, y):
    # 해당 위치에서 q로 탐색
    # 첫 시작방도 이동으로 간주하므로 1칸으로 표기
    q = deque([(x, y, 1)])
    while q:
        x, y, cnt = q.popleft()
        for k in range(4):  # 4방향에 대해서
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위를 벗어나지 않고, 원본 위치보다 정확히 1큰 경우,
            if 0 <= nx < N and 0 <= ny < N and data[x][y] + 1 == data[nx][ny]:
                q.append((nx, ny, cnt+1))   # 다음 위치도 조사 대상에 삽입
    # 모든 조사를 마친 후 결과 반환
    return cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = []     # 각 방별 결과물 취합.

    # 전수 조사
    for i in range(N):
        for j in range(N):
            # data[i][j]의 방 번호와 i, j번째 위치에서 탐색한 결과 누적 이동수를 result에 추가
            result.append([data[i][j], search(i, j)])

    # 누적 이동수를 기준으로 내림차순 정렬후, 방 번호로 오름차순 정렬
    result.sort(key=lambda x: (-x[1], x[0]))
    print(f'#{tc}', *result[0])
