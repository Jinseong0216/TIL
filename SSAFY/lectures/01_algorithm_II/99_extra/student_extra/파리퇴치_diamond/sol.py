import sys
sys.stdin = open('input.txt')


from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, cnt):
    global result
    visited = [[0] * N for _ in range(N)]
    q = deque([(x, y, cnt)])
    tmp = data[x][y]
    visited[x][y] = 1
    while q:
        x, y, cnt = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if cnt < M//2:
                    tmp += data[nx][ny]
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt+1))
    if result < tmp:
        result = tmp

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for x in range(N):
        for y in range(N):
            BFS(x, y, 0)
    print(f'#{tc} {result}')