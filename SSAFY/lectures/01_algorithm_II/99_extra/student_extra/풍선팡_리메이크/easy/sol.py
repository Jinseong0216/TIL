import sys
sys.stdin = open('input.txt')


def search(direction):
    count = 0
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            count += data[nx][ny]
    # print(count)
    return count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for x in range(N):
        for y in range(M):
            tmp = data[x][y]
            if data[x][y] % 2:
                tmp += search([[-1, -1], [-1, 1], [1, -1], [1, 1]])
            else:
                tmp += search([[-1, 0], [1, 0], [0, -1], [0, 1]])
            if result < tmp:
                result = tmp
    print(f'#{tc} {result}')