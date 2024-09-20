import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    min_v = sum(data)   # 충분히 큰 수
    max_v = 0           # 충분히 작은 수
    '''
        N = 7
        M = 3
        data = [A, B, C, D, E, F, G] 인 경우
        
        index 정보는 아래와 같다.
         0  1  2  3  4  5  6
        [A, B, C, D, E, F, G]
        
        일반적인 전수조사라면, i가 0부터 6이 될 때까지
        즉, range(N) == range(7)   {range는 0부터, N-1 까지의 정수 모음이므로}
        가 되어야 하지만, 구간인 M 만큼씩 조사하고 싶다면
        
        아래와 같이 조사 할 수 있어야 하므로,
         0  1  2 
        [A, B, C]               i = 0, 최대 범위 = 2 range(0, 3)
            1  2  3
           [B, C, D]            i = 1, 최대 범위 = 3 range(1, 4)
            ...
                  3  4  5
                 [D, E, F]      i = 3, 최대 범위 = 5 range(3, 6)
                     4  5  6
                    [E, F, G]   i = 4, 최대 범위 = 6 range(4, 7)
                    
        각 모든 구간에 대한 범위 설정이 곧, range(i, i+M) 이 되어야 한다.      
    '''
    for i in range(N-M+1):  # i + M개 만큼의 구간을 더할 것이므로 -M
        tmp = 0             # 각 구간마다의 합을 기록
        for j in range(i, i+M):     # 그 i번쨰부터 i+M까지
            # print(data[j], end='')  # 범위가 올바르게 적용됐는지 체크
            tmp += data[j]
        # i + M 크기 구간 만큼의 모든 정수를 더했다면, 최소 최대 값 비교
        if min_v >= tmp:    # 충분히 큰 수보다 tmp가 작다면,
            min_v = tmp     # 더 작은 수로 min_v 재 할당
        if max_v <= tmp:    # 충분히 작은 수 보다 tmp가 크다면,
            max_v = tmp     # 더 큰 수로 max_v 재 할당
    print(f'#{tc} {max_v - min_v}') # 두 수의 차를 출력
