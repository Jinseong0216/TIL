import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스의 수
T = int(input())
for tc in range(1, T+1):
    # N, M 입력받기
    N, M = map(int, input().split())
    # 배열 입력받고 각 행의 길이를 저장
    arr, row_range = [], []
    for _ in range(N):
        # 행 입력
        row = list(map(int, input().split()))
        # 행 저장 / 각 행의 길이 저장
        arr.append(row), row_range.append(len(row))
    if N < M: print(f'#{tc} -1'); continue;
    # 초기값 지정
    max_sum, min_sum = float('-inf'), float('inf')
    # 최대 열길이로 반복문 시작
    for jdx in range(max(row_range)):
        # 모든 행에 대해서 검사시작
        for idx in range(N):
            # 값 저장 / 구간 길이 기록
            temp, cnt = 0, 0
            for n_idx in range(idx, N):
                # 인덱스 범위 초과시 pass
                if jdx >= row_range[n_idx]: continue
                # 구간합 업데이트
                temp += arr[n_idx][jdx]
                # 길이 업데이트
                cnt += 1
                # 제시된 길이가 되었다면
                if cnt == M:
                    # 최대, 최소 업데이트
                    max_sum = max(max_sum, temp)
                    min_sum = min(min_sum, temp)
                    break

    print(f'#{tc}', max_sum - min_sum)