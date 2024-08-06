T = int(input())
for t in range(1,T+1):
    N = int(input())
    M = N // 2
    num = list(range(1,N+1))
    grid = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    subset = []

    for i in range(1, 1<<N):
        bit = [0]*N
        for j in range(16):
            if i & (1 <<j): bit[j] = 1
        if sum(bit) == M:
            subset += [[num[j] for j in range(N) if bit[j] == 1]]

    ans = []
    print(grid)
    for sub in subset:
        print(sub)
        sub_2 = [i for i in range(1,N+1) if i not in sub]
        S = S2 = 0
    
        for i in range(M):
            for j in range(M):
                S += (grid[sub[i]][sub[j]])
                S2 += (grid[sub_2[i]][sub_2[j]])

        ans += [abs(S-S2)]

    print(ans)
# 1
# 4
# 0 5 3 8
# 4 0 4 1
# 2 5 0 3
# 7 2 3 0