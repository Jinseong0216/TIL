import sys
sys.stdin = open('input.txt')

board = [[0]*1001 for _ in range(1001)]
N = int(input())
for num in range(1, N+1):
    x, y, d, r = map(int, input().split())
    for i in range(x, x+d):
        for j in range(y, y+d):
            board[i][j] = num

for k in range(1, N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == k:
                cnt += 1
    print(cnt)