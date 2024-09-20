import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS():
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = 0

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] <= visited[N - 1][N - 1]:
                if data[x][y] >= data[nx][ny]:
                    if visited[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        Q.append((nx, ny))
                elif data[x][y] < data[nx][ny]:
                    if visited[nx][ny] > visited[x][y] + 1 + (data[nx][ny] - data[x][y]):
                        visited[nx][ny] = (visited[x][y] + 1 + (data[nx][ny] - data[x][y]))
                        Q.append((nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_num = sum(sum(data, [])) + N + 1
    visited = [[min_num for _ in range(N)] for _ in range(N)]

    BFS()
    print(f'#{tc} {visited[N-1][N-1]}')