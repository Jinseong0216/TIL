# 1861. 정사각형 방
# dfs + 델타탐색 = ladder 문제와 같음.

for T in range(1, int(input())+1): # 테스트 케이스의 수
    N = int(input()) # 크기
    grid = [list(map(int, input().split())) for _ in range(N)] # 입력받기

    def dfs(start, now, length):
        global start_point, ans
        i, j = now # 현 위치

        dij = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 델타 탐색을 위한 delta
        for di, dj in dij:
            ni, nj = i+di, j+dj
            if ni<0 or nj<0 or ni>=N or nj>=N: continue # 인덱스 초과 거르기
            if grid[ni][nj] == grid[i][j]+1: dfs(start, [ni, nj], length+1) # 정확히 1 큰 장소로 이동

        if ans <= length: # 현재 길이가 발견한 길이보다 길다면 업데이트
            if ans == length: start_point = min(start_point, start) # 시작 위치 업데이트
            else: start_point, ans = start, length
            return

    start_point, ans = N*N+1, 0
    for idx in range(N):
        for jdx in range(N):
            flag = 1
            dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 델타 탐색을 위한 delta
            for di, dj in dij:
                ni, nj = idx + di, jdx + dj
                if ni < 0 or nj < 0 or ni >= N or nj >= N: continue  # 인덱스 초과 거르기
                if grid[ni][nj] == grid[idx][jdx] - 1:  # 정확히 1 작은애가 있으면 탐색X
                    flag = 0
                    break
            if flag: dfs(grid[idx][jdx], [idx, jdx], 1)
    print(f'#{T}', start_point, ans)