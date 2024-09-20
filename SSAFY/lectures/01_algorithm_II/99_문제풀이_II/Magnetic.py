N_pole = 1 # 1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체
S_pole = 2 # 테이블의 윗부분에 N극이 아래부분에 S극이 위치

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0     # 교착상태 수
    for j in range(100): # 열 우선
        np = 0  # 아래로 향하는 N극이 있는지 표시
        for i in range(100):
            if arr[i][j] == N_pole:
                np = 1
            elif arr[i][j] == S_pole and np == 1: # N극과 S극이 만나는 경우 교착
                cnt += 1
                np = 0
    print(f'#{tc} {cnt}')