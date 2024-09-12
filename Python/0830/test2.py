# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min_sum, max_sum = float('inf'), float('-inf')
    for idx in range(N-M+1):
        temp = sum(arr[jdx] for jdx in range(idx, idx+M))
        if min_sum > temp: min_sum = temp
        if max_sum < temp: max_sum = temp

    print(f'#{T} {max_sum-min_sum}')


