    grid = [[0]*100 for _ in range(100)]

    for _ in range(4):
        a, b, c, d = map(int,input().split())
        for x in range(a,c):
            for y in range(b,d):    # 직사각형이 지나가는 부분은 1로표시
                grid[x][y] = 1

    print(sum(sum(grid[i]) for i in range(100)))