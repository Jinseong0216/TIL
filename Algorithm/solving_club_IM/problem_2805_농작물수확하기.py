T = int(input())
for t in range(1, T+1):
    N = int(input())
    M = N//2
    weights = list(range(M, 0, -1)) + list(range(M+1))
    income = 0
    for i in range(N):
        floor_i_th = list(map(int, input()))
        income += sum(floor_i_th[weights[i] : N-weights[i]])

    print(f'#{t}', income)
