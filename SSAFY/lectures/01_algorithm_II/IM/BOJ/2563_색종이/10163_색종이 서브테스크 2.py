import sys
sys.stdin = open('input.txt')

board = [[0]*1001 for _ in range(1001)]
N = int(input())
for num in range(1, N+1):
    x, y, d, r = map(int, input().split())
    for i in range(x, x+d):
        board[i][y:y+r] = [num] * r

for k in range(1, N+1):
    cnt = 0
    for b in board:
        cnt += b.count(k)
    print(cnt)