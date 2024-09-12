TC = int(input())
for T in range(1, 1+TC):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(f'#{T} {numbers[M%N]}')
