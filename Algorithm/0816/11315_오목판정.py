import sys
sys.stdin = open('input_11315.txt', 'r')

def function(i,j):
    global ans

    dij = [[1, 0], [0, 1], [1, 1], [-1, 1]]
    for di, dj in dij:
        cnt = 1           # 현재 오목알의 수
        cnt_1 = cnt_2 = 0 # [di,dj], [-di, -dj] 방향의 연속된 오목알의 수
        while cnt < 5:
            ni, nj = i + (cnt_1+1)*di, j + (cnt_1+1)*dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N: break # 인덱스 초과 거르기
            if grid[ni][nj] != 'o': break # 오목알이 아닌경우 멈추기
            cnt, cnt_1 = cnt+1, cnt_1+1

        while cnt < 5:
            ni, nj = i+(-1)*(cnt_2+1)*di, j+(-1)*(cnt_2+1)*dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N: break
            if grid[ni][nj] != 'o': break
            cnt, cnt_2 = cnt+1, cnt_2+1

        if cnt == 5: # 연속된 오목알이 5개인 경우
            ans = 1
            return


T = int(input())
for t in range(1, 1+T):
    N = int(input())
    grid = [input().strip() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                function(i, j)

    if ans: print(f'#{t} YES')
    else: print(f'#{t} NO')
