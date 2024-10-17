import sys
input = sys.stdin.readline

N = int(input())
grid = [[0]*1001 for _ in range(1001)]
for num in range(1, N+1):
    x_LB, y_LB, width, height = map(int, input().split())
    for idx in range(y_LB, y_LB+height):
        grid[idx][x_LB: x_LB+width] = [num]*width

ans = [0]*(N+1)
for idx in range(1001):
    for jdx in range(1001):
        ans[grid[idx][jdx]] += 1

for num in range(1, N+1):
    print(ans[num])
