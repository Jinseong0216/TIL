import sys
import copy
import pprint

sys.stdin = open('input.txt', 'r')

Test_case_num = int(input())
for T in range(1, Test_case_num+1):
    N, M, K = map(int, input().split())
    grid = []
    for _ in range(N):
        temp = []
        for d in list(map(int, input().split())):
            if d == 0:
                temp.append([0, 0, -1])
            else:
                temp.append([d, d, 3])
        grid.append(temp)

    dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def function(hour, n, m):
        global grid
        if hour == 0:
            cnt = 0
            for i in range(n):
                for j in range(m):
                    cnt += (grid[i][j][2] != -1)
            return cnt

        new_data = [[[0, 0, -1] for _ in range(m+2)] for _ in range(n+2)]
        # (남은 시간, 생명력수치, 상태) -1 = 세포 없음 / 0 죽은 상태 /1 활성 / 2 비활성 / 3 방금들어옴

        for i in range(n):
            for j in range(m):
                time, level, status = grid[i][j]

                if status == 1 and time == 0: status = 0
                elif status == 1:
                    time = time - 1
                    for di, dj in dij:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj][2] == -1:
                            if new_data[ni + 1][nj + 1][2] == -1:
                                new_data[ni + 1][nj + 1] = [level, level, 3]
                            elif new_data[ni + 1][nj + 1][2] == 3:
                                if new_data[ni + 1][nj + 1][1] < level:
                                    new_data[ni + 1][nj + 1] = [level, level, 3]
                        if not (0 <= ni < N and 0 <= nj < M):
                            new_data[ni + 1][nj + 1] = [level, level, 3]

                elif status == 2 and time == 1: time, status = level, 1
                elif status == 2: time = time - 1

                elif status == 3 and level == 1: status = 1
                elif status == 3: time, status = time-1, 2

                new_data[i + 1][j + 1] = [time, level, status]

        grid = new_data

        if hour == 1:
            function(hour-1, n, m)
        else:
            function(hour-1, n+2, m+2)


    ans = function(K, N, M)
    print(f'#{T} {ans}')
