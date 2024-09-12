T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    min_v = sum(grid[i][i] for i in range(N))
    def cal(num ,i, visited):
        global min_v
        print(num, i, visited)
        if i == N - 1:
            min_v = min(min_v, num)
            return
        elif num < min_v:
            for j in range(N):
                if visited[j] == 0:
                    VST = visited[:]
                    VST[j] = 1
                    cal(num+grid[i+1][j], i+1, VST)
    
    for j in range(N):
        cal(grid[0][j], 0, visited = [int(i == j) for i in range(N)])
    print(f'#{t} {min_v}')