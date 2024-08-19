T = int(input())
for t in range(1, T+1):
    N = int(input())    # grid 사이즈
    grid = [list(map(int, input().split())) for _ in range(N)]

    C = 0
    island = []
    # 섬 위치 찾기
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                for j2 in range(j, N+1):
                    if j2 >= N or grid[i][j2] == 0: break
                y = j2-1
                if i != 0 and grid[i-1][j] == 1: continue
                if j != 0 and grid[i][j-1] == 1: continue
                for i2 in range(i, N+1):
                    if i2 >= N or grid[i2][j] == 0: break
                x = i2-1
                C = C + 1
                island.append([[a, b] for b in range(j, y+1) for a in range(i, x+1)])


    # 유효성 검사
    def is_valid(connection):
        possible = set(connection[0])
        for vt in range(1, C):
            if possible.intersection(set(connection[vt])):
                possible = possible.union(connection[vt])
        if len(possible) == C: return 1
        elif len(possible) == 1: return [0]
        else: return list((set(range(C))).difference(possible)) # 시작 할 점들



    def sol(grid, connection, price):
        global min_price

        next_vertex = is_valid(connection)
        if next_vertex == 1:
            if min_price > price:
                min_price = price
            return

        dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for cc in next_vertex:
            for i, j in island[cc]:
                for di, dj in dij:
                    new_grid = [grid[a][:] for a in range(N)]
                    ni, nj = i+di, j+dj
                    if ni<0 or nj<0 or ni>=N or nj>=N: continue
                    if grid[ni][nj] == 1 or grid[ni][nj] == 3: continue

                    new_price = price
                    flag = 0
                    while 0 <= ni < N and 0 <= nj < N:
                        if new_grid[ni][nj] == 1:
                            for idx in range(C):
                                if [ni, nj] in island[idx] and cc not in connection[idx]:
                                    new_connection = [connection[b][:] for b in range(C)]
                                    new_connection[idx].append(cc)
                                    new_connection[cc].append(idx)
                                    flag = 1
                            break
                        elif new_grid[ni][nj] == 3:
                            break
                        else:
                            new_grid[ni][nj] = 3
                            new_price = new_price + 1
                            ni, nj = ni+di, nj+dj
                    if flag:
                        sol(new_grid, new_connection, new_price)

    min_price = float('inf')
    connection = [[i] for i in range(C)]
    sol(grid, connection, 0)

    if min_price == float('inf'): min_price = -1
    print(f'#{t}', min_price)
