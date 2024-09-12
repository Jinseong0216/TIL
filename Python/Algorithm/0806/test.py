# 최대 길이 64
# 지나간 온 길을 25로 만들면 다시 못감
# 델타 탐색으로 가기
# 0. 가장 높은 지점 찾기
# 
# 1. 가장 높은 지점기준으로 반복문
# 
# 2. 몇 번째에 공사를 할지 정하기 0 ~ 63
#     (공사 순서가 되기전에, 길이 막혔다면 그때 공사하면 됨)
#         3. 각 케이스별로 공사 높이를 를 정함 1~k 
#         4. 델타 탐색으로 지나가기 + 길이 구함


T = 1
for t in range(1, T+1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    M = max(max(grid[i]) for i in range(N))                                     # 최대 높이이자, 동시에 최대 길이
    start_pt = [(i,j) for i in range(N) for j in range(N) if grid[i][j] == M]
    max_len = 0
    conduct = 1
    for s_pt in start_pt:
        for when_conduct in range()
    