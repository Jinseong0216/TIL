# grid는 스도쿠의 현재 상태를 저장할 9x9 격자 (2차원 리스트)
grid, empty_lst = [], []

# 9x9 스도쿠 보드를 입력받음
for row_index in range(9):
    row = list(map(int, input().split()))  # 각 행을 입력받고
    for col_index in range(9):
        if row[col_index] == 0:  # 값이 0인 칸(빈 칸)을 찾아서
            empty_lst.append((row_index, col_index))  # 빈 칸의 좌표를 empty_lst에 저장
    grid.append(row)  # 스도쿠 격자에 해당 행을 추가

# 빈 칸의 개수를 E에 저장
E = len(empty_lst)

# 깊이 우선 탐색(DFS) 함수 정의
def dfs(now):
    global is_continue

    # 이미 해답을 찾았다면 더 이상 진행하지 않도록 종료
    if is_continue == False: return

    # 빈 칸을 모두 채웠다면(스도쿠 완성)
    if now == E:
        # 스도쿠 완성된 보드를 출력
        for row in grid:
            print(" ".join(list(map(str, row))))  # 각 행을 공백으로 구분하여 출력
        is_continue = False  # 더 이상 진행하지 않도록 플래그를 변경
        return

    # 빈 칸의 위치를 찾는다 (empty_lst[now]에서 현재 빈 칸의 위치를 얻음)
    i, j = empty_lst[now]

    # 현재 빈 칸에 들어갈 수 있는 숫자들을 찾아서 시도해본다.
    for candidate in possible_numbers((i, j)):
        grid[i][j] = candidate  # 가능한 숫자를 해당 칸에 넣고
        dfs(now + 1)  # 다음 빈 칸으로 이동하여 재귀적으로 깊이 우선 탐색
        grid[i][j] = 0  # 다시 그 칸을 비워두고 다른 후보를 시도

# 현재 빈 칸에 들어갈 수 있는 숫자들을 계산하는 함수
def possible_numbers(now):
    # 3x3 박스의 시작 좌표를 계산
    start_row = (now[0] // 3) * 3  # 현재 행의 3x3 박스 시작 행
    start_col = (now[1] // 3) * 3  # 현재 열의 3x3 박스 시작 열

    # 1부터 9까지 가능한 숫자들을 모두 set으로 생성
    possibles = set(range(1, 10))

    # 현재 행에서 사용된 숫자들을 제외
    possibles -= set(grid[now[0]])

    # 현재 열에서 사용된 숫자들을 제외
    possibles -= set(grid[i][now[1]] for i in range(9))

    # 현재 3x3 박스에서 사용된 숫자들을 제외
    possibles -= set(grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3))

    return possibles  # 가능한 숫자들을 반환

# DFS 탐색을 시작하기 전에 스도쿠가 채워져있는 상태에서 빈 칸의 좌표를 담은 empty_lst와 함께 탐색 시작
is_continue = True  # 탐색을 계속할지 여부를 확인하는 플래그
dfs(0)  # 탐색을 시작
