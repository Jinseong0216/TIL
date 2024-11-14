from collections import deque
from itertools import product
from copy import copy

def solution(grid):
    N, M = len(grid), len(grid[0])
    red_visited, blue_visited = {}, {}
    red, blue, red_goal, blue_goal, turn = None, None, None, None, 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1: red = (i, j)
            elif grid[i][j] == 2: blue = (i, j)
            elif grid[i][j] == 3: red_goal = (i, j)
            elif grid[i][j] == 4: blue_goal = (i, j)

    red_visited[red] = True
    blue_visited[blue] = True
    q = deque([(red, blue, red_visited, blue_visited, turn)])

    while q:
        red, blue, red_visited, blue_visited, turn = q.popleft()
        if red == red_goal and blue==blue_goal: return turn
        red_candidates = [red]
        if red != red_goal:
            red_candidates = [
                (red[0]+red_di, red[1]+red_dj) 
                for red_di, red_dj 
                in [[0, 1], [0, -1], [1, 0], [-1, 0]]
                ]
        blue_candidates = [blue]
        if blue != blue_goal:
            blue_candidates = [
                (blue[0]+blue_di, blue[1]+blue_dj) 
                for blue_di, blue_dj 
                in [[0, 1], [0, -1], [1, 0], [-1, 0]]
                ]
        candidates = product(red_candidates, blue_candidates)

        for n_red, n_blue in candidates:
            # 같은 칸에 못감
            if n_red == n_blue: continue
            # 서로 위치교환 패스
            if n_red == blue and n_blue == red: continue
            # 인덱스 초과 패스
            if n_red[0]<0 or n_red[0]>=N or n_red[1]<0 or n_red[1]>=M: continue
            if n_blue[0]<0 or n_blue[0]>=N or n_blue[1]<0 or n_blue[1]>=M: continue
            # 벽 패스
            if grid[n_red[0]][n_red[1]] == 5: continue
            if grid[n_blue[0]][n_blue[1]] == 5: continue
            # 방문했으면 패스
            if red != n_red and red_visited.get(n_red, False): continue
            if blue != n_blue and blue_visited.get(n_blue, False): continue
            # 방문체크
            n_red_visited = copy(red_visited)
            n_red_visited[n_red] = True
            n_blue_visited = copy(blue_visited)
            n_blue_visited[n_blue] = True
            # 큐에 넣기
            q.append((n_red, n_blue, n_red_visited, n_blue_visited, turn+1))

    return 0