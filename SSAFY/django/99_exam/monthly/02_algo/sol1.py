import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N2 = input()
    result = 1  # 최종 결괏값의 최솟값은 1

    # 모든 범위에 대해서 전수 조사
    for i in range(N):
        # 내 위치 i번째를 기준으로
        # 좌,우에 동일한 범위 만큼 빼거나 더한게
        # 같은지 봐야한다.
        # tmp = 1
        range_idx = 1
        while 0 <= i - range_idx and i + range_idx < N and N2[i - range_idx] == N2[i + range_idx]:
            range_idx += 1
        if result < (range_idx - 1) * 2 + 1:
            result = (range_idx - 1) * 2 + 1
        # while True:     # 언제까지 조사해야 할지 모르겠으니..
        #     range_left = i - range_idx  # 왼쪽
        #     range_right = i + range_idx # 오른쪽
        #     # 범위 설정
        #     if range_left >= 0 and range_right < N:
        #         # 범위내 값이 대칭인지 확인
        #         if N2[range_left] == N2[range_right]:
        #             # 같으면 뭘할까?
        #             tmp += 2
        #             range_idx += 1
        #             if result < tmp:
        #                 result = tmp
        #         else:
        #             break
        #     else:
        #         break

    # 최종 출력
    print(f'#{tc} {result}')
