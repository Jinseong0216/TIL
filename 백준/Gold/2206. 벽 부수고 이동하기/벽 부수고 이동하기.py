import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
dist = [[[0, 0] for _ in range(M)] for _ in range(N)] # 최단거리 (벽 부순경우, 안 부순경우)


def bfs():
    queue = deque([(0, 0, 0)])
    dist[0][0][0] = 1

    dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while queue:
        idx, jdx, flag = queue.popleft()

        if (idx, jdx) == (N-1, M-1): break # 목표지점 도달시 종료.

        for di, dj in dij:
            ni, nj = idx+di, jdx+dj
            if ni<0 or nj<0 or ni>= N or nj>=M: continue # 인덱스 초과시 패스

            if grid[ni][nj] == 0: # 벽 아닌경우
                past_flag = (1 if grid[idx][jdx] == 1 else flag) # 이전에 벽을 부쉈다면 past_flag = 1 안 부쉈다면 0
                if dist[ni][nj][flag] == 0 or dist[ni][nj][flag] > dist[idx][jdx][past_flag] + 1: # 최단거리 업데이트 가능하면
                    dist[ni][nj][flag] = dist[idx][jdx][flag] + 1 # 업데이트 하고
                    queue.append((ni, nj, flag)) # 큐에 넣기

            elif grid[ni][nj] == 1 and flag == 0: # 가는 방향이 벽이면서, 아직까지 벽을 부순적이 없다면
                if dist[ni][nj][1] == 0 or dist[ni][nj][1] > dist[idx][jdx][0] + 1: # 벽을 부쉈을 때, 최단거리 업데이트 가능하면
                    dist[ni][nj][1] = dist[idx][jdx][0] + 1 # 업데이트 하고
                    queue.append((ni, nj, 1)) # 큐에 넣기 + 벽을 부순적이 있다는 의미로 flag에 1 넣기


bfs()
if dist[N-1][M-1] == [0, 0]: print(-1)
else: print(min(x for x in dist[N-1][M-1] if x != 0))

