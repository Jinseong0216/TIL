# 깊이 우선 탐색(DFS) 함수 정의
def dfs(now=0):
    global is_continue  # 전역 변수인 is_continue를 사용
    # is_continue가 False이면 더 이상 진행하지 않음 (답을 찾은 후 종료)
    if is_continue == False: return
    # 모든 빈 칸을 다 채운 경우 (스도쿠가 완성된 경우)
    if now == E:
        # 스도쿠 보드를 출력 (완성된 보드)
        for row in grid:
            print(" ".join(list(map(str, row))))
        is_continue = False  # 답을 찾았으므로 더 이상 탐색을 하지 않도록 설정
        return
    # ========= 탈출조건에서 안걸러진 애들 =========

    # 빈 칸의 좌표를 empty_lst에서 꺼내서 사용
    i, j = empty_lst[now]
    # 현재 위치에 들어갈 수 있는 후보 숫자들을 가져와서 시도
    for candidate in possible_numbers((i, j)):
        # 후보 숫자를 해당 칸에 넣기
        grid[i][j] = candidate 
        # 재귀 호출
        dfs(now + 1)
        # 해당 칸을 다시 비우고, 다른 후보를 시도
        grid[i][j] = 0

# 해당 위치(now)에 넣을 수 있는 숫자들을 구하는 함수
def possible_numbers(now):
    # 3x3 박스의 시작 좌표 계산 (해당 위치가 속한 3x3 박스의 왼쪽 상단)
    start_row = (now[0] // 3) * 3  # 행의 시작 인덱스
    start_col = (now[1] // 3) * 3  # 열의 시작 인덱스
    # 1부터 9까지 가능한 숫자들의 집합
    possibles = set(range(1, 10))
    # 해당 행에서 이미 사용된 숫자들을 제외
    possibles -= set(grid[now[0]])
    # 해당 열에서 이미 사용된 숫자들을 제외
    possibles -= set(grid[i][now[1]] for i in range(9))
    # 3x3 박스 내에서 이미 사용된 숫자들을 제외
    possibles -= set(grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3))
    # 가능한 숫자들을 반환
    return possibles

if __name__ == "__main__":
    # 9x9 스도쿠 보드를 입력받음
    grid = [list(map(int, input().split())) for _ in range(9)]  # 각 행을 입력받고 grid에 저장
    # 빈 칸(0인 칸)의 좌표를 empty_lst에 저장
    empty_lst = [(r, c) for r in range(9) for c in range(9) if grid[r][c] == 0]
    # 빈 칸의 개수 (스도쿠에서 0인 칸의 수)
    E = len(empty_lst)
    # 깊이 우선 탐색을 멈출지 여부를 확인하는 플래그 (답을 찾으면 False로 설정)
    is_continue = True
    # 함수 호출
    dfs()
