from collections import deque

for T in range(1, int(input())+1):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    distance = [[-1] * N for _ in range(N)]

    def bfs():
        queue = deque([start])
        distance[start[0]][start[1]] = 0
        dij = [[-1, -2], [-1, 2], [1, -2], [1, 2], [-2, -1], [-2, 1], [2, -1], [2, 1]]

        while queue:
            i, j = queue.popleft()
            for di, dj in dij:
                ni, nj = i+di, j+dj
                if ni<0 or nj<0 or ni>=N or nj>= N: continue
                if distance[ni][nj] == -1:
                    distance[ni][nj] = distance[i][j]+1
                    queue.append((ni, nj))
            if [i, j] == end: break
        return

    bfs()
    print(distance[end[0]][end[1]])