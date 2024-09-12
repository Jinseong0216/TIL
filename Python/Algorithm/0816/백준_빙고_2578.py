def find_bingo():
    cnt = 0
    if [check_list[k][k] for k in range(5)] == [1]*5: cnt += 1
    if [check_list[k][4-k] for k in range(5)] == [1]*5: cnt += 1

    for i in range(5):
        if check_list[i] == [1]*5: cnt += 1
        if [check_list[j][i] for j in range(5)] == [1]*5: cnt += 1
    return cnt


order = [list(map(int, input().split())) for _ in range(5)]
bingo = [0] * 26
for i in range(5):
    for j in range(5):
        num = order[i][j]
        bingo[num] = [i, j]

check_list = [[0]*5 for _ in range(5)]
numbers = []
for _ in range(5): numbers.extend(list(map(int, input().split())))

idx = 0
while idx < 25:
    x, y = bingo[numbers[idx]]
    check_list[x][y] = 1
    idx += 1

    if find_bingo() >= 3: break

print(idx)
