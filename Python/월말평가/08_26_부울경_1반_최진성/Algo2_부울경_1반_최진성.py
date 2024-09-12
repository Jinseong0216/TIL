T = int(input())    # 테스트 케이스 개수
for tc in range(1, T+1):
    N = int(input())    # 외계인의 수
    info = [list(map(int, input().split())) for _ in range(N)]  # 위험도 Aij
    min_risk = float('inf')     # 최솟값(초기값으로 infinity)

    # visited = 입국심사한 외계인 표시, before = 방금 지나간 외계인, risk = 현재까지 계산된 위험도, cnt = 계산 횟수
    def dfs(visited, before, risk, cnt):
        global min_risk     # 전역변수 수정을 위함(최솟값 업데이트)

        if cnt == N-1:  # 모든 외계인에 대하여 입국심사를 다 했다면
            if min_risk > risk:     # 현재 위험도가 지금까지 계산된 최소 위험도보다 작다면 업데이트
                min_risk = risk
            return

        for after in range(N):  # 다음번에 심사할 외계인 선택
            if visited[after] == 1: continue    # 이미 심사한 외계인 제외
            visited[after] = 1  # 심사한 외계인으로 표시
            dfs(visited, after, risk + info[before][after], cnt + 1)    # after 가 들어온 상황으로 함수를 다시 호출
            visited[after] = 0  # after 를 심사하지 않음으로 다시 초기화


    for alien in range(N):  # 제일 처음 심사 할 외계인을 for 문을 통해서 지정
        VST = [0 if i != alien else 1 for i in range(N)]    # 제일 처음 심사한 외계인 표시
        dfs(VST, alien, 0, 0)   # 함수 호출(1명 심사함, before 로 제일 처음 심사한 외계인, 위험도 0, 계산 횟수 0)
    print(f'#{tc} {min_risk}')


