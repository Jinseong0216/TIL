def dfs(now=0):
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


if __name__ == "__main__": 
    # 받아온 자료
    grid = [list(map(int, input().split())) for _ in range(9)]
    # 빈 공간
    empty_lst = [(r, c) for r in range(9) for c in range(9) if grid[r][c] == 0]
    # 빈 공간의 수
    E = len(empty_lst)
    # dfs멈춤 플래그
    is_continue = True
    # 함수 호출
    dfs()