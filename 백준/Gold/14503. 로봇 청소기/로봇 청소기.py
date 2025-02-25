N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 (반시계 방향)
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0 

while True:
    # 현재 위치 청소
    if grid[r][c] == 0:
        grid[r][c] = -1
        count += 1

    # 4방향 모두 탐색
    found = False
    for i in range(1, 5):
        n_d = (d - i) % 4  # 반시계 방향 회전
        n_r, n_c = r + direction[n_d][0], c + direction[n_d][1]
        
        if 0 <= n_r < N and 0 <= n_c < M and grid[n_r][n_c] == 0:
            r, c, d = n_r, n_c, n_d  # 이동 및 방향 변경
            found = True
            break
    
    # 청소할 곳이 없는 경우 후진
    if not found:
        n_r, n_c = r - direction[d][0], c - direction[d][1]
        if 0 <= n_r < N and 0 <= n_c < M and grid[n_r][n_c] != 1:
            r, c = n_r, n_c  # 후진
        else:
            break  # 후진할 수 없으면 작동 종료

print(count)
