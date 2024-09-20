import sys

sys.stdin = open("input.txt")

dx = [1, 0, -1, 0]  # 십자 (짝수용) 를 위한 델타
dy = [0, 1, 0, -1]

rx = [1, 1, -1, -1]  # 대각선 (홀수용) 을 위한 델타
ry = [-1, 1, -1, 1]

T = int(input())

for idx in range(T):
    N, M = map(int, input().split())
    ballons = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(M):
            s = ballons[i][j]

            if s % 2 == 0:  # case 1) 선택한 풍선이 짝수인 경우
                for dt in range(4):
                    di = i + dx[dt]
                    dj = j + dy[dt]
                    if 0 <= di < N and 0 <= dj < M:
                        s += ballons[di][dj]
                if s > result:
                    result = s  # 짝수를 위한 십자 델타를 사용하여 최대값과 비교

            else:  # case 2) 선택한 풍선이 홀수인 경우
                for rt in range(4):
                    ri = i + rx[rt]
                    rj = j + ry[rt]
                    if 0 <= ri < N and 0 <= rj < M:
                        s += ballons[ri][rj]
                if s > result:
                    result = s  # 홀수를 위한 X 델타를 사용하여 최대값과 비교

    print(f"#{idx + 1} {result}")  # 출력