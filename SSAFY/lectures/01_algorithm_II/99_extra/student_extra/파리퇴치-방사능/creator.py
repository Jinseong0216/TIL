import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 입력
T = int(input())

# T만큼 반복
for tc in range(1, T+1) :
    # NxN 배열, MxM 배열, 감염된 파리가 B칸에 있음
    N, M, B = map(int, input().split())

    # B칸의 행과 열
    radiation = []
    for _ in range(B) :
        a, b = map(int, input().split())
        radiation.append([a-1, b-1])
    # 파리의 수가 있는 배열
    arr = [list(map(int, input().split())) for _ in range(N)]


    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]

    result = []

    # 반복
    for i in range(N) :
        for j in range(N) :
            # 파리의 수를 더할 변수
            flies = 0

            # 파리를 죽인 칸을 담을 리스트
            temp = []
            # 파리채 크기만큼 죽여야하니까 간다
            # 한 줄씩 왼 -> 오
            for k in range(M) :
                for l in range(M) :
                    temp_i = i + k
                    temp_j = j + l
                    # 범위 안에 있고 그 칸에 있는 파리를 죽이지 않았으면
                    if 0 <= temp_i < N and 0 <= temp_j < N and [temp_i, temp_j] not in temp :
                        # 파리 수를 더하고
                        flies += arr[temp_i][temp_j]
                        # 파리를 죽인 칸을 temp에 기록한다
                        temp.append([temp_i, temp_j])
                        # 방사능 파리를 만나면
                        if [temp_i, temp_j] in radiation :
                            # 대각선 방향을 봐야하니까 ??
                            for w in range(4) :
                                radi_temp_i = temp_i + dx[w]
                                radi_temp_j = temp_j + dy[w]
                                # 범위 안에 있고 그 칸에 있는 파리를 죽이지 않았으면
                                if 0 <= radi_temp_i < N and 0 <= radi_temp_j < N and [radi_temp_i, radi_temp_j] not in temp :
                                    # 죽인 파리 수를 더하고
                                    flies += arr[radi_temp_i][radi_temp_j]
                                    # 파리를 죽인 칸을 temp에 기록한다
                                    temp.append([radi_temp_i, radi_temp_j])
            # print(i, j, 'temp:', temp)
            result.append(flies)
    # print(result)
    max_result = max(result)
    print(result.index(max_result))
    print(f'#{tc} {max(result)}')