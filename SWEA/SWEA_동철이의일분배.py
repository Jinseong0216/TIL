# 배열 최소 합과 같은 문제임
for x in range(1, int(input()) + 1):  # 테스트 케이스 만큼 반복
    N = int(input())  # 일의 수
    info = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]  # 확률 표(크기는 NxN)
    ans = 0
    for idx in range(N): ans *= info[idx][0] / 100  # 초기값으로 설정


    def function(idx, jdx, cummulated, visited):
        global ans

        # 이미 최대값이 될수 없는 경우, 백트래킹
        if cummulated < ans: return
        # 방문체크
        visited[jdx] = True
        # 마지막에 도달한 경우
        if idx == N - 1:
            # 최대값 업데이트
            if ans < cummulated: ans = cummulated
            return
        # 각 열에대한 검사
        for n_jdx in range(N):
            # 방문한 열이면 패스
            if visited[n_jdx]: continue
            # 확률이 0이면 패스
            if not info[idx + 1][n_jdx]: continue
            # 재귀 호출
            function(idx + 1, n_jdx, (cummulated * info[idx + 1][n_jdx]), visited)
            # 방문체크 초기화
            visited[n_jdx] = False


    visited = [False] * N
    for jdx in range(N):
        function(0, jdx, info[0][jdx], visited)
        visited[jdx] = False

    print(f'#{x} {round(ans * 100, 6):.6f}')
