import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    # x, y 위치를 기준으로 상하 좌우를 탐색.
    # 탐색 하는 이유가 뭘까?
    for k in range(4):
        for l in range(1, N):
            nx = x + (dx[k] * l)
            ny = y + (dy[k] * l)
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 0:
                data[nx][ny] = 1
            else:
            # if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 1:
                break

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 0은 복도, 1은 기둥, 2는 경비병?
    data = [list(map(int, input().split())) for _ in range(N)]

    # 경비병의 위치를 전수 조사
    for x in range(N):
        for y in range(N):
            if data[x][y] == 2:
                search(x, y)
                # for k in range(4):
                #     for l in range(1, N):
                #         nx = x + (dx[k] * l)
                #         ny = y + (dy[k] * l)
                #         if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 0:
                #             data[nx][ny] = 1
                #         else:
                #             # if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 1:
                #             break
    result = 0
    for x in range(N):
        for y in range(N):
            if data[x][y] == 0:
                result += 1
    print(f'#{tc} {result}')









