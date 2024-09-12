T = int(input())
for t in range(1, T+1):
    def find_winner(arr, n):
        if n == 1:
            return arr[0]
        elif n == 2:
            return arr[[0, 0, 1][(arr[0][1] - arr[1][1]) % 3]]
        else:
            i, j = arr[0][0], arr[-1][0]
            n_1, n_2 = ((i+j)//2)-i+1, j-(((i+j)//2)+1)+1
            winner_1 = find_winner(arr[:n_1], n_1)
            winner_2 = find_winner(arr[n-n_2:], n_2)
            return find_winner([winner_1, winner_2], 2)

    N = int(input())
    RSPs = input().split()
    RSPs = [[i+1, int(RSPs[i])] for i in range(N)]
    print(f'#{t} {find_winner(RSPs, N)[0]}')