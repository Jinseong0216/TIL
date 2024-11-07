grid, empty_lst = [], []
for row_index in range(9):
    row = list(map(int, input().split()))
    for col_index in range(9):
        if row[col_index] == 0: 
            empty_lst.append((row_index, col_index))
    grid.append(row)

E = len(empty_lst)

def dfs(now):
    global is_continue

    if is_continue == False: return 
    if now == E: 
        for row in grid:
            print(" ".join(list(map(str, row))))
        is_continue = False
        return 
    i, j = empty_lst[now]
    for candidate in possible_numbers((i, j)):
        grid[i][j] = candidate
        dfs(now+1)
        grid[i][j] = 0


def possible_numbers(now):
    start_row = (now[0] // 3)*3
    start_col = (now[1] // 3)*3

    possibles = set(range(1, 10))
    possibles -= set(grid[now[0]])
    possibles -= set(grid[i][now[1]] for i in range(9))
    possibles -= set(grid[i][j] for i in range(start_row, start_row+3) for j in range(start_col, start_col+3))
    return possibles

is_continue = True
dfs(0)
