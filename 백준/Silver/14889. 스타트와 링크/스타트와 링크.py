from itertools import combinations

N = int(input())
M = N // 2

potential_mat = [list(map(int,input().split())) for _ in range(N)]
ans = float('inf')

for teamA in combinations(range(N), M):
    teamB = list(num for num in range(N) if num not in teamA)
    potential_A, potential_B = 0, 0
    for pair in combinations(teamA, 2):
        pair_1, pair_2 = pair
        potential_A += potential_mat[pair_1][pair_2] +  potential_mat[pair_2][pair_1]
    for pair in combinations(teamB, 2):
        pair_1, pair_2 = pair
        potential_B += potential_mat[pair_1][pair_2] +  potential_mat[pair_2][pair_1]

    temp = abs(potential_A-potential_B)
    if ans > temp: ans = temp
    if ans == 0: break

print(ans)