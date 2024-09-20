import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    result = 0
    for i in range(1, -1, -1):      # 뒤에서 부터 조사
        if data[i] >= data[i+1]:    # B가 C보다 양이 많다면
            '''
                B = 3, C = 2일때,
                B가 1이 되어야 하므로
                B와 C의 차에 1개만큼 더 B에서 제거
                B - ((3 - 2) + 1) 
            '''
            result += data[i] - data[i + 1] + 1    # 먹어야 할 사탕 기록
            data[i] -= data[i] - data[i+1] + 1

        if data[i] <= 0:   # 사탕이 0개 이하가 되면 실패
            result = -1
            break
    print(f'#{tc} {result}')