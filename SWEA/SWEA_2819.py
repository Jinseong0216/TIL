for T in range(1, int(input())+1):
    grid = [input().split() for _ in range(4)] # 수를 이어 붙이기 위해서 int아닌 str로 받음.

    def dfs(num, position, length):
        global ans

        if length == 7:
            ans.append(num)
            return

        i, j = position
        dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 델타 탐색을 위한 delta
        for di, dj in dij:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= 4 or nj >= 4: continue  # 인덱스 초과 거르기
            dfs(num+grid[ni][nj], [ni, nj], length+1)

    ans = []
    for i in range(4):
        for j in range(4):
            dfs(grid[i][j], [i, j], 1)
    print(f'#{T}', len(set(ans)))
