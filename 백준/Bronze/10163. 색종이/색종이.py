# 10163번 색종이

grid = [['0']*101 for _ in range(101)]
N = int(input())

for flag in range(1,1+N):
    x, y, dx, dy = map(int, input().split())
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            grid[i][j] = (str(flag) + 'sep' + grid[i][j])[:len(str(flag))+3]

areas = []
Cnts = [0] + [0]*N
for i in range(101):
    for j in range(101):
        Cnts[int(grid[i][j].split('sep')[0])] += 1

for i in range(1,1+N): print(Cnts[i])