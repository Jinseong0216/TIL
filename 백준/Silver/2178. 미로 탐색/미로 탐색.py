import sys
from collections import deque
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
start, end = (0, 0), (N-1, M-1)


def bfs():
    que = deque([[0, 0]])
    distance = [[-1]*M for _ in range(N)]
    distance[0][0] = 1

    while que:
        i, j = que.popleft()

        dij = [[0,1],[0,-1],[1,0],[-1,0]]
        for di, dj in dij:
            ni, nj = i+di, j+dj
            if ni<0 or nj<0 or ni>=N or nj>=M: continue
            if grid[ni][nj] == 0: continue
            if distance[ni][nj] == -1:
                distance[ni][nj] = distance[i][j] + 1
                que.append((ni, nj))
            # if distance[ni][nj] != -1 and distance[ni][nj] > distance[i][j] + 1:
            #     distance[ni][nj] = distance[i][j] + 1
            #     que.append((ni, nj))

        if (i, j) == end:
            return distance[N-1][M-1]


ans = bfs()
print(ans)

