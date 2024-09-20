import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T+1):
    N, M, B = map(int, input().split())
    Bi = [list(map(int, input().split())) for _ in range(B)]
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            visited = [[0] * N for _ in range(N)]
            tmp = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    if not visited[x][y]:
                        tmp += data[x][y]
                        visited[x][y] = 1
                    if [x+1, y+1] in Bi:
                        #               좌상,     우상,     좌하,     우하
                        for dx, dy in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                tmp += data[nx][ny]

            if result < tmp:
                result = tmp
    print(f'#{tc} {result}')

