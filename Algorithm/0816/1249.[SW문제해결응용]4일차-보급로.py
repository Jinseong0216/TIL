# 1249. [S/W 문제해결 응용] 4일차 - 보급로
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


for C in range(1, int(input()) + 1):  # 테스트케이스 수
    N = int(input())  # 도로의 크기
    grid = [list(map(int, input().strip())) for _ in range(N)]


    def bfs():
        queue = deque([[0, 0]])
        distance = [[-1] * N for _ in range(N)]
        distance[0][0] = grid[0][0]

        dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            i, j = queue.popleft()
            for di, dj in dij:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= N or nj >= N: continue # 인덱스 범위초과 체크
                # 더 효율적인 경로가 존재한다면, 해당 경로에서 다시 인접 노드를 큐에 추가해서 확인해야 함!
                if distance[ni][nj] != -1 and distance[ni][nj] > distance[i][j] + grid[ni][nj]:
                    distance[ni][nj] = distance[i][j] + grid[ni][nj]    # 최소거리 업데이트
                    queue.append([ni, nj])  # 노드를 큐에 추가
                    continue
                elif distance[ni][nj] == -1:    # 가보지 않은 노드의 경우
                    distance[ni][nj] = distance[i][j] + grid[ni][nj]    # 최소거리 업데이트
                    queue.append([ni, nj])  # 노드를 큐에 추가
        return distance[-1][-1]     # [-1, -1]의 최소 경로를 반환

    ans = bfs()
    print(f'#{C} {ans}')


# for C in range(1, int(input()) + 1):  # 테스트케이스 수
#     N = int(input())  # 도로의 크기
#     grid = [list(map(int, input().strip())) for _ in range(N)]
#
#
#     def dfs(v, visited, dist):
#         global min_dist
#
#         i, j = v
#         if [i, j] == end:
#             min_dist = min(min_dist, dist)
#             return
#
#         dij = [[0, 1], [1, 0]]
#         for di, dj in dij:
#             ni, nj = i+di, j+dj
#             if ni < 0 or nj < 0 or ni >= N or nj >= N:
#                 continue
#             if visited[ni][nj]:
#                 continue
#             visited[ni][nj] = True
#             dfs([ni, nj], visited, dist+grid[ni][nj])
#             visited[ni][nj] = False
#
#
#     start, end = [0, 0], [N - 1, N - 1]
#     visited = [[False] * N for _ in range(N)]
#     visited[0][0] = True
#     min_dist = 0
#
#     dfs(start, visited, grid[0][0])
#     print(min_dist)

    # 위치      VST     dist
    # 0,0      0,0     grid[0][0]
    # 0,1      0,0     grid[0][0]+grid[0][1]
    #          0,1