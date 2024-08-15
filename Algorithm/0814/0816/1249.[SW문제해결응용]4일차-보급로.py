# 1249. [S/W 문제해결 응용] 4일차 - 보급로
from collections import deque

for C in range(1, int(input()) + 1):  # 테스트케이스 수
    N = int(input())  # 도로의 크기
    grid = [list(map(int, input().strip())) for _ in range(N)]


    def bfs():
        queue = deque([[0, 0]])
        distance_1 = [[-1] * N for _ in range(N)]
        distance_1[0][0] = grid[0][0]

        dij = [[0, 1], [1, 0]]
        while queue:
            i, j = queue.popleft()
            for di, dj in dij:
                ni, nj = i + di, j + dj
                if ni + nj >= N: continue  # 인덱스 범위초과 체크
                if distance_1[ni][nj] != -1:
                    distance_1[ni][nj] = min(distance_1[i][j] + grid[ni][nj], distance_1[ni][nj])  # 최소거리 업데이트
                    continue
                if distance_1[ni][nj] == -1:
                    distance_1[ni][nj] = distance_1[i][j] + grid[ni][nj]  # 최소거리 업데이트
                    queue.append([ni, nj])

        queue = deque([[N - 1, N - 1]])
        distance_2 = [[-1] * N for _ in range(N)]
        distance_2[-1][-1] = grid[-1][-1]

        dij = [[0, -1], [-1, 0]]
        while queue:
            i, j = queue.popleft()
            for di, dj in dij:
                ni, nj = i + di, j + dj
                if ni + nj < N - 1: continue  # 인덱스 범위초과 체크

                distance_2[ni][nj] = min(distance_2[i][j] + grid[ni][nj], distance_2[ni][nj])  # 최소거리 업데이트
                continue
            if distance_2[ni][nj] == -1:
                distance_2[ni][nj] = distance_2[i][j] + grid[ni][nj]  # 최소거리 업데이트
                queue.append([ni, nj])


    min_dist = []
    for k in range(N):
        min_dist.append(distance_1[k][N - k - 1] + distance_2[k][N - k - 1] - grid[k][N - k - 1])
    return min(min_dist)

ans = bfs()
print(f'#{C} {ans}')