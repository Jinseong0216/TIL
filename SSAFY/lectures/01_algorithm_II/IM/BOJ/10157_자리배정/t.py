import sys
sys.stdin = open("input.txt")

del_row = [0,1,0,-1]
del_col = [1,0,-1,0]
C, R = map(int,input().split()) # 가로 C, 세로 R
K = int(input()) # 관객번호 수
stage = [[0] * (C+1) for _ in range(R+1)] # 공연 무대
for s in stage:
    print(s)
print()
pan = 1
move, row, col  = 0, 1, 1
stage[row][col] = pan
x, y = 0, 0
if C * R < K:
    print(0)
else:
    while pan <= K:
        x = row + del_row[move]
        y = col + del_col[move]
        if 0 < x <= C and 0 < y <= R:
            if stage[y][x] == 0: # 아직 안갔으면
                stage[y][x] = pan # 팬으로 줌
                row += del_row[move] # 그만큼 전진함
                col += del_col[move] # 그만큼 전진함
                pan += 1
            else:
                move = (move+1) % 4
        else:
            move = (move + 1) % 4
for s in stage:
    print(s)
print(x-1, y)