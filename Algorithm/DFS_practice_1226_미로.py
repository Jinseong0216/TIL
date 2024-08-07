def DFS(start, end):
    v = start
    visited = [0]*(16*16+1)
    visited[v] = 1
    stack = []
    stack.append(v)
    while True:
        if v == end:
            return 1
        for w in adjL[v]:
            if visited[w] == 0:
                v = w
                stack.append(v)
                visited[v] = 1
        else:
            if stack:
                v = stack.pop()
            else:
                return 0

for t in range(10):
    T = int(input())
    grid = [list(input().strip()) for _ in range(16)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    adjL = [[] for _ in range(16*16+1)]
    start = end = -1
    for i in range(16):
        for j in range(16):
            for k in range(4):
                ni = i + di[k]
                nj = j +dj[k]
                if 0<= ni < 16 and 0<= nj < 16 and grid[ni][nj] == '0':
                    adjL[16*(i) +(j+1)].append(16*(ni) +(nj+1))
                elif 0<= ni < 16 and 0<= nj < 16 and grid[ni][nj] == '2':
                    start = 16*(ni) +(nj+1)
                elif 0<= ni < 16 and 0<= nj < 16 and grid[ni][nj] == '3':
                    end = 16*(ni) +(nj+1)
                    adjL[16*(i) +(j+1)].append(end)

    print(f'#{T} {DFS(start, end)}')
