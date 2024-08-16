dic = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

N = int(input())    # 주사위 개수

answer = 0
info = [list(map(int, input().split())) for _ in range(N)]
for idx in range(6):
    dice = info[0]
    bottom = dice[idx]
    top = dice[dic[idx]]
    max_sum = max(set(range(1, 7)) - set([top, bottom]))

    for i in range(N-1):
        dice = info[i+1]
        bottom = top
        top = dice[dic[dice.index(bottom)]]
        max_sum += max(set(range(1, 7)) - set([top, bottom]))
    if answer < max_sum: answer = max_sum
print(answer)


