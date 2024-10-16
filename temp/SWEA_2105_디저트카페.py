import sys
sys.stdin = open('input.txt')

def solution(now, dij_idx, number_of_desert):
    global ans

# 탈출 조건 지정파트
    # 마지막 방향이면서 / 처음 시작위치로 돌아왔다면 함수는 종료됨
    if dij_idx == 3 and now == start:
        # 만약 경로에서 찾은 디저트의 개수가 기존보다 많다면 업데이트
        if ans < number_of_desert: ans = number_of_desert
        return

# Case1) 방향성을 유지하며, 한 칸 이동    
    # 현재 위치
    i, j = now
    # 델타
    di, dj = dij[dij_idx]
    # 다음 위치 설정
    ni, nj = i+di, j+dj
    # out of range 피하기
    if 0 <= ni < N and 0 <= nj < N:
        # 다음 위치의 디저트
        desert = grid[ni][nj]
        # 아직 먹지않은 디저트라면
        if ate[desert] == False:
        # 먹음 체크
            ate[desert] = True
            # 함수 호출
            solution([ni, nj], dij_idx, number_of_desert+1)
            # 먹음 해제
            ate[desert] = False

# Case2) 방향성 유지X, 한 칸 이동
    # 마지막 방향이 아닌 경우에만 적용
    if dij_idx < 3:
        # 현재 위치
        i, j = now
        # 델타
        di, dj = dij[dij_idx+1]
        # 다음 위치 설정
        ni, nj = i+di, j+dj
        # out of range 피하기
        if 0 <= ni < N and 0 <= nj < N:
            # next 위치의 디저트
            desert = grid[ni][nj]
            # 아직 먹지않은 디저트라면
            if ate[desert] == False:
                # 먹음 체크
                ate[grid[ni][nj]] = True
                # 함수 호출
                solution([ni, nj], dij_idx+1, number_of_desert+1)
                # 먹음 해제
                ate[grid[ni][nj]] = False

        
# 테스트 케이스의 수          
T = int(input())
# 테스트 케이스별 반복
for t in range(1, T+1):
    # 그리드의 크기
    N = int(input())
    # 디저트의 정보를 담은 그리드
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 디저트 종류 먹음 체크를 위한 배열
    ate = [False]*(100+1)
    # 델타(이번 문제에서는 해당 순서대로 움직임)    
    dij = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    # 정답 초기값
    ans = 0
    for i in range(N):
        for j in range(N):
            # 시작위치, 먹은지 체크하기 위한 ate 리스트 만들기
            start = [i, j]
            # 함수 호출
            solution(now=[i, j], dij_idx=0, number_of_desert=0)

    # 답 출력
    if ans == 0: print(f'#{t} {-1}')
    else: print(f'#{t} {ans}')

